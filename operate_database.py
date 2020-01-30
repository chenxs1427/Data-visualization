# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 23:08
# @Author  : -- CXS --
# @File    : operate_database.py

import pymongo
import re

client = pymongo.MongoClient(host = "127.0.0.1",port = 27017)
collection_watch_nums = client['anime']['watch_nums']
collection_play_nums = client['anime']['play_nums']
collection_grade = client['anime']['grade']
final_collection = client['anime']['2019_anime_data']

# 合并数据库
def merge_database():
    for collection in [collection_grade,collection_watch_nums,collection_play_nums]:
        result = collection.find({}, {'order': 1, 'order_type': 1, 'media_id': 1})
        for each_dict in list(result):
            media_id = each_dict['media_id']
            new_data = {each_dict['order_type']:each_dict['order']}
            final_collection.update({'media_id':media_id},{'$set':new_data})
            print('%d 更新成功'%media_id)

# 统一数据
def wash_data():
    result = final_collection.find({}, {'play_count': 1,'media_id':1,})
    for each_dict in result:
        media_id = each_dict['media_id']
        play_count = each_dict['play_count']
        if '亿' in play_count:
            play_num = re.search(r'\d+\.\d+',play_count).group(0)
            new_num = float(play_num) * 10000
            new_count = str(new_num) + '万次播放'
            final_collection.update_one({'media_id':media_id}, {'$set':{'play_count':new_count}})
            print('%d update successfully'%media_id)

# 转换为浮点数
def astype_float():
    result = final_collection.find({}, {'play_count': 1,'media_id':1,'fav_count': 1,'score':1,})
    for each_dict in result:
        media_id = each_dict['media_id']
        play_count = each_dict['play_count']
        fav_count = each_dict['fav_count']
        score = each_dict['score']
        if isinstance(fav_count, str):
            play_num = float(re.search(r'(\d+\.\d+|\d+)',play_count).group(0))
            fav_num = float(re.search(r'(\d+\.\d+|\d+)',fav_count).group(0))
            score_num = float(re.search(r'(\d+\.\d+|\d+)',score).group(0))
            final_collection.update_one({'media_id':media_id},
                                        {'$set':{'play_count':play_num,'fav_count':fav_num,'score':score_num,}})
            print('%d update successfully'%media_id)

# 删除一些极端数据
def delete_record():
    result = final_collection.find({})
    for each_dict in result:
        media_id = each_dict['media_id']
        fav_count = each_dict['fav_count']
        if isinstance(fav_count,str) and '万' not in fav_count:
            final_collection.delete_one({'media_id':media_id})
            print('delete successfully')

# 从数据库拉取数据
def fetch_data(num):
    result = final_collection.find({}, {'play_count': 1,'title':1,'fav_count': 1,'score':1,})\
        .sort([('play_count',-1)]).limit(num)
    play_list,fav_list,score_list,title_list = [],[],[],[]
    for each_dict in result:
        title_list.append(each_dict['title'])
        score_list.append(each_dict['score'])
        fav_list.append(each_dict['fav_count'])
        play_list.append(each_dict['play_count'])
    return {
        'title':title_list,
        'score':score_list,
        'fav_count':fav_list,
        'play_count':play_list,
    }

# if __name__ == '__main__':
    # merge_database()
    # wash_data()
    # astype_float()
    # delete_record()
    # result = fetch_data(10)





