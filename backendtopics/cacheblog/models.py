from django.db import models

class Blog(models.Model):
    author = models.CharField(blank=False, null=False)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
