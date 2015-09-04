from scrapy import Item, Field


class Form(Item):
    url = Field()
    name = Field()
    title = Field()
    category = Field()
    language = Field()
    last_modified = Field()
    download_url = Field()
    download_size = Field()
    download_format = Field()


class Leaflet(Form):
    associated_form_names = Field()
