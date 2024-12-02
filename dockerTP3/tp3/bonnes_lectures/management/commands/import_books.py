import csv
from django.core.management.base import BaseCommand
from bonnes_lectures.models import Book

class Command(BaseCommand):
    help = 'Import books from a custom CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='|')
            for row in reader:
                book, created = Book.objects.get_or_create(
                    title=row['Titre'],
                    publisher=row['Maison d\'édition'],
                    year=int(row['Publication']),
                    isbn=row['ISBN'],
                    backCover=row['Résumé'],
                    cover=True  # Si vous voulez gérer cette colonne, ajoutez-la dans le CSV
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Book '{book.title}' added."))
                else:
                    self.stdout.write(f"Book '{book.title}' already exists.")
