#!/usr/bin/env python

import rethinkdb as rdb
import json 

rdb.connect('localhost', 28015).repl()
rdb.db('test').table_create('tv_shows').run()
rdb.table('tv_shows').insert({ 'name': 'Star Trek TNG' }).run()

cursor = r.table("tv_shows").run()
for doc in cursor:
    json.dumps(doc, indent=4, separators=(',', ': '))
