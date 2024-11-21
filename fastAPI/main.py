import os
from typing import Optional, List

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing_extensions import Annotated

from bson import ObjectId
from pymongo import MongoClient, ReturnDocument
from neo4j import GraphDatabase

import os

app = FastAPI(
    title="MNFA User Store App",
)

# MongoDB Configuration
MONGO_URI = os.getenv("MONGODB_URL")
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[os.getenv("MONGODB_DB")]
mongo_collection = mongo_db["users"]

# Neo4j Configuration
NEO4J_URI = os.getenv("NEO4J_URL")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
neo4j_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Represents an ObjectId field in the mongo database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

@app.post("/api/user/", response_model=User)
async def create_user(user: User = Body(...)):
    # Add user to MongoDB
    new_user = mongo_collection.insert_one(user.model_dump(by_alias=True, exclude=["id"]))

    created_user = mongo_collection.find_one({"_id": new_user.inserted_id})
    
    # Add user to Neo4j graph
    with neo4j_driver.session() as session:
        session.run(
            "CREATE (u:User {name: $name, email: $email})",
            name=user.model_dump(by_alias=True).name, email=user.model_dump(by_alias=True).email
        )
    return created_user

@app.get("/api/user/{user_email}")
async def get_user(user_email: str):
    # Fetch user from MongoDB
    user = mongo_collection.find_one({"email": user_email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch related graph data from Neo4j
    with neo4j_driver.session() as session:
        result = session.run(
            "MATCH (u:User {email: $email}) RETURN u", email=user_email
        ).single()
        graph_data = result["u"] if result else {}

    return {"user": user, "graph_data": graph_data}