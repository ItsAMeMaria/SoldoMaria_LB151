from django.contrib import admin

# Register your models here.

from .models import Player, Word, Category

admin.site.register(Player)
admin.site.register(Word)
admin.site.register(Category)