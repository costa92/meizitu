#-*- coding:utf-8 -*-
__author__ = "longqiuhong"
import  urllib.request

def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print( path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path + ' 目录已存在')
        return False


def download_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64;'
                        ' Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;'
                        ' Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


