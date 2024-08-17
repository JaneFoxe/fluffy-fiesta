from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """
    Класс разрешений, который позволяет доступ только аутентифицированным и активным пользователям.

    Доступ предоставляется, если пользователь прошел аутентификацию и отмечен как активный.

    Методы:
        has_permission(request, view):
            Возвращает True, если пользователь аутентифицирован и активен, иначе False.

    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_active:
            return True
        return False
