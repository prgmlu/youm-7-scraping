# youm-7-scraping

A very practical web-spider to collect the news from <a href="https://www.youm7.com">youm7</a> news website.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine if you're running Ubuntu.
Although other systems would be similar, i developed and tested it on Ubuntu 16.

### Prerequisites

You only need python3 and Scrapy.
```
pip3 install Scrapy
```
If you faced any problems, please refer to Scrapy <a href= "https://doc.scrapy.org/en/latest/intro/install.html">documentation</a>

### Running the Spider

After installing Scrapy, and cloning the repository, cd inside the directory where scrapy.cfg is:

```
git clone https://github.com/prgmlu/youm-7-scraping
cd youm-7-scraping
```
Now you can give the Spider a command like the following:

```
scrapy crawl youm -o data.json -a label=0 -a pages=3 -a category=علوم-و-تكنولوجيا/328/
```
In the command above:
* data.json is the outputted file where the scraped data will be saved
* label=0 is the label you want the news from that category be given, in that case we gave it label 0
* pages=3 is how many pages you want to scrap, in that case we will scrap 3 pages
* category have to be the identifying part of the url from the youm7 sections.

More examples:

```
scrapy crawl youm -o data.json -a label=1 -a pages=3 -a category=فن/48/
scrapy crawl youm -o data.json -a label=2 -a pages=3 -a category=سياسة/319/
scrapy crawl youm -o data.json -a label=3 -a pages=3 -a category=أخبار-الرياضة/298/
scrapy crawl youm -o data.json -a label=0 -a pages=3 -a category=علوم-و-تكنولوجيا/328/
```


## Fixing the JSON file

An important note, after scraping the above categories as shown, if the output is all concatenated to the same output file, for example "data.json", the file will not be valid json format, to fix this run the de_corrupt.py after you're done collecting the data:

```
python3 de_corrupt.py
```


## Authors

* **Mostafa Mahmoud**  
