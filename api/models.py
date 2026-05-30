from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=255)
    article = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)

    description = models.TextField(blank=True)
    material = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=100, blank=True)

    in_stock = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    delivery_time = models.CharField(max_length=255, blank=True)

    branding_available = models.BooleanField(default=False)
    branding_types = models.JSONField(default=list, blank=True)

    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField(blank=True)

    company_name = models.CharField(max_length=255, blank=True)
    inn = models.CharField(max_length=20, blank=True)
    company_card = models.FileField(upload_to='company_cards/', null=True, blank=True)

    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заявка #{self.id} — {self.full_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    color = models.CharField(max_length=100, blank=True)
    branding_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Обратная связь — {self.name}'