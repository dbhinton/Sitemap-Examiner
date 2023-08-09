import sys
import requests
import bs4
import xmltodict
from flask import Flask, render_template, request
from functools import lru_cache
import concurrent.futures

app = Flask(__name__)

# Cache for recently extracted SKUs
@lru_cache(maxsize=None)
def extract_sku_from_url(url):
    """Extracts SKU from a given URL."""
    url_parts = url.split('/')
    sku = url_parts[-1]
    return sku

def extract_product_info(url):
    """
    Extracts product information (author, title, price) from HTML content.

    Args:
        url (str): The URL of the product page.

    Returns:
        dict: Dictionary containing product details or error messages.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    content = response.content

    soup = bs4.BeautifulSoup(content, 'html.parser')

    author_element = soup.find('a', class_='CBD-ProductDetailAuthorLink')
    author = author_element.get_text(strip=True) if author_element else 'Author not found'

    title_element = soup.find('h1', class_='CBD-ProductDetailTitle')
    title = title_element.get_text(strip=True) if title_element else 'Title not found'

    price_element = soup.find('div', class_='CBD-PreviewGroupItemTotalPrice')
    price = price_element.get_text(strip=True) if price_element else 'Price not found'

    product_info = {
        'title': title,
        'author': author,
        'price': price
    }

    return product_info

def search_parallel(sku):
    """
    Searches for product information in parallel using multiple threads.

    Args:
        sku (str): The SKU to search for.

    Returns:
        dict: Dictionary containing product details or error messages.
    """
    if not sku.strip():
        return {'error': 'Please provide a sku.'}

    url = 'https://www.christianbook.com/sitemap4.xml'
    response = requests.get(url)

    if response.status_code != 200:
        return {'error': 'Unable to fetch sitemap.'}

    parsed_xml = xmltodict.parse(response.content)

    urlset_dict = parsed_xml.get('urlset', {})
    url_list = urlset_dict.get('url', [])

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for url_info in url_list:
            loc = url_info.get('loc', '')
            product_sku = extract_sku_from_url(loc)
            if product_sku == sku:
                futures.append(executor.submit(extract_product_info, loc))
        
        for future in concurrent.futures.as_completed(futures):
            product_info = future.result()
            if 'error' not in product_info:
                return product_info
    
    return {'error': 'SKU not found.'}

@app.route('/', methods=['GET'])
def index():
    """Render the index.html template."""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_sku():
    """
    Handle SKU search form submission.

    Returns:
        HTML: Rendered index.html template with product information.
    """
    sku = request.form.get('sku')
    product_info = search_parallel(sku)
    return render_template('index.html', product_info=product_info)

if __name__ == '__main__':
    app.run(debug=True)
