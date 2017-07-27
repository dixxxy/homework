#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author dixxxy
# @version 2017-07-26

import requests
from bs4 import BeautifulSoup
import time
from http import cookiejar


headers = {
    "Host":"www.zhihu.com",
    "Referer":"http://www.zhihu.com/",
    'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_10_5)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
}

#使用登录cookie信息
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
try:
    print(session.cookies)
    session.cookies.load(ignore_discard=True)
except:
    print("load cookies failed")

def get_xsrf():
    response = session.get("http://www.zhihu.com",headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    xsrf = soup.find('input',attrs={"name":"_xsrf"}).get("value")
    return xsrf

def get_captcha():
    """
    把验证码照片保存到当前目录，手动识别验证码
    :return:
    """
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r='+ t + "&type=login"
    r = session.get(captcha_url,headers=headers)
    with open('captcha.jpg','wb') as f:
        f.writer(r.content)
    captcha = input("验证码:")
    return captcha

def login(email,password):
    login_url = 'https://www.zhihu.com/login/email'
    data = {
        'email':email,
        'password':password,
        '_xsrf':get_xsrf(),
        "captcha":get_captcha(),
        'remember_me':'true'}
    response = session.post(login_url,data=data,headers=headers)
    login_code = response.json()
    print(login_code['msg'])
    for i in session.cookis:
        print(i)
    session.cookies.save()

if __name__ == '__main__':
    email = "xiayang531645339@qq.com"
    password = "101010dxya."
    login(email,password)

