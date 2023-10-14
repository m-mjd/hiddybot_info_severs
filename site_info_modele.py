import requests
from bs4 import BeautifulSoup


def extract_info_box(info_box):
    if info_box:
        title = info_box.find('span', class_='info-box-text').text.strip()
        number = info_box.find('span', class_='info-box-number').text.strip()
        progress = info_box.find('div', class_='progress-bar')['style']
        description = info_box.find(
            'span', class_='progress-description').text.strip()
        return title, number, progress, description
    return None, None, None, None


def get_info_boxes(soup):
    return {
        'today': extract_info_box(soup.find(id='today')),
        'yesterday': extract_info_box(soup.find(id='yesterday')),
        'monthly': extract_info_box(soup.find(id='last_30_days')),
        'total': extract_info_box(soup.find(id='total')),
        'network': extract_info_box(soup.find(id='network')),
        'cpu': extract_info_box(soup.find(id='cpu')),
        'ram': extract_info_box(soup.find(id='ram')),
        'disk': extract_info_box(soup.find(id='disk')),
        'online_users': extract_info_box(soup.find(id='online')),
    }


def scrape_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        info_boxes = get_info_boxes(soup)

        return {
            'today': info_boxes.get('today', (None, None, None, None)),
            'yesterday': info_boxes.get('yesterday', (None, None, None, None)),
            'monthly': info_boxes.get('monthly', (None, None, None, None)),
            'total': info_boxes.get('total', (None, None, None, None)),
            'network': info_boxes.get('network', (None, None, None, None)),
            'cpu': info_boxes.get('cpu', (None, None, None, None)),
            'ram': info_boxes.get('ram', (None, None, None, None)),
            'disk': info_boxes.get('disk', (None, None, None, None)),
            'online_users': info_boxes.get('online_users', (None, None, None, None)),
        }

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

