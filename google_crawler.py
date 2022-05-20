# # Crawl Google's search engine for images
from icrawler.builtin import GoogleImageCrawler
from time import sleep
import os

# keyword = input("Enter a keyword: ")
# num_images = int(input("Enter the number of images: "))

def google_crawler(keyword, num_images):
    while True:
        try:
            # create a GoogleImageCrawler instance with our keyword
            google_crawler = GoogleImageCrawler(
                feeder_threads=1,
                parser_threads=1,
                downloader_threads=4,
                storage={'root_dir': 'download'}
            )
            filters = dict(
                size='large',
                color='orange',
                license='commercial,modify',
                date=((2017, 1, 1), (2017, 11, 30)))
            # start the crawler with our keyword and number of images
            google_crawler.crawl(
                keyword=str(keyword)
                , max_num=int(num_images)
                , filters=filters
                , offset=0, file_idx_offset=0
                , min_size=(256, 256))
            # break out of the loop
            break
        except Exception as e:
            print(e)
            print("Error: Retrying...")
            sleep(5)
            continue
    # google_crawler = GoogleImageCrawler(storage={'root_dir': 'download'})
    # google_crawler.crawl(keyword=str(keyword), max_num=int(num_images))







