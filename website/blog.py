#!/usr/bin/python
#-*- coding=utf-8 -*-
from libs.models import PostMixin
from libs.handler import BaseHandler

class HomeHandler(BaseHandler, PostMixin):
    def get(self):
        print "handler:" ,self.db
        posts = self.get_count_posts(5)
        self.render("index.html", posts=posts)

handlers = [('/', HomeHandler),
]
