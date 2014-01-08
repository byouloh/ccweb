#!/usr/bin/python
import pymongo
from tornado.options import define, options
define("mongo_url", default="localhost", help="location of mongodb", type=str)
define("mongo_port", default=27017, help="port mongodb is listening on", type=int)
define("mongo_dbname", default="test", help="name of the database", type=str)

class Connection(object):
    def __init__(self, db_name):
        try:
            conn = pymongo.Connection(options.mongo_url, options.mongo_port)
            self._db = conn[options.mongo_dbname]
            print "SELF_DB:", self._db
        except:
            raise
