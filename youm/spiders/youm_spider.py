import scrapy

'''

important notes for usage of the spider:
the spider takes two arguments: the category you want to crawl
and the label you want to give
and the number of pages you want crawled

example:

scrapy crawl youm -o data.json -a label=0 -a pages=20 -a category=علوم-و-تكنولوجيا/328/
scrapy crawl youm -o data.json -a label=1 -a pages=20 -a category=فن/48/
scrapy crawl youm -o data.json -a label=2 -a pages=20 -a category=سياسة/319/
scrapy crawl youm -o data.json -a label=3 -a pages=20 -a category=أخبار-الرياضة/298/
scrapy crawl youm -o data.json -a label=4 -a pages=20 -a category=اقتصاد-وبورصة/297/
scrapy crawl youm -o data.json -a label=5 -a pages=20 -a category=صحة-وطب/245/





also u can use the percentage encodings like so:
scrapy crawl youm -o data.json -a label=1 -a pages=3 -a category=%D9%81%D9%86/48/


the command has to be written in the same directory where the scrapy.cfg file is
also, invoke the de corrupt script to get valid json:
python3 de_corrupt.py

'''


class YoumSpider(scrapy.Spider):
    
    name = 'youm'
    def __init__(self, label='',pages=10,category='', *args, **kwargs):
        super(YoumSpider, self).__init__(*args, **kwargs)
        self.category=category
        self.label=label
        self.pages=int(pages)
        self.start_urls = []
        url_template='https://www.youm7.com/Section/'+self.category
    
    #scraping the first n pages of articles for that category
        for i in range(1,self.pages+1):
            self.start_urls.append(url_template+str(i))

    def parse(self, response):
        for href in response.css('#paging h3 a::attr(href)'):
            yield response.follow(href, self.parse_article)

    def parse_article(self, response):
        article=' '.join((response.css('#articleBody p::text')).extract())
        article_clean=''.join(e for e in article if (e.isalnum() or e==' '))
        title=response.css('h1::text').extract()[0]
        yield {
            'article':article_clean,
            'link':response.request.url,
            'category':self.category.split('/')[0].replace('-',' '),
            'label':self.label,
            'title':title
        }