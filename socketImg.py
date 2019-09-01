__author__ = "longqiuhong"
import socket
import urllib.request
#设置超时时间为30s
socket.setdefaulttimeout(30)
#解决下载不完全问题且避免陷入死循环


def autImg(url,image_name):
    try:
        urllib.request.urlretrieve(url, image_name)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(url, image_name)
                break
            except socket.timeout:
                err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                print(err_info)
                count += 1
        if count > 5:
            print("downloading picture fialed!")



