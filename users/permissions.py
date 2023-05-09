from rest_framework import permissions


class IsSuperuserOrCreate(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method == "GET":
            return request.user.is_superuser and request.user

        return True
