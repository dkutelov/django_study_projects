from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_image = models.ImageField(upload_to='blog/images/')
    post_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
