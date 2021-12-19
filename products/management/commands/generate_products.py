import random
from uuid import uuid4
import argparse

from django.core.management.base import BaseCommand

from products.models import Category, Product


class Command(BaseCommand):
    help = 'Generates product nomenclature'

    @staticmethod
    def check_positive_int(value):
        i_value = int(value)
        if i_value <= 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive int value")
        return i_value

    def add_arguments(self, parser):
        parser.add_argument('categories_amount', type=self.check_positive_int)
        parser.add_argument('products_amount', type=self.check_positive_int)

    def handle(self, *args, **options):
        if options.get('categories_amount') > 0:
            categories = [Category(name=f"category{uuid4()}") for _ in range(options.get('categories_amount'))]
            Category.objects.bulk_create(categories)

            if options.get('products_amount') > 0:
                products = []
                for category in [Category.objects.get(name=c.name) for c in categories]:
                    for _ in range(options.get('products_amount')):
                        products.append(Product(name=f"product{uuid4()}",
                                                category=category,
                                                price=random.randrange(0, 1000),
                                                remains=random.randint(0, 100)))
                Product.objects.bulk_create(products)

            self.stdout.write(self.style.SUCCESS(f'Objects have been created successfully!'))