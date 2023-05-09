from addresses.models import Address
from addresses.serializers import AddressSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from addresses.permissions import IsOwnerAddress
from users.permissions import IsSuperuserOrCreate
from rest_framework.response import Response
from addresses.serializers import AddressSerializer
import ipdb


# Create your views here.
class AddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        list_by_user = Address.objects.filter(user=request.user)
        serializer = AddressSerializer(list_by_user, many=True)

        return Response(serializer.data)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerAddress]
    lookup_url_kwarg = "address_id"

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)
