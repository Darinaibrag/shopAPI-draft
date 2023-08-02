from rest_framework.permissions import BasePermission # Мы импортируем базовый класс BasePermission из Django REST Framework, который используется для создания пользовательских правил разрешений.


class IsAuthor(BasePermission): # Этот класс будет определять правило разрешения, позволяющее доступ только автору объекта (например, авторизованному пользователю, создавшему данный объект)
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
        # Здесь мы сравниваем пользователя, отправившего запрос (request.user),
        # с владельцем объекта (obj.owner). Если пользователь совпадает с владельцем,
        # то правило разрешения возвращает True, что означает, что у пользователя есть доступ к объекту.
        # В противном случае, если пользователь не является владельцем, правило разрешения вернет False, и доступ будет запрещен.

