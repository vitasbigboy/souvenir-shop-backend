from django.core.mail import send_mail
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response

from .models import Product, Category
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    OrderCreateSerializer,
    FeedbackSerializer,
)


@api_view(['GET'])
def ping(request):
    return Response({'message': 'pong'})


@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')
    price_from = request.GET.get('priceFrom')
    price_to = request.GET.get('priceTo')
    in_stock = request.GET.get('inStock')
    branding = request.GET.get('brandingAvailable')
    sort = request.GET.get('sort')

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(article__icontains=search) |
            Q(description__icontains=search)
        )

    if category:
        products = products.filter(category__slug=category)

    if price_from:
        products = products.filter(price__gte=price_from)

    if price_to:
        products = products.filter(price__lte=price_to)

    if in_stock == 'true':
        products = products.filter(in_stock=True, stock_quantity__gt=0)

    if branding == 'true':
        products = products.filter(branding_available=True)

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name_asc':
        products = products.order_by('name')
    else:
        products = products.order_by('-is_popular', 'name')

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {'error': 'Товар не найден'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filters(request):
    categories = Category.objects.all()

    data = {
        'categories': CategorySerializer(categories, many=True).data,
        'price': {
            'min': Product.objects.order_by('price').first().price if Product.objects.exists() else 0,
            'max': Product.objects.order_by('-price').first().price if Product.objects.exists() else 0,
        },
        'inStock': True,
        'brandingAvailable': True,
        'sortOptions': [
            {'value': 'price_asc', 'label': 'Сначала дешевле'},
            {'value': 'price_desc', 'label': 'Сначала дороже'},
            {'value': 'name_asc', 'label': 'По названию'},
        ]
    }

    return Response(data)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def create_order(request):
    serializer = OrderCreateSerializer(data=request.data)

    if serializer.is_valid():
        order = serializer.save()

        # Пока email выводится в консоль, чтобы не настраивать SMTP
        send_mail(
            subject=f'Новая заявка #{order.id}',
            message=f'''
Новая заявка с сайта.

ФИО: {order.full_name}
Город: {order.city}
Телефон: {order.phone}
Email: {order.email}
Компания: {order.company_name}
ИНН: {order.inn}
Комментарий: {order.comment}

Сумма заказа: {order.total} ₽
''',
            from_email='noreply@example.com',
            recipient_list=['manager@example.com'],
            fail_silently=True,
        )

        send_mail(
            subject=f'Ваша заявка #{order.id} принята',
            message=f'''
Здравствуйте, {order.full_name}!

Ваша заявка принята.
Сумма заказа: {order.total} ₽

Менеджер свяжется с вами для уточнения деталей.
''',
            from_email='noreply@example.com',
            recipient_list=[order.email],
            fail_silently=True,
        )

        return Response(
            {'message': 'Заявка успешно отправлена', 'order_id': order.id},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_feedback(request):
    serializer = FeedbackSerializer(data=request.data)

    if serializer.is_valid():
        feedback = serializer.save()

        send_mail(
            subject='Новое сообщение обратной связи',
            message=f'''
Имя: {feedback.name}
Телефон: {feedback.phone}
Email: {feedback.email}

Сообщение:
{feedback.message}
''',
            from_email='noreply@example.com',
            recipient_list=['manager@example.com'],
            fail_silently=True,
        )

        return Response(
            {'message': 'Сообщение успешно отправлено'},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)