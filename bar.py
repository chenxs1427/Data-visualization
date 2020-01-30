# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 1:41
# @Author  : -- CXS --
# @File    : data_visualization.py

from operate_database import fetch_data
from pyecharts import options
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode

anime_data_dict = fetch_data(10),

def bar(num=10):
    b = (
        Bar(
            init_opts = options.InitOpts(
                page_title='柱状图',
                animation_opts = options.AnimationOpts(
                    # animation_delay = 1000,
                    animation_easing = 'elasticOut'
                ),  # 初始化打开时的动画效果
                theme='light',  # 主题
                width='1500px',height='750px',  # 柱状图大小
                bg_color={
                    'type':'pattern',
                    'image': JsCode('img'),
                    'repeat':'no-repeat',
                }  # 设置背景图片，也可设置成背景颜色
            ),
        )
        .add_xaxis(anime_data_dict['title'])  # 添加x轴
        .add_yaxis('评分(10分制)',anime_data_dict['score'])
        .add_yaxis('播放量/千万次',[round(each/1000,2) for each in anime_data_dict['play_count']])
        .add_yaxis('追番人数/十万人',[round(each/10,2) for each in anime_data_dict['fav_count']])  # 添加多个y轴
        .reversal_axis()  # 翻转xy轴
        .set_global_opts(  # 全局配置(整张图的配置)
            title_opts=options.TitleOpts(
                title='B站2019年新番数据',
                subtitle='番名',
            ),  # 设置主标题和副标题
            datazoom_opts=options.DataZoomOpts(type_='inside'),  # 动态滑动效果
        )
        # .set_series_opts(
        #     markarea_opts=options.MarkPointOpts(
        #         data=[
        #             options.MarkPointItem(type_='max',name='最大值'),
        #             options.MarkPointItem(type_='min', name='最小值'),
        #             options.MarkPointItem(type_='average', name='平均值'),
        #         ]  # 局部配置(局部柱状图的配置)
        #     ),
        # )
        .add_js_funcs(
            """
            var img = new Image();
            img.src = '银古.jpg';
            """
            )  # 通过js传入背景图片
        .render('anime_bar.html')  # 生成html文件
    )
    return b

if __name__ == '__main__':
    bar()



