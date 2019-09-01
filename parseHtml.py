#-*- coding:utf-8 -*-
__author__ = "longqiuhong"
from bs4  import BeautifulSoup
import re

def indexTags(html):
    soup = BeautifulSoup(html,'lxml')
    tags = soup.find(class_='tags')
    tags = tags.find_all('a')

    result = []
    for tag in tags:

        tmp = {
            'link':tag['href'],
            'name':tag.string
        }

        result.append(tmp)

    return result



def getNextPage(html,host):
    soup = BeautifulSoup(html, 'lxml')
    page = soup.find(class_='thisclass')
    pageNextLi = page.find_next().string
    nextPage = 0
    if pageNextLi.isalnum() == True:
        nextPage = int(page.text) + 1

    # nextPage = host+ 'a/list_1_'+ str(nextPage) +'.html'
    return nextPage

def parseList(html):
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find(class_='wp-list')
    wpItems = list.find_all(class_='wp-item')
    result = []
    for wpItem in wpItems:
        tmp = {
            'link': wpItem.h3.a['href'],
            'name': wpItem.h3.a.string
        }
        result.append(tmp)
    return result



def parseDeil(html):
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.find(id='picture')
    imgs = imgs.find_all('img')
    result = []
    for img in imgs:
        tmp ={
            'img':img['src']
        }
        result.append(tmp)
    return result