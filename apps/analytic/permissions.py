from rest_framework.permissions import BasePermission


class AdminRolePermission(BasePermission):
    """Предоставление прав доступа пользователям с ролью ADMIN"""

    def has_permission(self, request, view):
        return request.user.role == 'admin'
