from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from neo4j import GraphDatabase

import os

app = FastAPI()

# MongoDB Configuration
MONGO_USERNAME = os.getenv("MONGODB_USERNAME")
MONGO_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGO_HOST = os.getenv("MONGODB_HOST")
MONGO_URI = "mongodb://" + MONGO_USERNAME + ":" + MONGO_PASSWORD + "@" + MONGO_HOST + "/"
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[os.getenv("MONGODB_DB")]
mongo_collection = mongo_db["users"]

# Neo4j Configuration
NEO4J_URI = os.getenv("NEO4J_URL")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
neo4j_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

@app.post("/api/user/")
async def create_user(user: dict):
    # Add user to MongoDB
    user_id = mongo_collection.insert_one(user).inserted_id
    user["id"] = str(user_id)
    
    # Add user to Neo4j graph
    with neo4j_driver.session() as session:
        session.run(
            "CREATE (u:User {id: $id, name: $name, email: $email})",
            id=str(user_id), name=user.get("name"), email=user.get("email")
        )
    return {"message": "User created successfully", "user": user}

@app.get("/api/user/{user_id}")
async def get_user(user_id: str):
    # Fetch user from MongoDB
    user = mongo_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch related graph data from Neo4j
    with neo4j_driver.session() as session:
        result = session.run(
            "MATCH (u:User {id: $id}) RETURN u", id=user_id
        ).single()
        graph_data = result["u"] if result else {}

    return {"user": user, "graph_data": graph_data}