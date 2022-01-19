from django.contrib import admin

from .models import AeroPrecision, Brownells, DanielDefense, EuroOptic, Gear1800, Guns, Palmetto, PrimaryArms, SportsmansGuide


class AeroPrecisionAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class BrownellsAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class DanielDefenseAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class EuroOpticAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class Gear1800Admin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class GunsAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class PalmettoAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class PrimaryArmsAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class SportsmansGuideAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['sku']}),
        ('Collection', {'fields': ['manufacturer_id',
         'brand_name', 'category', 'sub_category']}),
        ('Content', {'fields': [
         'product_name', 'long_description', 'short_description']}),
        ('Images', {'fields': ['thumb_url', 'image_url', 'medium_image_url']}),
        ('Checkout', {'fields': ['buy_link', 'alternative_buy_link']}),
        ('Tagging', {'fields': ['keywords', 'reviews']}),
        ('Pricing', {'fields': ['retail_price',
         'sale_price', 'shipping_cost']}),
        ('Branding', {'fields': ['brand_page_link', 'brand_logo_image']}),
        ('Detail', {'fields': ['color', 'size', 'pattern', 'material',
         'weight', 'age_group', 'gender', 'upc', 'gtin', 'guid']}),
        ('Availability', {'fields': [
         'availability', 'sale_price_effective_date', 'visibility', 'quantity', 'condition', 'shipping_status']}),
        ('Additional Information', {'fields': [
         'tracking', 'product_group', 'parent_group', 'model_number', 'content_widget', 'alternative_product_id', 'alternative_image_id', 'google_categorization', 'commission']}),
    ]

    list_display = ('sku', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity')

    list_filter = ['brand_name', 'category', 'availability']

    search_fields = ['sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


admin.site.register(AeroPrecision, AeroPrecisionAdmin)
admin.site.register(Brownells, BrownellsAdmin)
admin.site.register(EuroOptic, EuroOpticAdmin)
admin.site.register(DanielDefense, DanielDefenseAdmin)
admin.site.register(Gear1800, Gear1800Admin)
admin.site.register(Guns, GunsAdmin)
admin.site.register(Palmetto, PalmettoAdmin)
admin.site.register(PrimaryArms, PrimaryArmsAdmin)
admin.site.register(SportsmansGuide, SportsmansGuideAdmin)
