from django.contrib import admin
from .models import *


class portfolioImageInline(admin.StackedInline):
    model = PortfolioGallery

class portfolioAdmin(admin.ModelAdmin):
    inlines = [portfolioImageInline]

admin.site.register(Portfolio, portfolioAdmin)
admin.site.register(Post)
admin.site.register(Services)