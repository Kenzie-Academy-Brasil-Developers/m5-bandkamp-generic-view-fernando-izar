from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):

    @extend_schema(
        operation_id="get_user",
        parameters=[
            UserSerializer,
            OpenApiParameter("id", int, OpenApiParameter.PATH),
            OpenApiParameter("username", str, OpenApiParameter.PATH),
            OpenApiParameter("email", str, OpenApiParameter.PATH),
            OpenApiParameter("password", str, OpenApiParameter.PATH),
            OpenApiParameter("first_name", str, OpenApiParameter.PATH),
            OpenApiParameter("last_name", str, OpenApiParameter.PATH),
            OpenApiParameter("is_superuser", bool, OpenApiParameter.PATH),],
        description="Rota para obter um usuário",
        summary="Obter um usuário",
        tags=["users"],
    )
    def get(self, request: Request, pk: int) -> Response:
        ...

    @extend_schema(
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        ... 
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
