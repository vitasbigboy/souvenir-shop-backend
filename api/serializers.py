from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Feedback


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'article',
            'price',
            'image',
            'description',
            'material',
            'color',
            'in_stock',
            'stock_quantity',
            'delivery_time',
            'branding_available',
            'branding_types',
            'is_popular',
            'category',
        ]


class OrderItemCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
    color = serializers.CharField(required=False, allow_blank=True)
    branding_selected = serializers.BooleanField(default=False)


class OrderCreateSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    city = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    comment = serializers.CharField(required=False, allow_blank=True)

    company_name = serializers.CharField(required=False, allow_blank=True)
    inn = serializers.CharField(required=False, allow_blank=True)
    company_card = serializers.FileField(required=False)

    items = OrderItemCreateSerializer(many=True)

    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError('Корзина не может быть пустой.')
        return items

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total = 0

        for item_data in items_data:
            product = Product.objects.get(id=item_data['product_id'])

            if not product.in_stock or product.stock_quantity <= 0:
                raise serializers.ValidationError(
                    f'Товар "{product.name}" отсутствует в наличии.'
                )

            quantity = item_data['quantity']
            price = product.price
            total += price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                product_name=product.name,
                price=price,
                quantity=quantity,
                color=item_data.get('color', ''),
                branding_selected=item_data.get('branding_selected', False),
            )

        if total < 15000:
            raise serializers.ValidationError(
                'Минимальная сумма заказа — 15 000 ₽.'
            )

        order.total = total
        order.save()

        return order


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'phone', 'email', 'message', 'created_at']