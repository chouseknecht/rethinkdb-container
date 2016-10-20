#!/bin/bash

if [ ! "$(ls -A /data)" ]; then
    # if the data dir is empty, create a new database 
    rethinkdb create --directory /data
fi

exec "$@"
