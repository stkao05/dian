import requests
import codecs
import json
import shutil
from bs4 import BeautifulSoup
import pprint
import data


POST_TEMPLATE = u"""
---
layout: post
title:  "{title}"
date:   {timestamp}
categories: {categories}
---
{content}
"""



def read_post(path):
    with open(path, "r") as f:
        soup = BeautifulSoup(f, "html5lib")

    title = soup.select("#content > div > h2 > span.titlename")[0].contents[0]
    y = soup.select("#content > div > h2 > span.titledate > span.titledate-year")[0].contents[0]
    m = soup.select("#content > div > h2 > span.titledate > span.titledate-month")[0].contents[0]
    d = soup.select("#content > div > h2 > span.titledate > span.titledate-day")[0].contents[0]
    h = soup.select("#content > div > h2 > span.titledate > span.titledate-hour")[0].contents[0]
    mm = soup.select("#content > div > h2 > span.titledate > span.titledate-min")[0].contents[0]

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

    dest_path = "./dian/_posts/" + file_name

    with codecs.open(dest_path, 'w', encoding='utf8') as f:
        content = POST_TEMPLATE.format({
            title=title,
            timestamp=timestamp,
        })

        f.write(content)


    # post_data = dict(
        # title=title
    # )

    # print file_name




# for fname in data.post_file_paths:
    # post_path = "./raw/post/" + fname
    # read_post(post_path)




test_post = "./raw/post/blog.xuite.net|music_dian|wretch|141767176.html"
read_post(test_post)



################################


# with open("./html/post_url_list.json", "r") as f:
    # post_urls = json.loads(f.read())

# for url in post_urls:
    # path = "./html/posts/" + url.replace("//", "").replace("/", "|") + ".html"

    # with open(path, "r") as f:
        # soup = BeautifulSoup(f, "html5lib")
        # img = soup.select("#content_all img")
        # urls = [_.get("src") for _ in img]
        # img_urls = img_urls + urls


# with open('html/img_urls.json', 'w') as f:
    # json.dump(img_urls, f, indent=4, separators=(',', ': '))



# def save_html_response(response, path):
    # if response.encoding is not "utf-8":
        # response.encoding = "utf-8"

    # html = response.text

    # with codecs.open(path, 'w',encoding='utf8') as f:
        # f.write(html)


# with open("./html/img_urls.json", "r") as f:
    # img_urls = json.loads(f.read())


# i = 0

# for url in img_urls:
    # print i, len(img_urls)
    # try:
        # r = requests.get(url, stream=True, timeout=5)

        # if r.status_code == 200:
            # path = "./html/img/" + url.replace("http://", "").replace("https://", "").replace("/", "|")

            # with open(path, 'wb') as f:
                # r.raw.decode_content = True
                # shutil.copyfileobj(r.raw, f)
    # except Exception as e:
        # print "error", e

    # i = i + 1



################################



# save image url

# img_urls = []

# with open("./html/post_url_list.json", "r") as f:
    # post_urls = json.loads(f.read())

# for url in post_urls:
    # path = "./html/posts/" + url.replace("//", "").replace("/", "|") + ".html"

    # with open(path, "r") as f:
        # soup = BeautifulSoup(f, "html5lib")
        # img = soup.select("#content_all img")
        # urls = [_.get("src") for _ in img]
        # img_urls = img_urls + urls


# with open('html/img_urls.json', 'w') as f:
    # json.dump(img_urls, f, indent=4, separators=(',', ': '))



################################


# download individual posts

# with open("./html/post_url_list.json", "r") as f:
    # post_urls = json.loads(f.read())

# i = 0

# for url in post_urls:
    # print i

    # url = "https:" + url
    # res = requests.get(url)
    # path ="./html/posts/%s.html" % url.replace("https://", "").replace("/", "|")
    # save_html_response(res, path)

    # i = i + 1



# list_urls = ["https://blog.xuite.net/music_dian/wretch?&p=%d" % i for i in range(0, 22)]

# for url in list_urls:
    # res = requests.get(url)
    # path ="./html/post_lists/%s.html" % url.replace("https://", "").replace("/", "|")
    # save_html_response(res, path)


# list_html_paths = ["./html/post_lists/blog.xuite.net|music_dian|wretch?&p=%d.html" % i for i in range(1, 22)]
# post_urls = []

# for path in list_html_paths:
    # with open(path, "r") as f:
        # soup = BeautifulSoup(f, "html5lib")
        # anchors = soup.select("#content > div > h3 > span.titlename > a")
        # urls = [_.get("href") for _ in anchors]

        # post_urls = post_urls + urls


# with open('html/post_url_list.json', 'w') as f:
        # json.dump(post_urls, f, indent=4, separators=(',', ': '))

# print post_urls
