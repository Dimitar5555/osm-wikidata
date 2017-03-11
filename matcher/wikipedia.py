import requests
from .utils import chunk, drop_start

page_size = 50

def get_cats(titles):
    query_url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'format': 'json',
        'formatversion': 2,
        'action': 'query',
        'continue': '',
        'prop': 'categories',
        'titles': '|'.join(titles),
        'cllimit': 'max',
        'clshow': '!hidden',
    }
    r = requests.get(query_url, params=params)
    json_reply = r.json()
    return json_reply['query']['pages']

def get_items_with_cats(items):
    assert isinstance(items, dict)
    for cur in chunk(items.keys(), page_size):
        for page in get_cats(cur):
            if 'categories' not in page:  # redirects
                continue
            cats = [drop_start(cat['title'], 'Category:')
                    for cat in page['categories']]
            items[page['title']]['cats'] = cats
