from django.db import models



class Category(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField(max_length=20000,blank=True,null=True)
    picture = models.ImageField(upload_to='Images',blank=True)
    color_picture = models.ImageField(upload_to='Images',blank=True)

    def __str__(self):
        return f'{self.type}'

    def get_category_image_url(self):
        return self.picture.url

    def get_category_color_image_url(self):
        return self.color_picture.url