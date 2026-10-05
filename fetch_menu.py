# Pulls the live FriesLab dine-in menu into menu-data.js
# Run again any time prices/items change on frieslab.net:  python fetch_menu.py
import re, json, urllib.request

req = urllib.request.Request('https://www.frieslab.net/menu/dine_in?category=Wings',
                             headers={'User-Agent': 'Mozilla/5.0'})
h = urllib.request.urlopen(req).read().decode('utf-8')
chunks = re.findall(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)', h)
s = ''.join(json.loads('"' + m + '"') for m in chunks)


def grab(key):
    k = s.index('"%s":' % key) + len(key) + 3
    return json.JSONDecoder().raw_decode(s[k:])[0]


cats = sorted(grab('initialCategories'), key=lambda c: c['priority'])
items = list(grab('initialMenuItems').values())
out = {'categories': [], 'items': []}
used = set()
for it in items:
    variants = it.get('menu_variants') or []
    v = next((v for v in variants if v['menu_type'] == 'DINE_IN'), variants[0] if variants else None)
    if not v:
        continue
    used.add(v['category_id'])
    out['items'].append({
        'id': it['id'],
        'cat': v['category_id'],
        'name': it['name'].strip(),
        'price': v['offer_price'] if v['offer_price'] is not None else v['price'],
        'desc': ' '.join((it.get('ingredients') or '').split()),
        'img': 'https://www.frieslab.net/images/menu-images/' + it['image'] if it.get('image') else '',
        'hot': bool(it.get('is_chilli')),
        'best': bool(it.get('is_bestseller')),
        'isNew': bool(it.get('new_item')),
    })
out['categories'] = [{'id': c['id'], 'name': c['name'].strip()} for c in cats if c['id'] in used]

with open('menu-data.js', 'w', encoding='utf-8') as f:
    f.write('window.MENU = ' + json.dumps(out, ensure_ascii=False, indent=1) + ';\n')
print(len(out['categories']), 'categories,', len(out['items']), 'items')
