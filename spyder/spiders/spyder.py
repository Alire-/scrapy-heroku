import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


#    allowed_domains = ['https://www.mywsba.org/LawyerDirectory/']
  #  start_urls = ['https://www.mywsba.org/LawyerDirectory/LawyerProfile.aspx?Usr_ID=1']



class FirstSpider(scrapy.Spider):
    name = "barSpider"
    
    
    
    def start_requests(self):
        crawl_limit = 100000
        y = 0 
        crawl_counter = 0
        for x in range(0, crawl_limit):
            y = y +1
            url = 'https://www.mywsba.org/LawyerDirectory/LawyerProfile.aspx?Usr_ID={0}'.format(y)
            yield scrapy.Request(url, self.parse)
                


    def parse(self, response):
        for lawyer in response.css('#content-left'):
            yield {
                'name': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblMemberName::text').extract_first(),
                'admitted': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblAdmitDate::text').extract_first(),
                'status': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblStatus::text').extract_first(),
                'addresss': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblAddress::text').extract_first(),
                'phone': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblPhone::text').extract_first(),
                'TDD:' : lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblTDD::text').extract_first(),
                'email' : lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblEmail::text').extract_first(),
                'website' : lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_hlWebsite::text').extract_first(),
                'practice areas': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblPracticeAreas::text').extract_first(),
                'private practice': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblPrivatePractice::text').extract_first(),
                'has insurance?': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblHasInsurance::text').extract_first(),
                'languages': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblLanguages::text').extract_first(),
                'memberships': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblCommittees::text').extract_first(),
                'discipline': lawyer.css('#dnn_ctr671_MyWSBA_LawyerProfile_lblNodiscipline::text').extract_first(),
}


