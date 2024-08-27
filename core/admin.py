from store.models import Product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
<<<<<<< HEAD
from store.admin import ProductAdmin, ProductImageInline
=======
from store.admin import ProductAdmin
>>>>>>> 0034254 (all added)
from tags.models import TaggedItem
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
<<<<<<< HEAD
    inlines = [TagInline, ProductImageInline]
=======
    inlines = [TagInline]
>>>>>>> 0034254 (all added)


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
