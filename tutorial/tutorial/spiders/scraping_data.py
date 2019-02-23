import scrapy
import json


def getDomain(start_urls):
    full_url = start_urls
    full_url_list = full_url.split(".")
    domain_extensions = str(full_url_list[-1])
    domain_extensions_list = domain_extensions.split('/')
    domain_extension = domain_extensions_list[0]

    domain = full_url_list[-2] + "." + domain_extension

    if domain == "reuters.com":

        if 'in' in full_url_list[-3]:
            domain = 'in.reuters.com'

    return domain


test_data_set = ["Brazil", "Reliance Industries", "Bharti Airtel", "BlackRock", "Lodha Group", "IL&FS", "SBI",
                 "Reliance", "Brasil"]



urls = []
scraped_data = []

# crawled_links=[]

crawled_links = json.loads(open('stories2.json').read())

temp_body_list = []

count = 0
for link in crawled_links:
    urls.append(crawled_links[count]["link"])
    count = count + 1


class ScrapingSpider(scrapy.Spider):
    name = "data_scraper2"
    start_urls = urls

    def parse(self, response):
        resp = str(response)
        for test_data in test_data_set:

            titles = str(response.css(".ArticleHeader_headline::text").getall())
            bodies = str(response.css(".StandardArticleBody_body p::text").getall())
            titles2 = str(response.css("h1.clearfix.title::text").getall())
            bodies2 = str(response.css("div.Normal::text").getall())

            if getDomain(resp) == "reuters.com" or getDomain(resp) == "in.reuters.com":

                if test_data.lower() in titles.lower() or test_data.lower() in bodies.lower():

                    page_title = response.css(".ArticleHeader_headline::text").get()
                    a = {"link": str(response.request.url), "page_title": page_title,"text": bodies}
                    if a not in scraped_data:
                        scraped_data.append(a.copy())


            else:

                if test_data.lower() in titles2.lower() or test_data.lower() in bodies2.lower():
                    page_title = response.css(".clearfix h1 ::text").get()

                    a = {"link": str(response.request.url), "page_title": page_title, "text": bodies2}
                    if a not in scraped_data:
                      scraped_data.append(a.copy())

        f = open("stories_data.json", 'w')
        f.write(json.dumps(scraped_data))
        f.close

