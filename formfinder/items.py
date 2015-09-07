from scrapy import Item, Field


class Form(Item):
    type = Field()
    url = Field()
    name = Field()
    title = Field()
    category = Field()
    language = Field()
    last_modified = Field()
    download_url = Field()
    download_size = Field()
    download_format = Field()
    associated_form_names = Field()
