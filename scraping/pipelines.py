# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from datetime import datetime, timezone

class ScrapingPipeline(object):
    def __init__(self, MONGO_URI, MONGO_DB, MONGO_DATA_RAW_COLLECTION):
        self.MONGO_URI = MONGO_URI
        self.MONGO_DB = MONGO_DB
        self.MONGO_DATA_RAW_COLLECTION = MONGO_DATA_RAW_COLLECTION

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            MONGO_URI=crawler.settings.get('MONGO_URI'),
            MONGO_DB=crawler.settings.get('MONGO_DATABASE'),
            MONGO_DATA_RAW_COLLECTION=crawler.settings.get('MONGO_DATA_RAW_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.MONGO_URI)
        self.db = self.client[self.MONGO_DB]
        self.nome_template = spider.colecao if hasattr(spider, 'colecao') else spider.name
        self.client.close()

    def process_item(self, item, spider):
        item['timestamp'] = datetime.now(timezone.utc).isoformat()
        item['spider_name'] = self.nome_template
        item['status'] = 0
        self.db[self.MONGO_DATA_RAW_COLLECTION].insert_one(dict(item))
        return item
