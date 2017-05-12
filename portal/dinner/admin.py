# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Eating, Menu, FoodDay, CustomFood
#
admin.site.register(FoodDay)
admin.site.register(Menu)
admin.site.register(Eating)
admin.site.register(CustomFood)
