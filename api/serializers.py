from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "eMail", "userName", "item_name","buy_date"]