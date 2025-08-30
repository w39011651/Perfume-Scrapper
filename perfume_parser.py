from bs4 import BeautifulSoup
import requests
import json

ALL_PERFUME_URL = "https://www.fincataiwan.com/categories/%E9%A6%99%E6%B0%B4?limit=72"


def get_product_name_and_price(bs:BeautifulSoup):
    product_dict = {}
    all_products_tag = bs.select("div.Product-info")
    for product in all_products_tag:
        product_name = product.select_one("div.Product-title").text
        price = product.select_one("div.Label-price.sl-price").text
        if price == 'NT$1,180':
            product_dict[product_name] = {"price":price, "url": None}
    return product_dict

def get_product_and_url(bs: BeautifulSoup):
    all_link_tags = bs.find_all('a', class_ = 'Product-item')
    name_to_url = {}
    for tag in all_link_tags:
        ga_product_str = tag.get('ga-product')
        if ga_product_str:
            ga_product_data = json.loads(ga_product_str)
            product_title = ga_product_data["title"]
            product_href = tag.get('href')

            name_to_url[product_title] = product_href
    return name_to_url

def get_perfumes_url():
    response = requests.get(ALL_PERFUME_URL)
    bs = BeautifulSoup(response.text, 'lxml')

    product_dict = get_product_name_and_price(bs)
    url_dict = get_product_and_url(bs)
    
    for k,v in url_dict.items():
        if product_dict.get(k):
            product_dict[k]["url"] = v

    return product_dict


if __name__ == '__main__':
    response = requests.get(ALL_PERFUME_URL)
    bs = BeautifulSoup(response.text, 'lxml')

    product_dict = get_product_name_and_price(bs)
    url_dict = get_product_and_url(bs)
    for k,v in url_dict.items():
        if product_dict.get(k):
            product_dict[k]["url"] = v

    for k,v in product_dict.items():
        print(f'{k:<35}{v['price']:<10}{v['url']:<100}')
        

    
    
    
        
