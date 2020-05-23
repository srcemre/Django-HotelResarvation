from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.forms import ModelForm, TextInput, Select, FileInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


TYPE = (
    ('menu', 'menu'),
    ('blog', 'blog'),
    ('agent', 'agent'),
    ('duyuru', 'duyuru'),
    ('etkinlik', 'etkinlik'),
)
STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
)


class Content(models.Model):
    menu = models.OneToOneField(Menu, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=10, choices=TYPE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    thumbnail = models.ImageField(blank=True, upload_to='images/content/', default='images/null.jpg')
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="45" height="37"/>'.format(self.thumbnail.url))

    image_tag.short_descripton = 'Image'

    def get_absolute_url(self):
        return reverse('content_detail', kwargs={'slug': self.slug})


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['type', 'title', 'slug', 'keywords', 'description', 'thumbnail', 'detail']
        widgets = {
            'title': TextInput(attrs={'class': 'table', 'placeholder': 'title'}),
            'slug': TextInput(attrs={'class': 'table', 'placeholder': 'slug'}),
            'keywords': TextInput(attrs={'class': 'table', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'table', 'placeholder': 'description'}),
            'type': Select(attrs={'class': 'table', 'placeholder': 'type'}, choices=TYPE),
            'thumbnail': FileInput(attrs={'class': 'table', 'placeholder': 'thumbnail'}),
            'detail': CKEditorWidget(),
        }


class CImages(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/content/images')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="45" height="37"/>'.format(self.image.url))

    image_tag.short_descripton = 'Image'


class ContentImageForm(ModelForm):
    class Meta:
        model = CImages
        fields = ['title', 'image']
