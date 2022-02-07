from django.contrib import admin
from .models import Node, Transaction, Blockchain
# Register your models here.

admin.site.register(Node)
admin.site.register(Transaction)
admin.site.register(Blockchain)