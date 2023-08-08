import sys
import requests
import bs4
import xmltodict

def extract_sku_from_url(url):
    url_parts = url.split('/')
    sku = url_parts[-1]
    return sku

def search(sku):
    if not sku.strip():
        return 'Please provide a sku.'

    url = 'https://www.christianbook.com/sitemap4.xml'
    response = requests.get(url)

    if response.status_code != 200:
        return 'Unable to fetch sitemap.'

    parsed_xml = xmltodict.parse(response.content)

    urlset_dict = parsed_xml.get('urlset', {})
    url_list = urlset_dict.get('url', [])

    for url_info in url_list:
        loc = url_info.get('loc', '')

        product_sku = extract_sku_from_url(loc)
        if product_sku == sku:
            print(loc)
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(loc, headers=headers)
            content = response.content

            soup = bs4.BeautifulSoup(content, 'html.parser')

            author_element = soup.find('a', class_='CBD-ProductDetailAuthorLink')
            if author_element:
                author = author_element.get_text(strip=True)
            else:
                author = 'Author not found'

            title_element = soup.find('h1', class_='CBD-ProductDetailTitle')
            if title_element:
                title = title_element.get_text(strip=True)
            else:
                title = 'Title not found'

            price_element = soup.find('div', class_='CBD-PreviewGroupItemTotalPrice')
            if price_element:
                price = price_element.get_text(strip=True)
            else:
                price = 'Price not found'

            product_info = {
                'title': title,
                'author': author,
                'price': price
            }

            return product_info

    return {'error': 'SKU not found.'}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please provide a SKU as an argument.')
        sys.exit(1)

    sku = sys.argv[1]
    print(f"Searching for SKU: {sku}")
    result = search(sku)
    print(f"Result: {result}")
