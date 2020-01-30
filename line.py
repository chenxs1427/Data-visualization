# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 11:00
# @Author  : -- CXS --
# @File    : grid.py

from operate_database import fetch_data
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie,Grid,Line,Tab,Funnel,PictorialBar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker

anime_data_dict = fetch_data(18)

def judge_name(name):
    if len(name) > 6:
        return name[:6]
    else:
        return name

def grid(num=18):
    line1 = (
        Line()
            .add_xaxis(anime_data_dict['title'])
            .add_yaxis('评分',anime_data_dict['score'],
                       # yaxis_index=2,
                       color='#9370DB',
                       is_smooth=True,
                       is_hover_animation=True,
                       markline_opts=opts.MarkPointOpts(
                           data=[opts.MarkPointItem(type_='max'),
                                 opts.MarkPointItem(type_='min')]
                       )
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title='Line-基本示例'))
    )

    bar1 = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_easing='elasticOut'
                ),  # 柱状图弹出效果
                bg_color='#87CEEB',
                height='100px',
            ),
        )
        .add_xaxis(anime_data_dict['title'])
        .add_yaxis('播放量',[round(each/1000,2) for each in anime_data_dict['play_count']],yaxis_index=1,category_gap='80%')
        .add_yaxis('追番人数',[round(each/10,2) for each in anime_data_dict['fav_count']], yaxis_index=0, category_gap='80%')  # 设置轴的间隔
        .extend_axis(
            yaxis=opts.AxisOpts(
                name='评分',
                type_='value',
                position='right',
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='#d14a61')
                ),
                axislabel_opts=opts.LabelOpts(formatter='{value}'),
            )
        )  # 右侧y轴
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="播放量",
                type_="value",
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            ))

            .set_global_opts(
            title_opts=opts.TitleOpts(
                title='B站2019年新番数据可视化',
                subtitle=''
            ),
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
            yaxis_opts=opts.AxisOpts(
                name='追番人数',
                position='right',
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='#5793f3')
                ),
                axislabel_opts=opts.LabelOpts(formatter='{value}'),
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger='axis',
                axis_pointer_type='cross'
            ),
        )
        .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(0, 244, 255, 1)'
                            }, {
                                offset: 1,
                                color: 'rgba(0, 77, 167, 1)'
                            }], false)"""),
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": 'rgb(0, 160, 221)',
                }},  # 这里局部设置，绘制渐变圆柱形柱状
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                    opts.MarkPointItem(type_="average", name="平均值"),
                ]
            ),
        ))
    bar1.overlap(line1)
    # bar1.render('bar_line.html')
    # line1.render('line.html')
    grid = (
        Grid(init_opts=opts.InitOpts(page_title='折线图',width='1500px',height='500px'))
            .add(bar1, opts.GridOpts(pos_left="5%", pos_right="20%", pos_top="30%"), is_control_axis_index=True)
            .render('anime_line.html')
    )  # grid布局，将line添加进bar1里，并设置位置与大小
    return grid

if __name__ == '__main__':
    grid()
