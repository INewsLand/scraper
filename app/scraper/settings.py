# -*- coding: utf-8 -*-

settings = {
    'BOT_NAME': 'scraper',
    'SPIDER_MODULES': ['scraper.spiders'],
    'NEWSPIDER_MODULE': 'scraper.spiders',
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ROBOTSTXT_OBEY': True,
    'CONCURRENT_REQUESTS': 16,
    'DOWNLOAD_DELAY': 3,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
    'CONCURRENT_REQUESTS_PER_IP': 16,
    'COOKIES_ENABLED': True,
    'ITEM_PIPELINES': {
        'scraper.pipelines.MongoPipeline': 100,
    },
}
