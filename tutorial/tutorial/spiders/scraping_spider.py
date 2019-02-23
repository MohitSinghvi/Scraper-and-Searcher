import scrapy
import json



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


test_data_set=["Brazil","Reliance Industries","Bharti Airtel","BlackRock","Lodha Group","IL&FS","SBI","Reliance","Brasil"]

brazil=[]
reliance_industries=[]
bharti_airtel=[]
black_rock=[]
lodha_group=[]
ilfs=[]
sbi=[]

urls=[]
scraped_data=[]


#crawled_links=[]

crawled_links=json.loads(open('stories2.json').read())


temp_body_list=[]

count=0
for link in crawled_links:

    urls.append(crawled_links[count]["link"])
    count = count + 1

class ScrapingSpider(scrapy.Spider):
    name="data_scraper"
    start_urls = urls

    #     [
    #     'https://in.reuters.com/search/news?blob=swisscom',
    #     'https://www.reuters.com/news/archive/bondsNews',
    #     'https://economictimes.indiatimes.com/markets/bonds',
    #     'https://in.reuters.com/search/news?blob=bharti+airtel',
    #     'https://in.reuters.com/article/telkomkenya-m-a-bharti-airtel/bharti-airtel-in-talks-to-buy-telkom-kenya-sources-idINKCN1P80NO',
    # ]
    #global test_data_set
    def parse(self, response):
        resp=str(response)
        for test_data in test_data_set:

            titles=str(response.css(".ArticleHeader_headline::text").extract())
            bodies=str(response.css(".StandardArticleBody_body p::text").extract())
            titles2=str(response.css("h1.clearfix.title::text").extract())
            bodies2=str(response.css("div.Normal::text").extract())


            if getDomain(resp)=="reuters.com" or getDomain(resp)=="in.reuters.com":

                if test_data in titles or test_data in bodies :

                    page_title=response.css(".ArticleHeader_headline::text").get()

                    if(test_data.lower()=="brazil" or test_data.lower()=="brasil"):
                        allpara=response.css(".StandardArticleBody_body p::text").extract()
                        for para in allpara:
                            if "Brasil" in para or "Brazil" in para:
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in brazil:
                                    brazil.append(a.copy())
                                # if a not in scraped_data:
                                #     scraped_data.append(a.copy())


                    elif(test_data.lower()=="reliance industries" or test_data.lower()=="reliance" ):
                        allpara = response.css(".StandardArticleBody_body p::text").extract()
                        for para in allpara:
                            if "reliance" in para.lower() :
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in reliance_industries:
                                    reliance_industries.append(a.copy())


                        #reliance_industries.append(str(response.request.url))

                    elif(test_data.lower()=="bharti airtel"):
                        allpara = response.css(".StandardArticleBody_body p::text").extract()
                        for para in allpara:
                            if "bharti airtel" in para.lower() :
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in bharti_airtel:
                                    bharti_airtel.append(a.copy())


                        #bharti_airtel.append(str(response.request.url))
                    elif(test_data.lower()=="blackrock"):
                        allpara = response.css(".StandardArticleBody_body p::text").extract()
                        for para in allpara:
                            if "blackrock" in para.lower() :
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in black_rock:
                                    black_rock.append(a.copy())


                    elif(test_data.lower()=="lodha group"):
                        allpara = response.css(".StandardArticleBody_body p::text").extract()
                        for para in allpara:
                            if "lodha group" in para.lower():
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in lodha_group:
                                    lodha_group.append(a.copy())

                    elif(test_data.lower()=="il&fs"):
                        allpara = response.css(".StandardArticleBody_body p::text").extract()
                        for para in allpara:
                            if "il&fs" in para.lower():
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in ilfs:
                                    ilfs.append(a.copy())


                    elif (test_data.lower() == "sbi"):
                        allpara = response.css(".StandardArticleBody_body p::text").extract()
                        for para in allpara:
                            if "sbi" in para.lower():
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in sbi:
                                    sbi.append(a.copy())

            else:


                if test_data in titles2 or test_data in bodies2:
                    page_title=response.css(".clearfix h1 ::text").get()









                    if (test_data.lower() == "brazil" or test_data.lower() == "brasil"):
                        allpara = response.css("div.Normal::text").extract()
                        for para in allpara:
                            if "Brasil" in para or "Brazil" in para:
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in brazil:
                                    brazil.append(a.copy())

                    elif (test_data.lower() == "reliance industries" or test_data.lower() == "reliance"):
                        allpara = response.css("div.Normal::text").extract()
                        for para in allpara:
                            if "reliance" in para.lower():
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in reliance_industries:
                                    reliance_industries.append(a.copy())

                        # reliance_industries.append(str(response.request.url))

                    elif (test_data.lower() == "bharti airtel"):
                        allpara = response.css("div.Normal::text").extract()
                        for para in allpara:
                            if "bharti airtel" in para.lower():
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in bharti_airtel:
                                    bharti_airtel.append(a.copy())

                        # bharti_airtel.append(str(response.request.url))
                    elif (test_data.lower() == "blackrock"):
                        allpara = response.css("div.Normal::text").extract()
                        for para in allpara:
                            if "blackrock" in para.lower():
                                a = {"link": str(response.request.url), "para": para, "page_title": page_title}
                                if a not in black_rock:
                                    black_rock.append(a.copy())


                    elif (test_data.lower() == "lodha group"):
                        print("<<<<<<<<<<oye hoye>>>>>>>>>>>>>>")
                        allpara = response.css("div.Normal ::text").extract()
                        for para in allpara:
                            if "lodha group" in para.lower():
                                a = {"link": str(response.request.url), "para": para,"page_title":page_title}
                                if a not in lodha_group:
                                    lodha_group.append(a.copy())

                    elif (test_data.lower() == "il&fs"):
                        allpara = response.css("div.Normal::text").extract()
                        for para in allpara:
                            if "il&fs" in para.lower():
                                a = {"link": str(response.request.url), "para": para,"page_title":page_title}
                                if a not in ilfs:
                                    ilfs.append(a.copy())


                    elif (test_data.lower() == "sbi"):
                        allpara = response.css("div.Normal::text").extract()
                        for para in allpara:
                            if "sbi" in para.lower():
                                a = {"link": str(response.request.url), "para": para,"page_title":page_title}
                                if a not in sbi:
                                    sbi.append(a.copy())

        f = open("stories_data.json", 'w')
        f.write('{"brazil":'+json.dumps(brazil)+',"reliance_industries":'+json.dumps(reliance_industries)+',"black_rock":'+json.dumps(black_rock)+',"lodha_group":'+json.dumps(lodha_group)+',"ilfs":'+json.dumps(ilfs)+',"sbi":'+json.dumps(sbi)+'}')
        f.close()






        print("\nBRAZIL : \n",brazil,"\nreliance_industries\n",reliance_industries,"\nbharti_airtel\n",bharti_airtel,"\nblack_rock\n",black_rock,"\nlodha_group\n",lodha_group,"\nSBI\n",sbi,"\nilfs\n",ilfs)


        #print("\nBRAZIL : \n",brazil)