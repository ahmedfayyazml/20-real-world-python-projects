import  requests
import selectorlib

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL  = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """SCRAPE THE PAGE SOURCE FROM URL"""
    response = requests.get(url,headers=HEADERS)
    source = response.text
    return  source
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value



if  __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    save_text(extracted)
    print(extracted)
