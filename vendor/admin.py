from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from vendor.models import PriceHistory, Product, Page


class PriceHistoryInline(admin.TabularInline):
    model = PriceHistory
    extra = 0

    readonly_fields = ['date', 'price']

    fields = ('date', 'price')


class ProductAdmin(admin.ModelAdmin):
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
        (None, {'fields': ['sku', 'retailer']}),
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

    inlines = [PriceHistoryInline]

    list_display = ('sku', 'retailer', 'brand_name', 'category', 'product_name',
                    'retail_price', 'sale_price', 'availability', 'quantity_status')

    list_filter = ['retailer', 'availability']

    search_fields = ['retailer', 'sku', 'brand_name', 'category', 'product_name',
                     'retail_price', 'sale_price', 'availability', 'quantity']


class PageAdminForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.values('product_name'),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Products'),
            is_stacked=False,

        )
    )

    class Meta:
        model = Page
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['products'].initial = self.instance.products.all()

    def save(self, commit=True):
        page = super(PageAdminForm, self).save(commit=False)

        if commit:
            page.save()

        if page.pk:
            for product in self.cleaned_data['products']:
                page.products.add(product)

        return page


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm

    list_display = ('slug', 'title', 'product_num')

    search_fields = ['slug', 'title']


admin.site.register(Product, ProductAdmin)
admin.site.register(Page, PageAdmin)
