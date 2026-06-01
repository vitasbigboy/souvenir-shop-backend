from django.core.management.base import BaseCommand
from api.models import Category, Product, Order, OrderItem, Feedback


class Command(BaseCommand):
    help = "Seed demo products"

    def handle(self, *args, **kwargs):
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        Feedback.objects.all().delete()
        Product.objects.all().delete()
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_product'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_category'")

        Category.objects.all().delete()

        categories_data = [
            ("Канцелярия", "stationery"),
            ("Подарочные наборы", "gift-sets"),
            ("Посуда", "dishes"),
            ("Письменные принадлежности", "writing"),
            ("Сезонные товары", "seasonal"),
        ]

        categories = {}

        for name, slug in categories_data:
            categories[name] = Category.objects.create(name=name, slug=slug)

        products_data = [
            {
                "category": "Канцелярия",
                "name": "Премиум набор блокнотов",
                "article": "GS-NB-001",
                "price": 2500,
                "image": "https://images.unsplash.com/photo-1510922903530-28ecf3f00362?w=800",
                "description": "Элегантный набор блокнотов в кожаном переплете, идеально подходит для корпоративных подарков.",
                "material": "Премиум кожа",
                "color": "Черный",
                "in_stock": True,
                "stock_quantity": 150,
                "delivery_time": "3-5 рабочих дней",
                "branding_available": True,
                "branding_types": ["Печать", "Тиснение"],
                "is_popular": True,
            },
            {
                "category": "Подарочные наборы",
                "name": "Подарочный набор руководителя",
                "article": "GS-GB-002",
                "price": 5500,
                "image": "https://images.unsplash.com/photo-1544377208-215a63786183?w=800",
                "description": "Роскошный подарочный набор с премиальными офисными аксессуарами.",
                "material": "Премиальные материалы",
                "color": "Черный",
                "in_stock": True,
                "stock_quantity": 45,
                "delivery_time": "5-7 рабочих дней",
                "branding_available": True,
                "branding_types": ["Печать", "Шелкография"],
                "is_popular": True,
            },
            {
                "category": "Посуда",
                "name": "Премиум кружка",
                "article": "GS-MG-003",
                "price": 1200,
                "image": "https://images.unsplash.com/photo-1618381801643-3d253a63a386?w=800",
                "description": "Высококачественная керамическая кружка с премиальной отделкой.",
                "material": "Премиум керамика",
                "color": "Белый",
                "in_stock": True,
                "stock_quantity": 320,
                "delivery_time": "2-4 рабочих дня",
                "branding_available": True,
                "branding_types": ["Печать", "Шелкография"],
                "is_popular": True,
            },
            {
                "category": "Письменные принадлежности",
                "name": "Набор ручек люкс",
                "article": "GS-PN-004",
                "price": 3500,
                "image": "https://images.unsplash.com/photo-1650735311937-1876825e971b?w=800",
                "description": "Премиальный набор письменных принадлежностей в элегантной подарочной коробке.",
                "material": "Металл с премиальной отделкой",
                "color": "Серебристый",
                "in_stock": False,
                "stock_quantity": 0,
                "delivery_time": "10-14 рабочих дней",
                "branding_available": True,
                "branding_types": ["Гравировка"],
                "is_popular": False,
            },
            {
                "category": "Подарочные наборы",
                "name": "Корпоративный подарочный пакет",
                "article": "GS-PK-005",
                "price": 7500,
                "image": "https://images.unsplash.com/photo-1694481901573-a970f982ac5e?w=800",
                "description": "Полный корпоративный подарочный пакет с премиальным набором офисных аксессуаров.",
                "material": "Высококачественные материалы",
                "color": "Черный",
                "in_stock": True,
                "stock_quantity": 28,
                "delivery_time": "7-10 рабочих дней",
                "branding_available": True,
                "branding_types": ["Печать", "Шелкография", "Тиснение"],
                "is_popular": True,
            },
            {
                "category": "Сезонные товары",
                "name": "Новогодний подарочный набор",
                "article": "GS-NY-006",
                "price": 4200,
                "image": "https://images.unsplash.com/photo-1697717657359-46433ee8497c?w=800",
                "description": "Специальный новогодний корпоративный подарочный набор.",
                "material": "Премиальная подборка",
                "color": "Красный",
                "in_stock": True,
                "stock_quantity": 85,
                "delivery_time": "3-5 рабочих дней",
                "branding_available": True,
                "branding_types": ["Печать", "Шелкография"],
                "is_popular": True,
            },
            {
                "category": "Подарочные наборы",
                "name": "Бизнес-набор аксессуаров",
                "article": "GS-AK-007",
                "price": 3800,
                "image": "https://images.unsplash.com/photo-1546313960-15422d64201a?w=800",
                "description": "Полный набор бизнес-аксессуаров с элегантным дизайном.",
                "material": "Премиальные материалы",
                "color": "Черный",
                "in_stock": True,
                "stock_quantity": 62,
                "delivery_time": "4-6 рабочих дней",
                "branding_available": True,
                "branding_types": ["Печать", "Тиснение"],
                "is_popular": True,
            },
            {
                "category": "Канцелярия",
                "name": "Стартовый офисный набор",
                "article": "GS-SP-008",
                "price": 2800,
                "image": "https://images.unsplash.com/photo-1582993467771-54d2ae110087?w=800",
                "description": "Базовый набор офисных принадлежностей с современным дизайном.",
                "material": "Качественные офисные принадлежности",
                "color": "Разноцветный",
                "in_stock": True,
                "stock_quantity": 200,
                "delivery_time": "2-3 рабочих дня",
                "branding_available": True,
                "branding_types": ["Печать"],
                "is_popular": True,
            },
        ]

        for item in products_data:
            category_name = item.pop("category")
            Product.objects.create(category=categories[category_name], **item)

        self.stdout.write(self.style.SUCCESS("Готово: 8 товаров добавлены"))