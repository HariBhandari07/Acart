from django.contrib import admin

from ecommerce.models import Category, Product, ProductHasImage, ProductReview, WishList, Cart




admin.site.register(Category)


class ProductHasImageInline(admin.TabularInline):
    model = ProductHasImage


class AdminProduct(admin.ModelAdmin):
    inlines = [ProductHasImageInline]


admin.site.register(Category)

admin.site.register(Product, AdminProduct)


admin.site.register(Product, AdminProduct)  # product sangai image pani upload garna milxa admin panal ma
# it merges Product and ProductHasImage in. ProductHas image is child of parent Product.Check django admin tabular inline
admin.site.register(ProductReview)

# admin.site.register(ProductHasImage)

admin.site.register(WishList)

admin.site.register(Cart)
