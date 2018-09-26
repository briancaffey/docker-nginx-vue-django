"""
Registers Post Models to Admin
"""

from django.contrib import admin
from . models import Post

admin.site.register(Post)
