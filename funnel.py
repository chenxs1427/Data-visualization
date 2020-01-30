# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 14:58
# @Author  : -- CXS --
# @File    : funnel.py

from operate_database import fetch_data
from pyecharts import options as opts
from pyecharts.charts import Funnel

anime_data_dict = fetch_data(15)

def bing(num=15) -> Funnel:

    f = (
        Funnel(init_opts=opts.InitOpts(page_title='漏斗图',width='1300px',height='650px'))
        .add("新番", [list(z) for z in zip(anime_data_dict['title'],anime_data_dict['play_count'])],
            label_opts=opts.LabelOpts(position="inside"),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="播放量漏斗图"),legend_opts=opts.LegendOpts(
                                 type_="scroll", pos_right="4%",pos_top="10%", orient="vertical"))
        .render('funnel.html')
    )##滚动条
    return f

if __name__ == '__main__':
    bing(15)