# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 21:25
# @Author  : -- CXS --
# @File    : total_page.py

from pyecharts import options as opts
from pyecharts.charts import Page,Tab
from bar import bar
from line import grid
from rosetype_pie import pie_rosetype
from funnel import bing
from pictureBar import pic

# 同一页面中
# page = Page()
# page.add(bar(), grid(), pie_rosetype(),bing(),pic())
# page.render("one_page.html")

# 不同标签页中
# tab = Tab()
# tab.add(bar(), "bar-example")
# tab.add(grid(), "grid-example")
# tab.add(pie_rosetype(), "pie-example")
# tab.add(bing(), "bing-example")
# tab.add(pic(), "pic-example")
# tab.render("multi_tabs.html")


