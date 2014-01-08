#!/usr/bin/python
# -*- coding=utf-8 -*-

import urllib2
import lxml.html
from pymongo import Connection

conn = Connection()
dbs = conn.test
posts = dbs.post

def get_next_page(url):
    page = urllib2.urlopen(url)
    raw_data = page.read().replace('\x00', '')
    dom = lxml.html.fromstring(raw_data.decode('utf8', 'ignore'), parser = lxml.html.HTMLParser(remove_comments = True))
    np_dom =  dom.xpath('//ul[@class="y_page clearfix"]/li/a')[-1]
    return np_dom.attrib["href"]

def yiyan_spider(url=''):
    page = urllib2.urlopen(url)
    raw_data = page.read().replace('\x00', '')
    dom = lxml.html.fromstring(raw_data.decode('utf8', 'ignore'), parser = lxml.html.HTMLParser(remove_comments = True))
    for d in dom.xpath('//div[@class="y_space_article"]'):
        avatar =  d.xpath('.//div[@class="img_l"]/a/img')[0].attrib['src']
        author =  d.xpath('.//div[@class="number_t"]/a')[0].text
        title =  d.xpath('.//h3/a')[0].text
        t_link =  d.xpath('.//h3/a')[0].attrib["href"]
        abstract =  d.xpath('.//p')[0].text

        post = {"avator": avatar,
                 "author": author,
                 "title" : title,
                 "t_link": t_link,
                 "abstract": abstract
        }

        posts.insert(post)

if __name__ == '__main__':
    url = "http://article.yeeyan.org"
    #http://article.yeeyan.org/lists/new/7
    #yiyan_spider(url)
    print url + get_next_page(url)


