import scrapy
from json import loads
from re import search

class WebmotorsSpider(scrapy.Spider):
    name = 'webmotors'
    
    start_urls = ['https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros-novos%2Festoque%3Flkid%3D1001%2F&actualPage=1&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false']

    def parse(self, response):
        rsp = loads(response.body)
        search_results = rsp.get('SearchResults')
         
        for result in search_results:
            result["_id"] = result["UniqueId"]
            yield result

        if len(search_results) > 0:
            next_page_number = response.request.url
            next_page_number = search("(?<=actualPage=)[0-9]+(?=&display)", next_page_number)[0]
            next_page_number = int(next_page_number) + 1

            yield scrapy.Request(
                url=f'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros-novos%2Festoque%3Flkid%3D1001%2F&actualPage={next_page_number}&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false',
                callback=self.parse
            )