# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.utils.project import get_project_settings

class DouyuspiderPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        img_url = item["img_url"]
        yield scrapy.Request(img_url)


    def item_completed(self, results, item, info):
        print('result:',results)
        print('result:', item)
        success = results[0][0]
        print(success)
        if success:
            img_path = results[0][1]['path']
            img_path = self.IMAGES_STORE + "/" + img_path
            dest_name = self.IMAGES_STORE + "/" + item['name'] + '.jpg'
            os.rename(img_path,dest_name)
            item['img_path'] = dest_name
        return item
