from django.db import models
from .validators import validate_blocked_words
from base.models import BasePublishModel
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class ProductModel(BasePublishModel):
    
    title = models.TextField()
    price = models.FloatField()
    description = models.TextField(null=True)
    seller = models.TextField(null=True)
    color = models.TextField(null=True)
    product_dimensions = models.TextField(null=True)
    slug = models.SlugField(null=True, blank=True, db_index=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return f"/product/{self.slug}"
    

    def save(self, *args, **kwargs):
        validate_blocked_words(self.title)
        super().save(*args, **kwargs)

def slugify_pre_save(sender, instance, *arg, **kwargs):
        if instance.slug is None or instance.slug == "":
            new_slug = slugify(instance.title)
            MyModel = instance.__class__
            qs = MyModel.objects.filter(slug__startswith=new_slug).exclude(id=instance.id)
            if qs.count() == 0:
                instance.slug = new_slug
            else:
                instance.slug = f"{new_slug}-{qs.count()+1}"    

        
pre_save.connect(slugify_pre_save, sender=ProductModel)