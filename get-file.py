import csv


def run():
    with open('items.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        items = [row for row in reader if row['name']]

    for item in items:
        item['name'] = int(item['name'])
    items = sorted(items, key=lambda i: i['name'])

    with open('result.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, ['name', 'title', 'description',
                                          'keywords'])
        for item in items:
            new_item = {
                'name': '{0!s}.eps'.format(item['name']),
                'title': item['title'],
                'description': item['title'],
                'keywords': item['keywords'],
            }
            writer.writerow(new_item)

if __name__ == "__main__":
    run()
