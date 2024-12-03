import csv
from django.core.management.base import BaseCommand
from bonnes_lectures.models import Book

class Command(BaseCommand):
    help = "Import books from a CSV file"

    def handle(self, *args, **options):
        with open('bonnes_lectures/data/manga.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Book.objects.create(
                    title=row['title'],
                    publisher=row['publisher'],
                    year=row['year'],
                    isbn=row['isbn'],
                    backCover=row['back_cover']
                )
        self.stdout.write(self.style.SUCCESS('Données importées avec succès !'))
