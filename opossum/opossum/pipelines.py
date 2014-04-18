# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

from .items import ExportImageItem


class OpossumPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('/home/moorcock/work/mrs_opossum/items.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ['id', 'title', 'image', 'keywords']
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        item_exp = ExportImageItem(
            id=item['id'],
            title=item['title'].strip(' \t\n'),
            image=item['images'][0]['path'].split('/')[-1].split('.')[0],
            keywords=item['keywords']
        )
        self.exporter.export_item(item_exp)
        return item_exp
