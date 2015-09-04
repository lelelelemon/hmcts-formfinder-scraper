import urlparse

from scrapy.spiders import Spider
from scrapy.http import FormRequest, Request

from ..items import Form, Leaflet

class HMCTSFormFinderSpider(Spider):
    name = "formfinder"
    allowed_domains = ["hmctsformfinder.justice.gov.uk"]
    base_url = 'http://hmctsformfinder.justice.gov.uk'
    start_url = "http://hmctsformfinder.justice.gov.uk/HMCTS/GetForms.do"

    def start_requests(self):
        return [
            FormRequest(
                self.start_url,
                formdata={
                    'court_forms_num': '',
                    'court_forms_title': c,
                    'court_forms_category': '',
                    'submit': 'Search'
                },
                method="POST",
                callback=self.get_document_pages
            )
            #for c in 'aeiou'
            for c in 'a'
        ]

    def get_document_pages(self, response):
        pages_path = ('//a[starts-with(@href, "GetForm.do?") '
                      'or starts-with(@href, "GetLeaflet.do?")]/@href')

        for page in response.xpath(pages_path).extract():
            url = urlparse.urljoin(response.url, page.strip())
            yield Request(url, callback=self.parse)

    def _get_details_item_text(self, details, i):
        return ''.join(details.xpath('dd[%d]/text()' % i).extract()).strip()

    def _get_download_format_and_size(self, details):
        return self._get_details_item_text(details, 5)[1:-1].split()

    def _get_download_url(self, details):
        return ''.join([
            self.base_url,
            details.xpath('dd[5]/a/@href').extract_first()
        ])

    def parse(self, response):
        section = response.xpath('//div[@id="Content"]/*/div[@class="formwrap"][1]')

        details = section.xpath('*/dl')
        dl_fmt, dl_size = self._get_download_format_and_size(details)

        kwargs = {
            'url': response.url,
            'name': section.xpath('h3/text()').extract_first().strip(),
            'title': self._get_details_item_text(details, 1),
            'category': self._get_details_item_text(details, 2),
            'language': self._get_details_item_text(details, 3),
            'last_modified': self._get_details_item_text(details, 4),
            'download_url': self._get_download_url(details),
            'download_size': dl_size,
            'download_format': dl_fmt,
        }

        if '_forms_' in response.url:
            yield Form(**kwargs)

        elif '_leaflets_' in response.url:
            forms_xpath = '//div[@id="Content"]/*/div[@class="formwrap"]/h3/text()'
            kwargs['associated_form_names'] = [n.strip() for n in
                response.xpath(forms_xpath)[1:].extract()]
            yield Leaflet(**kwargs)
