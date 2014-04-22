import csv
from PIL import Image
from PIL.ExifTags import TAGS


def run():
    with open('items.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

    for row in reader:
        img = Image.open('/home/moorcock/jpegs/{0}'
                         '.jpg'.format(row['name']))


if __name__ == "__main__":
    run()
