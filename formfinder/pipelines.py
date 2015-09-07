import os
import requests

from scrapy.exceptions import DropItem

from .items import Form


class FormDownloadPipeline(object):
    def __init__(self):
        self.output_dir = './forms'

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def process_item(self, item, spider):
        url = item.get('download_url')

        if url:
            filename = url.split('/')[-1]
            req = requests.get(url, stream=True)

            with open(os.path.join(self.output_dir, filename), 'wb') as f:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()

        return item

