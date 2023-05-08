from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from requests.models import Request
from requests.serializers import RequestSerializer
from django.core.mail import send_mail
from django.conf import settings
from requests.models import Request
from users.models import User


class RequestViews(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        product = self.request.data.get("product")

        for prod in product:
            product_name = prod["name"]
            seller = User.objects.get(id=prod["seller_id"])

            send_mail(
                subject="Pedido recebido",
                message=f"O usuário com email {self.request.user.email} \
comprou o produto {product_name}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f"{seller.email}"],
                fail_silently=False,
            )

        send_mail(
            subject=f"Kenzie Commerce",
            message=f"Obrigado por comprar conosco!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{self.request.user.email}"],
            fail_silently=False,
        )

        return serializer.save(
            product=product,
            user=self.request.user,
        )


class RequestDetailViews(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    lookup_url_kwarg = "request_id"

    def perform_update(self, serializer):
        request = Request.objects.get(id=self.kwargs["request_id"])
        status = self.request.data["status"]

        send_mail(
            subject="Status do pedido",
            message=f"O status do seu pedido foi alterado para {status}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{request.user.email}"],
            fail_silently=False,
        )

        return super().perform_update(serializer)
