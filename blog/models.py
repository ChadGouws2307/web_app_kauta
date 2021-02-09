from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    summary = models.TextField(default='', max_length=200)
    intro = models.TextField(default='', blank=True)
    head_1 = models.TextField(default='', blank=True)
    body_1 = models.TextField(default='', blank=True)
    head_2 = models.TextField(default='', blank=True)
    body_2 = models.TextField(default='', blank=True)
    head_3 = models.TextField(default='', blank=True)
    body_3 = models.TextField(default='', blank=True)
    head_4 = models.TextField(default='', blank=True)
    body_4 = models.TextField(default='', blank=True)
    head_5 = models.TextField(default='', blank=True)
    body_5 = models.TextField(default='', blank=True)
    conclusion_head = models.TextField(default='', blank=True)
    conclusion = models.TextField(default='', blank=True)
    image = models.ImageField(default='kalai_logo_1.png', upload_to='images', blank=True, null=True)
    image_1 = models.ImageField(default='', upload_to='images', blank=True, null=True)
    image_2 = models.ImageField(default='', upload_to='images', blank=True, null=True)
    image_3 = models.ImageField(default='', upload_to='images', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
