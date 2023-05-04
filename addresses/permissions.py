from rest_framework import permissions
from addresses.models import Address


class IsOwnerAddress(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Address) -> bool:
        return request.user == obj.user or request.user.is_superuser
