# -*- encoding: UTF-8 -*-

# --------------------------------import-----------------------------------

import scrapy
from AudioDownload.items import AudiodownloadItem

# ----------------------------------class-----------------------------------

class AudioSpider(scrapy.Spider):
    name = "zhuixu"
    start_urls = ["http://www.audio699.com/book/805.html"]

    def parse(self, response):
        audiochapter_urls = response.xpath("/html/body/div/div/div/div/div[4]/div/ul//a/@href").extract()
        for audiochapter_url in audiochapter_urls:
            print(audiochapter_url)
            yield scrapy.Request(audiochapter_url, callback=self.parseAudioUrl, dont_filter=True)

    def parseAudioUrl(self, response):
        audio_name = response.xpath("/html/body/div/div/div/div/div[2]/h1/text()").extract()[0]
        audio_url = response.xpath("/html/body/div/div/div/div/div[2]/div[1]/audio/source/@src").extract()
        print(audio_url)
        print("--------------------------------------------------------")
        print(audio_name)
        #with open(audio_url, 'wb') as f:
            #f.write(audio_name)

