#-*- coding:utf-8 -*-
__author__ = "longqiuhong"
import requests
from requests import exceptions


def getHttp(url,params=''):
    try:
        headers = getHeaders()
        response = requests.get(url, params=params, headers=headers)
        if(response.status_code == requests.codes.ok):
            response.encoding = 'gb18030'
            return response.text
    except exceptions.ConnectTimeout:
        print ("请求链接超时")


def getHeaders():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    return  headers
