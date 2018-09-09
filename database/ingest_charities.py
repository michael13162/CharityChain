import requests
import sqlite3

def query(page_size, page_num):
    base_url = 'https://api.data.charitynavigator.org/v2'
    params = {
        'app_id': '36f7e58b',
        'app_key': '5b7e63cbf53729f850317094a8e79575',
        'rated': 'TRUE',
        'pageSize': page_size,
        'pageNum': page_num
    }
    print(params)
    r = requests.get(base_url + '/Organizations', params=params)
    if r.status_code != 200:
        print('ERROR')
        
    return r.json()

def insert_db(db, query):
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    cur.close()


page_size = 1000
page_num = 1

results = []

while True:
    new_results = query(page_size, page_num)
    results.extend(new_results)

    print(str(len(results)) + ' ', end='', flush=True)

    if len(new_results) != page_size:
        break

    page_num += 1

db = sqlite3.connect('database.db')

for result in results:
    if 'ein' in result and result['ein'] is not None:
        ein = result['ein']
    else:
        ein = 'NOT FOUND'

    if 'tagLine' in result and result['tagLine'] is not None:
        tag_line = result['tagLine']
    else:
        tag_line = 'NOT FOUND'

    if 'charityName' in result and result['charityName'] is not None:
        charity_name = result['charityName']
    else:
        charity_name = 'NOT FOUND'

    if 'currentRating' in result and result['currentRating']['rating'] is not None:
        rating = str(result['currentRating']['rating'])
    else:
        rating = '0'

    print(ein + " " + tag_line + " " + charity_name + " " + rating)

    query = 'INSERT INTO charity(ein, tag_line, charity_name, rating) values(\'%s\', \'%s\', \'%s\', \'%s\')' % (
        ein.replace('\'', '\'\''),
        tag_line.replace('\'', '\'\''),
        charity_name.replace('\'', '\'\''),
        rating.replace('\'', '\'\'')
    )

    insert_db(db, query)

