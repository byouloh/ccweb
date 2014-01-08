#!/usr/bin/python
# -*- coding=utf-8 -*-
import os.path
import tornado.web
from libs import libs4mongodb
from blog import handlers as handler
from blogconfig import DATABASE, COOKIE_SECRET, DEBUG

class Application(tornado.web.Application):
    def __init__(self):
        handlers = handler
        settings = dict(
                template_path = os.path.join(os.path.dirname(__file__), "templates"),
                static_path = os.path.join(os.path.dirname(__file__), "static"),
                xsrf_cookies = True,
                cookie_secret = COOKIE_SECRET,
                debug = DEBUG,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = libs4mongodb.Connection(DATABASE)
        print "__init__:", self.db._db.post

