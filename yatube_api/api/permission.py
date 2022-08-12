from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission на уровне объекта, чтобы разрешить
    редактирование только автору объекта."""
    def has_object_permission(self, request, view, obj):
        # Проверить разрешения для запроса только на чтение
        # SAFE_METHODS - кортеж, содержащий запросы 'GET', 'OPTIONS'и 'HEAD'
        if request.method in permissions.SAFE_METHODS:
            return True
        # Экземпляр должен иметь атрибут с именем `author`.
        return obj.author == request.user
