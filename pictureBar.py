# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 21:00
# @Author  : -- CXS --
# @File    : pictureBar.py

from operate_database import fetch_data
from pyecharts import options as opts
from pyecharts.charts import PictorialBar

anime_data_dict = fetch_data(15)

def pic(num=15) -> PictorialBar:

    p = (
        PictorialBar(init_opts=opts.InitOpts(page_title='象形柱状图',width='1600px',height='600px',bg_color='#7FFFAA'))
        .add_xaxis(anime_data_dict['title'])
        .add_yaxis(
            "10万人",
            [round(each/10,2) for each in anime_data_dict['fav_count']],
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=18,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],#偏移量
            is_symbol_clip=True,
            symbol='path://M29.902,23.275c1.86,0,3.368-1.506,3.368-3.365c0-1.859-1.508-3.365-3.368-3.365 c-1.857,0-3.365,1.506-3.365,3.365C26.537,21.769,28.045,23.275,29.902,23.275z M36.867,30.74c-1.666-0.467-3.799-1.6-4.732-4.199 c-0.932-2.6-3.131-2.998-4.797-2.998s-7.098,3.894-7.098,3.894c-1.133,1.001-2.1,6.502-0.967,6.769 c1.133,0.269,1.266-1.533,1.934-3.599c0.666-2.065,3.797-3.466,3.797-3.466s0.201,2.467-0.398,3.866 c-0.599,1.399-1.133,2.866-1.467,6.198s-1.6,3.665-3.799,6.266c-2.199,2.598-0.6,3.797,0.398,3.664 c1.002-0.133,5.865-5.598,6.398-6.998c0.533-1.397,0.668-3.732,0.668-3.732s0,0,2.199,1.867c2.199,1.865,2.332,4.6,2.998,7.73 s2.332,0.934,2.332-0.467c0-1.401,0.269-5.465-1-7.064c-1.265-1.6-3.73-3.465-3.73-5.265s1.199-3.732,1.199-3.732 c0.332,1.667,3.335,3.065,5.599,3.399C38.668,33.206,38.533,31.207,36.867,30.74z',
        )#这里是图像中小人的url路径
        .reversal_axis()#翻转
        .set_global_opts(
            datazoom_opts=opts.DataZoomOpts(type_="inside"),
            title_opts=opts.TitleOpts(title="追番人数",pos_top="4%",pos_left="5%"),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
        .render('pictorial_bar.html')
    )
    return p

if __name__ == '__main__':
    pic(15)
