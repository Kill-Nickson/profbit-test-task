import random
from uuid import uuid4
import argparse

from django.core.management.base import BaseCommand

from products.models import Category, Product


class Command(BaseCommand):
    help = 'Refresh products fields'

    def handle(self, *args, **options):
        for product in Product.objects.all().iterator():
            product.status = random.choice(Product.STATUS_CHOICES)
            product.price = random.randrange(0, 1000)
            product.remains = random.randint(0, 100)
            product.save()
        self.stdout.write(self.style.SUCCESS(
            f'Products have been changed successfully!')
        )
