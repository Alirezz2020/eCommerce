from django.db import models
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE,related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        db_table = 'category'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug,])


class Product(models.Model):
        category = models.ManyToManyField(Category, related_name='products')
        name = models.CharField(max_length=100)
        slug = models.SlugField(max_length=100, unique=True)
        image = models.ImageField(upload_to='products/%Y/%m/%d')
        description = models.TextField()
        price = models.DecimalField(max_digits=5, decimal_places=2)
        available = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['name',]
            verbose_name_plural = 'Products'
            verbose_name = 'Product'
            db_table = 'product'


        def __str__(self):
                return self.name

        def get_absolute_url(self):
            return reverse('home:product-detail', args=[self.slug,])





