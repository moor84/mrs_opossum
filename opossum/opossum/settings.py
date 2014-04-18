# Scrapy settings for opossum project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'opossum'

SPIDER_MODULES = ['opossum.spiders']
NEWSPIDER_MODULE = 'opossum.spiders'

# EXPORT_FIELDS = ['id', 'title', 'keywords', 'images']

ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
    'opossum.pipelines.OpossumPipeline': 2
}

IMAGES_STORE = '/home/moorcock/work/mrs_opossum/images/'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'opossum (+http://www.yourdomain.com)'
