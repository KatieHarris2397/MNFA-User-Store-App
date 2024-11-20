#!/usr/bin/env bash
echo "Creating mongo users..."
mongosh --authenticationDatabase admin --host localhost -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD $MONGO_INITDB_DATABASE --eval "db.createUser({user: '$MONGO_INITDB_ROOT_USERNAME', pwd: '$MONGO_INITDB_ROOT_PASSWORD', roles: [{role: 'readWrite', db: '$MONGO_INITDB_DATABASE'}]});"
echo "Mongo users created."