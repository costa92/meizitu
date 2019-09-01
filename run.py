#-*- coding:utf-8 -*-
__author__ = "longqiuhong"

import requestHttp
import parseHtml
import time
import file
import urllib.request
import socketImg
import os
import requests

def getIndex(host,page):

    url = host + "a/list_1_"+ str(page)+".html"
    html = requestHttp.getHttp(url)
    nextPage = parseHtml.getNextPage(html,host)
    print(nextPage)
    if page == 0:
        print("已经全部下载完妹子图了！")
        exit()

    parseMeizitu(html, host, nextPage)


# 选择html代码并且下载图片
def parseMeizitu(html,host,page):
    lists = parseHtml.parseList(html)
    for list in lists:
        time.sleep(2)
        filePath = "img/" + list['name']
        file.mkdir(filePath)
        deilHtml = requestHttp.getHttp(list['link'])
        imgs = parseHtml.parseDeil(deilHtml)

        for i, img in enumerate(imgs):
            filename = filePath + '/' + str(i) + '.jpg'  # 保持图片路径
            print ('开始下载图片：' + img['img'])

            if os.path.exists(filename) == False:  # 判断图片是否存在
                # auto_down(img['img'],filename)
                getDown(img['img'], filename)
            else:
                print ('下载图片：' + img['img'] + '已经存在')
            print ('结束下载图片：' + filename)
    getIndex(host,page)

# 下载图片
def auto_down(url,filename):
    try:
        urllib.request.urlretrieve(url,filename)
    except urllib.request.ContentTooShortError:
        print ('Network conditions is not good.Reloading.')
        auto_down(url,filename)

#  下载图片
def getDown(url,filename):
    r = requests.get(url)
    if(r.content):
        with open(filename, 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':
    host = "https://www.meizitu.com/"
    getIndex(host,page=1)