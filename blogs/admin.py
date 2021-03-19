from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) #จะมี model blog และ post ขึ้น จะเป็นการบันทึกข้อมูลโดย admin
