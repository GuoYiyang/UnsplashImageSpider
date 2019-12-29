# -*- coding: utf-8 -*-
import scrapy
import json
from UnsplashImageSpider.items import ImagespiderItem


class UnsplashImageSpider(scrapy.Spider):
    name = 'unsplash_image'
    allowed_domains = ['unsplash.com']
    start_urls = ['https://unsplash.com/napi/photos?page=1&per_page=12']

    def __init__(self):
        self.page_index=1

    def parse(self, response):
        photo_list=json.loads(response.text)
        for photo in photo_list:
            item=ImagespiderItem()
            item['image_id']=photo['id']
            item['download']=photo['links']['download']
            yield item
        self.page_index+=1
        next_link='https://unsplash.com/napi/photos?page=' + str(self.page_index) + '&per_page=12'
        yield scrapy.Resquest(next_link,callback=self.parse)
