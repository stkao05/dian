# -*- coding: utf-8 -*-

import requests
import codecs
import json
import shutil
from bs4 import BeautifulSoup
import pprint
import data
from sets import Set
from collections import defaultdict
import re

rex_dot_sanitize = re.compile(r"([^\.]*)(\.+)", re.IGNORECASE)

def sanitize_file_name(file_name):
    res = file_name

    res = res.replace("/", "-")

    m = rex_dot_sanitize.match(file_name)
    if m:
        res = m.group(1)

    if res != file_name:
        print "Convert file name '" + file_name + "' to '" + res + "'"

    return res



POST_TEMPLATE = u"""---
layout: post
title:  "{title}"
date:   {timestamp}
categories: {category}
---
{content}
"""

all_tags = Set()
checkes = defaultdict(list)

def read_post(path):
    with open(path, "r") as f:
        soup = BeautifulSoup(f, "html5lib")

    title = soup.select("#content > div > h2 > span.titlename")[0].contents[0]
    y = soup.select("#content > div > h2 > span.titledate > span.titledate-year")[0].contents[0]
    m = soup.select("#content > div > h2 > span.titledate > span.titledate-month")[0].contents[0]
    d = soup.select("#content > div > h2 > span.titledate > span.titledate-day")[0].contents[0]
    h = soup.select("#content > div > h2 > span.titledate > span.titledate-hour")[0].contents[0]
    mm = soup.select("#content > div > h2 > span.titledate > span.titledate-min")[0].contents[0]

    category = soup.select("#content > div > div.blogrank div span.category > a")[0].contents[0]
    category = category.replace(u"♪", "").strip()

    content = unicode(soup.select("#content_all")[0])

    title = title.replace("\"", "'")

    # contents = soup.select("#content_all")[0].contents
    # for _ in contents:
        # all_tags.add(_.name)

        # if (_.name == "table" or
                # _.name == "ul" or
                # _.name == "span" or
                # _.name == "font" or
                # _.name == "blockquote"):

            # checkes[_.name].append(path)

    timestamp = "{y}-{m}-{d} {h}:{mm}:00 +0800".format(
        y=y,
        m=m,
        d=d,
        h=h,
        mm=mm
    )

    file_name = u"{y}-{m}-{d}-{title}".format(
        y=y,
        m=m,
        d=d,
        title=title
    )
    file_name = sanitize_file_name(file_name)

    dest_path = "./dian/_posts/" + file_name + ".markdown"


    categories = ""

    with codecs.open(dest_path, 'w', encoding='utf8') as f:
        fcontent = POST_TEMPLATE.format(
            title=title,
            timestamp=timestamp,
            category=category,
            content=content
        )

        f.write(fcontent)


def main():
    # test_post = "./raw/post/blog.xuite.net|music_dian|wretch|141767176.html"
    # read_post(test_post)

    # print all_tags
    # pprint.pprint(checkes)

    for fname in data.post_file_paths:
        post_path = "./raw/post/" + fname
        read_post(post_path)
        print "."

    pass


if __name__ == "__main__":
    main()

