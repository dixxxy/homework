# http://tieba.baidu.com/f?kw=%C9%FA%BB%EE%B4%F3%B1%AC%D5%A8&fr=ala0&tpl=5
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author dixxxy
# @version 2017-07-27

import requests
import re
import time
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "ERROR"

def print_result(url):
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    match_list = soup.find_all('div',attrs={'class':'matchmain bisai_qukuai'})
    for match in match_list:
        time = match.find('div',attrs={'class':'whenm'}).text.strip()
        teamname = match.find_all('apan',attrs={'class':'team_name'})

        if teamname[0] == 'php':
            team1_name = "暂无队名"
        else:
            team1_name = teamname[0].string

        team1_support_level = match.find('span',class_='team_number_green').string
        team2_name = teamname[1].string
        team2_support_level = match.find('span',class_='team_number_red').string
        print('比赛时间：{}，\n 队伍一：{}      胜率 {}\n 队伍二：{}      胜率 {} \n'.format(time, team1_name, team1_support_level,
                                                                           team2_name, team2_support_level))


def main():
    url= 'http://dota2bocai.com/match'
    print_result(url)

if __name__ == '__main__':
    main()