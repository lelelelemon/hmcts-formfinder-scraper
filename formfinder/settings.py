SPIDER_MODULES = ['formfinder.spiders']
NEWSPIDER_MODULE = 'formfinder.spiders'
DEFAULT_ITEM_CLASS = 'formfinder.items.Form'
#ITEM_PIPELINES = {'formfinder.'}
FEED_FORMAT = 'jsonlines'
FEED_URI = 'file://' + os.path.join(HERE, '../output.jsonl')
