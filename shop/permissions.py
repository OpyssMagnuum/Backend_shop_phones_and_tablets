from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Проверяем является ли пользователь, который сделал запрос тем, кто владеет объектом
        # Либо только для чтения

        if request.method == 'GET':
            return True
        return request.user == obj.user
