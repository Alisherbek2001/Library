from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Book(models.Model):
    WRAPPER_STATUS = (
        ('yumshoq','Yumshoq'),
        ('qattiq','Qattiq')
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    category = models.ManyToManyField(Category)
    date = models.DateField(default='2024-05-21')
    price = models.IntegerField()
    discount = models.IntegerField(null=True,blank=True)
    wrapper = models.CharField(choices=WRAPPER_STATUS,max_length=255,default='Yumshoq')
    page_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    book = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'