# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 20:31
# @Author  : -- CXS --
# @File    : bilibili_anime_spider.py

"""
追番人数：679万追番
https://api.bilibili.com/pgc/season/index/result?st=1&year=%5B2019%2C2020)&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=3&sort=0&page={}&season_type=1&pagesize={}&type=1
播放量：9324.6万次播放
https://api.bilibili.com/pgc/season/index/result?st=1&year=%5B2019%2C2020)&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=2&sort=0&page={}&season_type=1&pagesize={}&type=1
评分：9.9分
https://api.bilibili.com/pgc/season/index/result?st=1&year=%5B2019%2C2020)&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=4&sort=0&page={}&season_type=1&pagesize={}&type=1

请求头：
Accept: application/json, text/plain, */*
Origin: https://www.bilibili.com
Referer: https://www.bilibili.com/anime/index/
Sec-Fetch-Mode: cors
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
"""

import requests
import json
import math
import pymongo

# 数据初始链接
watch_url = 'https://api.bilibili.com/pgc/season/index/result?st=1&year=%5B2019%2C2020)&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=3&sort=0&page={}&season_type=1&pagesize={}&type=1'
play_url = 'https://api.bilibili.com/pgc/season/index/result?st=1&year=%5B2019%2C2020)&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=2&sort=0&page={}&season_type=1&pagesize={}&type=1'
grade_url = 'https://api.bilibili.com/pgc/season/index/result?st=1&year=%5B2019%2C2020)&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=4&sort=0&page={}&season_type=1&pagesize={}&type=1'

# 连接mongodb
client = pymongo.MongoClient(host = "127.0.0.1",port = 27017)
collection_watch_nums = client['anime']['watch_nums']
collection_play_nums = client['anime']['play_nums']
collection_grade = client['anime']['grade']

# 获取返回结果，并用json解析
def get_json_content(url):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://www.bilibili.com',
        'Referer': 'https://www.bilibili.com/anime/index/',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    response = requests.get(url,headers = headers)
    content = response.content.decode()
    json_data = json.loads(content)
    return json_data

# 生成请求，并yield结果
def get_anime_list(each_url):
    url = 'https://api.bilibili.com/pgc/season/index/result?st=1&year=%5B2019%2C2020)&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=3&sort=0&page=1&season_type=1&pagesize=20&type=1'
    json_data = get_json_content(url)
    total_nums = json_data['data']['total']
    pagesize = 20
    page = 1
    while pagesize*page < total_nums:
        url = each_url.format(int(page),int(pagesize))
        json_data = get_json_content(url)
        ani_list = json_data['data']['list']
        page += 1
        yield ani_list
    else:
        pagesize = total_nums % 20
        page = math.ceil(total_nums/20)
        url = each_url.format(int(page),int(pagesize))
        json_data = get_json_content(url)
        ani_list = json_data['data']['list']
        page += 1
        yield ani_list

# 插入数据库
def watch_data_save():
    double_list = list(get_anime_list(watch_url))
    for anime_list in double_list:
        collection_watch_nums.insert_many(anime_list)
        print('插入成功')


def play_data_save():
    double_list = list(get_anime_list(play_url))
    for anime_list in double_list:
        collection_play_nums.insert_many(anime_list)
        print('插入成功')



def grade_data_save():
    double_list = list(get_anime_list(grade_url))
    for anime_list in double_list:
        collection_grade.insert_many(anime_list)
        print('插入成功')


if __name__ == '__main__':
    # watch_data_save()
    # play_data_save()
    grade_data_save()



