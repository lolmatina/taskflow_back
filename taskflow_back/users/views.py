from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomTokenObtainPairSerializer

class SignInView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        operation_description="User sign-in",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['username', 'password']
        )
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SignOutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="User sign-out",
        responses={205: 'Token blacklisted'}
    )
    def get(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()

            return Response({"detail": "Token blacklisted"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail": "Invalid token or token missing"}, status=status.HTTP_400_BAD_REQUEST)
