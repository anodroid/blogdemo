from django.db import models
# from mdeditor.fields import MDTextField 
from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # content = MDTextField()
    content = RichTextUploadingField()
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    modify_date = models.DateField(auto_now=True, verbose_name='修改日期')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    created_date = models.DateField(auto_now_add=True, verbose_name='创建日期')
    summary = models.CharField(max_length=200, verbose_name='概要')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Visit(models.Model):
    visit_date = models.DateField(auto_now_add=True, verbose_name='访问日期')
    count = models.IntegerField(default=0, verbose_name='日访问量')
    
    class Meta:
        verbose_name = '日访问量'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return str(self.day)

    def sum_over(self):
        return 