from django.core.management.base import BaseCommand

from feed.models import AeroPrecision, Brownells, DanielDefense, EuroOptic, Gear1800, Guns, Palmetto, PrimaryArms, SportsmansGuide
from vendor.models import Product, Page

import os

from library import debug

debug = debug.debug

FILEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Command(BaseCommand):
    help = 'Build Product Database'

    def add_arguments(self, parser):
        parser.add_argument('functions', nargs='+', type=str)

    def handle(self, *args, **options):
        if "product" in options['functions']:
            self.aero()
            self.brownells()
            self.daniel()
            self.euro()
            self.gear1800()
            self.guns()
            self.palmetto()
            self.primaryarms()
            self.sportsmans()

    def aero(self):
        rows = AeroPrecision.objects.all()
        self.update(rows, "AeroPrecision")

    def brownells(self):
        rows = Brownells.objects.all()
        self.update(rows, "Brownells")

    def daniel(self):
        rows = DanielDefense.objects.all()
        self.update(rows, "DanielDefense")

    def euro(self):
        rows = EuroOptic.objects.all()
        self.update(rows, "EuroOptic")

    def gear1800(self):
        rows = Gear1800.objects.all()
        self.update(rows, "Gear1800")

    def guns(self):
        rows = Guns.objects.all()
        self.update(rows, "Guns")

    def palmetto(self):
        rows = Palmetto.objects.all()
        self.update(rows, "Palmetto")

    def primaryarms(self):
        rows = PrimaryArms.objects.all()
        self.update(rows, "PrimaryArms")

    def sportsmans(self):
        rows = SportsmansGuide.objects.all()
        self.update(rows, "SportsmansGuide")

    def update(self, rows, retailer):
        debug("Product", 0, "Start Processing {} Products".format(retailer))

        for row in rows:
            try:
                product = Product.objects.get(
                    sku=row.sku,
                )
            except Product.DoesNotExist:
                product = Product.objects.create(
                    sku=row.sku,
                )

            product.retailer = retailer

            product.manufacturer_id = row.manufacturer_id
            product.brand_name = row.brand_name
            if row.product_name == "" or row.product_name == None:
                continue
            product.product_name = row.product_name

            product.long_description = row.long_description
            product.short_description = row.short_description
            product.category = row.category
            product.sub_category = row.sub_category
            product.product_group = row.product_group
            product.thumb_url = row.thumb_url
            product.image_url = row.image_url
            product.buy_link = row.buy_link
            product.keywords = row.keywords
            product.reviews = row.reviews
            try:
                product.retail_price = float(row.retail_price)
            except:
                pass
            try:
                product.sale_price = float(row.sale_price)
            except:
                pass
            product.brand_page_link = row.brand_page_link
            product.brand_logo_image = row.brand_logo_image
            product.tracking = row.tracking
            product.parent_group = row.parent_group
            product.color = row.color
            product.size = row.size
            product.pattern = row.pattern
            product.material = row.material
            try:
                product.weight = float(row.weight)
            except:
                pass
            product.age_group = row.age_group
            product.gender = row.gender
            product.upc = row.upc
            product.gtin = row.gtin
            product.guid = row.guid

            product.sale_price_effective_date = row.sale_price_effective_date
            if row.availability == "False":
                product.availability = False
            if row.visibility == "False":
                product.visibility = False

            product.model_number = row.model_number
            try:
                if row.quantity == '':
                    product.quantity = -1
                else:
                    product.quantity = int(row.quantity)
            except:
                pass
            product.alternative_buy_link = row.alternative_buy_link
            product.alternative_product_id = row.alternative_product_id
            product.alternative_image_id = row.alternative_image_id
            product.medium_image_url = row.medium_image_url
            product.content_widget = row.content_widget

            product.google_categorization = row.google_categorization
            try:
                product.commission = float(row.commission)
            except:
                pass

            try:
                product.save()
            except Exception as e:
                print(e)
                continue

            PAGE_LEVEL = 5
            productTags = product.product_name.split(" ")

            if len(productTags) < PAGE_LEVEL:
                pageTitle = product.product_name

                page = Page(slug=self.get_slug(pageTitle))
                page.title = self.get_title(pageTitle)

                page.save()
                product.pages.add(page)

            else:
                for ii in range(0, len(productTags) - PAGE_LEVEL):
                    pageTitle = " ".join([productTags[jj]
                                          for jj in range(ii, ii + PAGE_LEVEL - 1)])

                    page = Page(slug=self.get_slug(pageTitle))
                    page.title = self.get_title(pageTitle)

                    page.save()
                    product.pages.add(page)

            product.pricehistory_set.create(
                price=row.sale_price
            )

            print("Product {} has been saved successfully".format(product.sku))

        debug("Product", 0, "Completed Processing {} Products".format(retailer))

    def get_slug(self, str):
        slug = str.translate(
            {ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+'\""})
        slug = slug.replace("  ", " ").replace(
            "  ", "").replace(" ", "-").replace("--", "-").lower()
        if slug[-1] == "-":
            slug = slug[:-1]

        return slug

    def get_title(self, str):
        title = str
        if str[-1] in "!@#$%^&*()[]{};:,./<>?\|`~-=_+'\"":
            title = str[:-1]
        title = title.strip()

        return title
