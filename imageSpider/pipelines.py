# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.request import *


class ImagespiderPipeline(object):
    def process_item(self, item, spider):
        # 每个item代表一个要下载的图片
        print('----------' + item['image_id'])
        real_url = item['download'] + "?force=true"
        try:
            pass
            # 打开URL对应的资源
            with urlopen(real_url) as result:
                # 读取图片数据
                data = result.read()
                # 打开图片文件
                with open("images/" + item['image_id'] + '.jpg', 'wb+') as f:
                    # 写入读取的数据
                    f.write(data)
        except:
            print('下载图片出现错误' + item['image_id'])
