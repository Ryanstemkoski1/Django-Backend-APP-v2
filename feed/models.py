from django.db import models


class AeroPrecision(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Brownells(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class DanielDefense(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class EuroOptic(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Gear1800(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Guns(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Palmetto(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class PrimaryArms(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class SportsmansGuide(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)

    manufacturer_id = models.CharField(max_length=200, default=None, null=True)
    brand_name = models.CharField(max_length=200, default=None, null=True)
    category = models.CharField(max_length=200, default=None, null=True)
    sub_category = models.CharField(max_length=200, default=None, null=True)

    product_name = models.CharField(max_length=200, default=None, null=True)
    long_description = models.TextField(
        max_length=2000, default=None, null=True)
    short_description = models.TextField(
        max_length=500, default=None, null=True)

    thumb_url = models.URLField(default=None, null=True)
    image_url = models.URLField(default=None, null=True)
    medium_image_url = models.URLField(default=None, null=True)

    buy_link = models.URLField(default=None, null=True)
    alternative_buy_link = models.URLField(default=None, null=True)

    keywords = models.TextField(max_length=2000, default=None, null=True)
    reviews = models.TextField(max_length=2000, default=None, null=True)

    retail_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    brand_page_link = models.URLField(max_length=1000, default=None, null=True)
    brand_logo_image = models.URLField(default=None, null=True)

    color = models.CharField(max_length=200, default=None, null=True)
    size = models.CharField(max_length=200, default=None, null=True)
    pattern = models.CharField(max_length=200, default=None, null=True)
    material = models.CharField(max_length=200, default=None, null=True)
    weight = models.FloatField(default=1)
    age_group = models.CharField(max_length=200, default=None, null=True)
    gender = models.CharField(max_length=200, default=None, null=True)
    upc = models.CharField(max_length=200, default=None, null=True)
    gtin = models.CharField(max_length=200, default=None, null=True)
    guid = models.CharField(max_length=200, default=None, null=True)

    sale_price_effective_date = models.CharField(
        max_length=200, default=None, null=True)
    availability = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, default=None, null=True)
    shipping_status = models.CharField(
        max_length=200, default=None, null=True)

    tracking = models.TextField(max_length=200, default=None, null=True)
    product_group = models.CharField(max_length=200, default=None, null=True)
    parent_group = models.CharField(max_length=200, default=None, null=True)
    model_number = models.CharField(max_length=200, default=None, null=True)
    content_widget = models.TextField(max_length=1000, default=None, null=True)
    alternative_product_id = models.CharField(
        max_length=200, default=None, null=True)
    alternative_image_id = models.CharField(
        max_length=200, default=None, null=True)

    google_categorization = models.CharField(
        max_length=200, default=None, null=True)
    commission = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
