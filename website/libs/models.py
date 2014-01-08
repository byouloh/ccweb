#!/usr/bin/python
#-*- coding=utf-8 -*-
import json
from bson import json_util
class PostMixin(object):
    def get_count_posts(self, count=None):
        if count:
            coll = self.db._db.post
            posts = coll.find()
            return posts
            #return str(json.dumps({'results':list(posts)},default=json_util.default))

