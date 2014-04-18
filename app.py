import csv
from flask import Flask, render_template, send_from_directory, redirect, request


app = Flask(__name__)


@app.route("/")
def index():
    items = []
    with open('items.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        items = [row for row in reader]

    for item in items:
        item['id'] = int(item['id'])
    items = sorted(items, key=lambda i: i['id'])

    return render_template('list.html', items=items)


@app.route("/img/<image_id>")
def img(image_id=None):
    file_name = '{0!s}.jpg'.format(image_id)
    return send_from_directory('images/full/', file_name)


@app.route("/save", methods=['POST'])
def save():
    with open('items.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        items = [row for row in reader]

    with open('items.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, ['name', 'id', 'title', 'image',
                                          'keywords'])
        writer.writeheader()
        for item in items:
            item['name'] = request.form.get('name_{0!s}'.format(item['id']),
                                            '')
            writer.writerow(item)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
