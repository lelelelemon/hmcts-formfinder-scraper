import os

HERE = os.path.dirname(os.path.realpath(__file__))

SPIDER_MODULES = ['formfinder.spiders']
NEWSPIDER_MODULE = 'formfinder.spiders'
DEFAULT_ITEM_CLASS = 'formfinder.items.Form'
ITEM_PIPELINES = {
    'formfinder.pipelines.FormDownloadPipeline': 0,
}

FEED_FORMAT = 'jsonlines'
FEED_URI = 'file://' + os.path.join(HERE, '../output.jsonl')
