from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """
    Represents a product in the e-commerce platform.

    Attributes:
        name (str): The name of the product.
        slug (str): A unique slug for the product.
        description (str): A detailed description of the product.
        ingredients (str, optional): Ingredients used in the product.
        manufacturer (str): The manufacturer of the product.
        price (Decimal): The price of the product.
        stock_quantity (int): The available stock quantity of the product.
        image (ImageField, optional): An image of the product.
        rating (int): The product's rating.
        category (Category): The category this product belongs to.
        tags (Tag): The tags this product belongs to.
        created_at (datetime): The date and time when the product was created.
        updated_at (datetime): The date and time when the product was last updated.
        is_active (bool): Indicates if the product is active.
    """

    name = models.CharField(verbose_name=_('product name'), max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name=_('product description'))
    manufacturer = models.CharField(verbose_name=_('product manufacturer'), max_length=100)
    ingredients = models.TextField(verbose_name=_('ingredients'), blank=True, null=True)
    price = models.DecimalField(verbose_name=_('product price'), max_digits=7, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(verbose_name=_('product stock quantity'), default=0)
    image = models.ImageField(verbose_name=_('product image'), upload_to='products/', null=True, blank=True)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=1
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_products')
    tags = models.ManyToManyField('Tag', blank=True, related_name='tag_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        """ Return the string representation of the product. """
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    """
    Represents a product category in the e-commerce platform.

    Attributes:
        name (str): The name of the category.
        slug (str): A unique slug for the category.
        description (str, optional): A description of the category.
        created_at (datetime): The date and time when the category was created.
        updated_at (datetime): The date and time when the category was last updated.
        is_active (bool): Indicates if the category is active.
    """

    name = models.CharField(verbose_name=_('category name'), max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name=_("category description"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ Return the string representation of the category. """
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """
    Represents a product tag in the e-commerce platform.

    Attributes:
        name (str): The name of the tag.
    """
    name = models.CharField(verbose_name=_('product tag name'), max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Tag')
        verbose_name_plural = _('Product Tags')
