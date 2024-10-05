from django.contrib import admin



# Register your models here.
from .models import User, Articles,View,Categories,ArticleView

# Register the custom User model
admin.site.register(User)
admin.site.register(ArticleView)
# Register the Article model
admin.site.register(Articles)
admin.site.register(View)
admin.site.register(Categories)
