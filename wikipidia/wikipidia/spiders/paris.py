import scrapy


class ParisSpider(scrapy.Spider):
    name = "paris"
    start_urls = ["https://en.wikipedia.org/wiki/Eiffel_Tower"]

    def parse(self, response):
        raw_image_url = response.css('.image img ::attr(src)').getall()
        cleane_img_urls = []
        for img_url in raw_image_url:
            cleane_img_urls.append(response.urljoin(img_url))
            
        yield{
            'image_urls': cleane_img_urls
        }
