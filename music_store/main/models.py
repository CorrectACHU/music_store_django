from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория товара')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название товара')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class EarphonesProduct(Product):
    type = models.CharField(max_length=50, verbose_name='Тип')
    construction = models.CharField(max_length=50, verbose_name='Конструкция')
    wireless = models.BooleanField(default=False)
    frequency = models.CharField(max_length=100, verbose_name='Частотный дипозон')
    sensitivities = models.CharField(max_length=60, verbose_name='Чувствительность')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class SpeakersProduct(Product):
    TYPE_SPEAKERS = [
        ('BT', 'Bluetooth - колонка'),
        ('SMART', 'Умная колонка'),
        ('USUAL', 'Проводная колонка')
    ]

    type = models.CharField(max_length=50, verbose_name='Тип', choices=TYPE_SPEAKERS)
    RMS = models.CharField(max_length=60, verbose_name='Мощность')
    frequency = models.CharField(max_length=100, verbose_name='Частотный дипозон')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_product')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена', default=0)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель : {} {}".format(self.user.first_name, self.user.last_name)

