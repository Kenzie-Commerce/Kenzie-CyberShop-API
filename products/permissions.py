from rest_framework import permissions
from rest_framework.request import Request
from products.models import Product
from rest_framework.views import View


class IsSeller(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return bool(
            request.method == "GET"
            or request.user.is_superuser
            or request.user.is_seller
        )


class isSellerOwner(permissions.BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: Product,
    ):
        return bool(request.user == obj.seller_id)
