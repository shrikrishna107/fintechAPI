from django.db import models

class BlogPost(models.Model):
    eMail = models.CharField(max_length = 100)
    userName = models.CharField(max_length=100)
    item_name = models.CharField(max_length = 100)
    buy_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.eMail
