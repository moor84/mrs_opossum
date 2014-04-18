import csv
from flask import Flask, render_template, send_from_directory, redirect


app = Flask(__name__)


@app.route("/")
def index():
    items = []
    with open('items.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        items = [row for row in reader]

    return render_template('list.html', items=items)


@app.route("/img/<image_id>")
def img(image_id=None):
    file_name = '{0!s}.jpg'.format(image_id)
    return send_from_directory('images/full/', file_name)


@app.route("/save")
def save():
    # TODO
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
