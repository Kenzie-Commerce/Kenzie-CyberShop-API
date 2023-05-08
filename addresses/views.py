from addresses.models import Address
from addresses.serializers import AddressSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from addresses.permissions import IsOwnerAddress


# Create your views here.
class AddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerAddress]
    lookup_url_kwarg = "address_id"

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)
