# web-scraping

## Install required modules:
`pip install .`   

## Usage
`import page_parser`   
Create page object and load an html page   
`page = page_parser.Page()`   
`page.load(url)`   
Create parsing schema, e.g   
`parsing_schema = {   
    "App's name":   
        "//tr[@class='app-info__row'][position()=1]/td[position()=2]",   
    "App's version":   
        "//tr[@class='app-info__row'][position()=4]/td[position()=2]",   
    "Number of downloads":   
        "//tr[@class='app-info__row'][position()=3]/td[position()=2]",   
    "Release date":   
        "//tr[@class='app-info__row'][position()=5]/td[position()=2]",   
    "App's description":   
        "//p[@itemprop='description']"   
}`   
Create parser and use Page.parse_page methot with schema and parser   
`parser = page_parser.xPathParser()`   
`page.parse_page(parser, parsing_schema)`   
Method Page.get_parsed_page() returns parsed page according to schema   
`page.get_parsed_page()`   

## Run server
`python server.py`   
Go to http://127.0.0.1:8080/
