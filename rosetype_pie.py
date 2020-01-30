# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 14:24
# @Author  : -- CXS --
# @File    : rosetype_pie.py

from operate_database import fetch_data
from pyecharts import options as opts
from pyecharts.charts import Pie

anime_data_dict = fetch_data(30)

def pie_rosetype(num=30) -> Pie:
    # 玫瑰饼图
    pie = (
        Pie(init_opts=opts.InitOpts(page_title='饼图',width="1300px", height="650px"))#设置图例大小
        .add(
             "",
            [list(z) for z in zip(anime_data_dict['title'], anime_data_dict['fav_count'])],
            radius=[100, 120],
            center=["35%", "50%"],
            rosetype="radius",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="追番人数占比", subtitle="",pos_top="10%",pos_left="30%"),
                         # datazoom_opts=opts.DataZoomOpts(type_='inside'),
                        legend_opts=opts.LegendOpts(
                                 type_="scroll", pos_right="4%",pos_top="10%", orient="vertical")
                         )#设置滚动条
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"),)#设置图示
        .render('anime_pie.html')
    )
    return pie

if __name__ == '__main__':
    pie_rosetype(30)