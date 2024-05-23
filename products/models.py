from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name=_('parent'),
                               on_delete=models.CASCADE,
                               related_name='children')
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_('avatar'), blank=True, upload_to='categories/')
    is_active = models.BooleanField(verbose_name=_('active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_('avatar'), blank=True, upload_to='products/')
    category = models.ManyToManyField('Category', verbose_name=_('category'), blank=True)
    is_active = models.BooleanField(verbose_name=_('active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='files', on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file = models.FileField(verbose_name=_('file'), upload_to='files/%Y/%m/%d/')
    is_active = models.BooleanField(verbose_name=_('active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
