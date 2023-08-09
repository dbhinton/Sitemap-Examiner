import requests
import bs4
import xmltodict
from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_sku():
    sku = request.form.get('sku')
    product_info = search(sku)
    return render_template('index.html', product_info=product_info)

if __name__ == '__main__':
    app.run(debug=True)
