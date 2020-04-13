from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title       = models.CharField(max_length=30) #charfield = uzunluk
    keywords    = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thumbnail   = models.ImageField(blank=True, upload_to='images', default='images/null.jpg')
    status      = models.CharField(max_length=10, choices=STATUS)
    slug        = models.SlugField()
    parent      = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        #level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" width="45" height="37"/>'.format(self.thumbnail.url))
    image_tag.short_descripton = 'Image'

class Accommodation(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    STAR = (
        ('0', '-'),
        ('1', '(1) *'),
        ('2', '(2) **'),
        ('3', '(3) ***'),
        ('4', '(4) ****'),
        ('5', '(5) *****'),
    )
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    title       = models.CharField(max_length=100) #charfield = uzunluk
    keywords    = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thumbnail   = models.ImageField(blank=True, upload_to='images', default='images/null.jpg')
    star        = models.CharField(max_length=1, blank=True, choices=STAR)
    address     = models.TextField(max_length=150)
    email       = models.CharField(max_length=30)
    phone       = models.PositiveSmallIntegerField()
    fax         = models.PositiveSmallIntegerField(blank=True,null=True)
    city        = models.CharField(max_length=30) #TODO: City için bir veri tabanı hazırlanacak.
    detail      = RichTextUploadingField(blank=True)
    status      = models.CharField(max_length=10, choices=STATUS)
    slug        = models.SlugField()
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="85"/>'.format(self.thumbnail.url))
    image_tag.short_descripton = 'Image'

class Room(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    hotel       = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    title       = models.CharField(max_length=150)  # charfield = uzunluk
    keywords    = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thumbnail   = models.ImageField(blank=True, upload_to='images/rooms', default='images/null.jpg')
    price       = models.FloatField()
    amount      = models.IntegerField()
    person      = models.PositiveSmallIntegerField()
    bed         = models.PositiveSmallIntegerField()
    detail      = RichTextUploadingField(blank=True)
    status      = models.CharField(max_length=10, choices=STATUS)
    slug        = models.SlugField()
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="85"/>'.format(self.thumbnail.url))
    image_tag.short_descripton = 'Image'

class Image(models.Model):
    hotel = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images', default='images/null.jpg')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url:
            return mark_safe('<img src="{}" height="85"/>'.format(self.image.url))
    image_tag.short_descripton = 'Image'

