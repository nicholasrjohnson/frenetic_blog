from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('Published Date', default=timezone.now)
    edited_date = models.DateTimeField('Edited Date', default=timezone.now)
    slug = models.SlugField(max_length=500)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='posts'
    )

    def save(self, *args, **kwargs):
        print(self.title)
        if not self.id:
            print("slugifying")
            self.slug = slugify(self.pub_date.strftime(
                "%a-%d-%b-%Y-%H%M%S-") + self.title)
        print(self.slug)
        print("just printed slug")
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post',
                       self.id,
                       args=[self.slug])

    def __str__(self):
        return self.title
