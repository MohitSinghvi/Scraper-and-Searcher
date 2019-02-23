import scrapy
import json
from ..items import TutorialItem

link_list=[]
def getDomain(start_urls):
    full_url = start_urls
    full_url_list = full_url.split(".")
    domain_extensions =str(full_url_list[-1])
    domain_extensions_list=domain_extensions.split('/')
    domain_extension = domain_extensions_list[0]


    domain = full_url_list[-2]+"."+domain_extension



    if domain == "reuters.com":

        if 'in' in full_url_list[-3]:

            domain='in.reuters.com'


    return domain

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://in.reuters.com/search/news?blob=swisscom',
        'https://www.reuters.com/news/archive/bondsNews',
        'https://economictimes.indiatimes.com/markets/bonds',
        'https://in.reuters.com/search/news?blob=bharti+airtel',
        'https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=2146846&curpg=3&img=1',
        'https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=2146846&curpg=2&img=1',


    ]
    surl=start_urls
    def parse(self, response):

        items=TutorialItem()
        #story_title_list=[]

        resp=str(response)
        domain=getDomain(resp)
        print("<<<<<<<<<DOMAIN>>>>>>>>>"+domain)
        if(domain=='reuters.com'):
            all_stories=response.css(".news-headline-list .story")

            for story in all_stories:

                link=story.css(".story-content a").xpath("@href")[0].extract()
                items['link']=response.urljoin(link)
                temp={"link":str(response.urljoin(items['link']))}
                link_list.append(temp.copy())
                yield items


        elif(getDomain(resp)=='in.reuters.com'):
            all_stories = response.css(".search-result-content h3")
            for story in all_stories:
                link = story.css("a").xpath("@href")[0].extract()
                items['link'] = response.urljoin(link)

                temp = {"link": str(response.urljoin(items['link']))}
                link_list.append(temp.copy())
                yield items

        else:
            all_stories = response.css("body div.eachStory")

            for story in all_stories:

                link = story.css("a").xpath("@href").get()

                items['link'] = response.urljoin(link)
                temp = {"link": str(response.urljoin(items['link']))}
                link_list.append(temp.copy())
                yield items
        f=open("stories2.json",'w')
        f.write(str(link_list).replace("'",'"'))
        f.close()


        #
        # print("\n\n")
        # print("\n\n")
        # print("\n\n")
        # print("\n\n")
        # print(link_list)
        # print("\n\n")
        # print("\n\n")
        # print("\n\n")
        # print("\n\n")




