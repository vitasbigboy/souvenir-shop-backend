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

        categories = {
            name: Category.objects.create(name=name, slug=slug)
            for name, slug in categories_data
        }

        products_data = [
            {
                "category": "Канцелярия",
                "name": "Премиум набор блокнотов",
                "article": "GS-NB-001",
                "price": 2500,
                "image": "https://images.unsplash.com/photo-1510922903530-28ecf3f00362?w=800",
                "description": "Элегантный набор блокнотов в кожаном переплете, идеально подходит для корпоративных подарков. Высококачественная бумага, возможность нанесения логотипа компании.",
                "material": "Премиум кожа",
                "color": "Черный",
                "characteristics": [
                    {"name": "Размер", "value": "A5 (148 x 210 мм)"},
                    {"name": "Страницы", "value": "200 листов в линейку"},
                    {"name": "Материал", "value": "Премиум кожа"},
                    {"name": "Вес", "value": "350 г"},
                ],
                "tags": ["С логотипом", "Для коллег", "Наборы"],
                "gallery": [
                    "https://images.unsplash.com/photo-1510922903530-28ecf3f00362?w=800",
                    "https://images.unsplash.com/photo-1508873699372-7aeab60b44ab?w=800",
                    "https://images.unsplash.com/photo-1516390118834-21602d501886?w=800",
                ],
                "colors": [
                    {"name": "Черный", "hex": "#000000"},
                    {"name": "Коричневый", "hex": "#8B4513"},
                    {"name": "Синий", "hex": "#000080"},
                ],
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
                "description": "Роскошный подарочный набор с премиальными офисными аксессуарами. Включает ручку, блокнот и визитницу.",
                "material": "Премиальные материалы",
                "color": "Черный",
                "characteristics": [
                    {"name": "Содержимое", "value": "Ручка, блокнот, визитница"},
                    {"name": "Материал", "value": "Премиальные материалы"},
                    {"name": "Упаковка", "value": "Подарочная коробка люкс"},
                    {"name": "Размеры", "value": "30 x 25 x 8 см"},
                ],
                "tags": ["С логотипом", "Для коллег", "Наборы", "Для мужчин"],
                "gallery": [
                    "https://images.unsplash.com/photo-1544377208-215a63786183?w=800",
                    "https://images.unsplash.com/photo-1697719274531-5b647347a1ed?w=800",
                    "https://images.unsplash.com/photo-1694481903606-822baa14f7ab?w=800",
                ],
                "colors": [
                    {"name": "Черный", "hex": "#000000"},
                    {"name": "Серебристый", "hex": "#C0C0C0"},
                ],
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
                "description": "Высококачественная керамическая кружка с премиальной отделкой. Идеально подходит для брендирования и ежедневного использования в офисе.",
                "material": "Премиум керамика",
                "color": "Белый",
                "characteristics": [
                    {"name": "Объем", "value": "350 мл"},
                    {"name": "Материал", "value": "Премиум керамика"},
                    {"name": "Уход", "value": "Можно мыть в посудомойке"},
                    {"name": "Размеры", "value": "9 x 8 см"},
                ],
                "tags": ["С логотипом", "Для коллег"],
                "gallery": [
                    "https://images.unsplash.com/photo-1618381801643-3d253a63a386?w=800",
                    "https://images.unsplash.com/photo-1516390118834-21602d501886?w=800",
                    "https://images.unsplash.com/photo-1562878274-ad7a29ea8cdd?w=800",
                ],
                "colors": [
                    {"name": "Белый", "hex": "#FFFFFF"},
                    {"name": "Черный", "hex": "#000000"},
                    {"name": "Серый", "hex": "#808080"},
                ],
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
                "description": "Премиальный набор письменных принадлежностей в элегантной подарочной коробке. Идеальный подарок для руководителя.",
                "material": "Металл с премиальной отделкой",
                "color": "Серебристый",
                "characteristics": [
                    {"name": "Содержимое", "value": "Шариковая и перьевая ручка"},
                    {"name": "Материал", "value": "Металл с премиальной отделкой"},
                    {"name": "Презентация", "value": "Подарочная коробка в комплекте"},
                    {"name": "Вес", "value": "120 г (набор)"},
                ],
                "tags": ["Для коллег", "Для мужчин", "Наборы"],
                "gallery": [
                    "https://images.unsplash.com/photo-1650735311937-1876825e971b?w=800",
                    "https://images.unsplash.com/photo-1650735310411-19b29700012d?w=800",
                    "https://images.unsplash.com/photo-1650735311842-699bd178babd?w=800",
                ],
                "colors": [
                    {"name": "Серебристый", "hex": "#C0C0C0"},
                    {"name": "Золотой", "hex": "#FFD700"},
                    {"name": "Черный", "hex": "#000000"},
                ],
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
                "description": "Полный корпоративный подарочный пакет с премиальным набором офисных аксессуаров и брендированных товаров.",
                "material": "Высококачественные материалы",
                "color": "Черный",
                "characteristics": [
                    {"name": "Содержимое", "value": "Множество премиальных товаров"},
                    {"name": "Материал", "value": "Высококачественные материалы"},
                    {"name": "Упаковка", "value": "Подарочная коробка люкс"},
                    {"name": "Брендирование", "value": "Полный пакет брендирования"},
                ],
                "tags": ["С логотипом", "Наборы", "Для коллег", "Для мужчин"],
                "gallery": [
                    "https://images.unsplash.com/photo-1694481901573-a970f982ac5e?w=800",
                    "https://images.unsplash.com/photo-1720785004894-95a93636b58f?w=800",
                    "https://images.unsplash.com/photo-1720785004324-e4ecc9a00c62?w=800",
                ],
                "colors": [],
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
                "description": "Специальный новогодний корпоративный подарочный набор с праздничной упаковкой и премиальным содержимым.",
                "material": "Премиальная подборка",
                "color": "Красный",
                "characteristics": [
                    {"name": "Содержимое", "value": "Сезонные подарочные товары"},
                    {"name": "Материал", "value": "Премиальная подборка"},
                    {"name": "Упаковка", "value": "Праздничный дизайн"},
                    {"name": "Сезон", "value": "Новый год 2026"},
                ],
                "tags": ["С логотипом", "Наборы", "Новый год"],
                "gallery": [
                    "https://images.unsplash.com/photo-1697717657359-46433ee8497c?w=800",
                    "https://images.unsplash.com/photo-1697719274531-5b647347a1ed?w=800",
                    "https://images.unsplash.com/photo-1694481903606-822baa14f7ab?w=800",
                ],
                "colors": [],
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
                "description": "Полный набор бизнес-аксессуаров с элегантным дизайном и премиальным качеством.",
                "material": "Премиальные материалы",
                "color": "Черный",
                "characteristics": [
                    {"name": "Содержимое", "value": "Офисные принадлежности"},
                    {"name": "Материал", "value": "Премиальные материалы"},
                    {"name": "Дизайн", "value": "Профессиональный и элегантный"},
                    {"name": "Упаковка", "value": "Премиальная коробка"},
                ],
                "tags": ["С логотипом", "Для коллег", "Для мужчин", "Наборы"],
                "gallery": [
                    "https://images.unsplash.com/photo-1546313960-15422d64201a?w=800",
                    "https://images.unsplash.com/photo-1605174697130-0bb0b83c92fc?w=800",
                    "https://images.unsplash.com/photo-1544377208-215a63786183?w=800",
                ],
                "colors": [],
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
                "description": "Базовый набор офисных принадлежностей с современным дизайном. Идеален для новых сотрудников или командных подарков.",
                "material": "Качественные офисные принадлежности",
                "color": "Разноцветный",
                "characteristics": [
                    {"name": "Содержимое", "value": "Блокнот, ручки, стикеры"},
                    {"name": "Материал", "value": "Качественные офисные принадлежности"},
                    {"name": "Дизайн", "value": "Современный и яркий"},
                    {"name": "Количество", "value": "Несколько предметов"},
                ],
                "tags": ["С логотипом", "Для коллег", "Наборы"],
                "gallery": [
                    "https://images.unsplash.com/photo-1582993467771-54d2ae110087?w=800",
                    "https://images.unsplash.com/photo-1531346479518-1ddeedc3ff77?w=800",
                    "https://images.unsplash.com/photo-1508873699372-7aeab60b44ab?w=800",
                ],
                "colors": [
                    {"name": "Разноцветный", "hex": "#FF6B6B"},
                    {"name": "Синяя гамма", "hex": "#4A90E2"},
                    {"name": "Зеленая гамма", "hex": "#7ED321"},
                ],
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