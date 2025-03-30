# Проект на Django - онлайн магазин телефонов и планшетов
## Модели
Реализовано несколько моделей для продукции, отзывов, заказов и т.д., а также сериализаторы к ним.
- Product
- Tag
- Brand
- Order
- Review
- Cart

Также есть модель User, позже заменённая на модель из django.contrib.auth.models.

## Вьюшки
Вьюшки есть для каждой модели, подключены с помощью роутинга.
Отдельно выполнена MakingOrderViewSet, для создания заказа:
> Через этот вьюсет создаётся заказ, удаляется корзина, а также уменьшается количество продукции.

## Аутентификация
Есть базовая аутентификация через токены, также есть проверка на GET запрос через отдельный файл `permissions.py`

