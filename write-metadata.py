import csv
from PIL import Image
from PIL.ExifTags import TAGS


def run():
    with open('items.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        items = [row for row in reader]



if __name__ == "__main__":
    run()
