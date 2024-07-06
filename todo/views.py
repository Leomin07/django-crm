from rest_framework.exceptions import ValidationError
from rest_framework.decorators import (
    authentication_classes,
    permission_classes,
    api_view,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework import status, generics
from django.contrib.auth import authenticate
from todo.authenticate import (
    ExpiringTokenAuthentication,
    token_expire_handler,
)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from todo.serializers import UserLoginSerializer, UserRegisterSerializer, UserSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [ExpiringTokenAuthentication]

    def get_object(self):
        return self.request.user


@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    signin_serializer = UserLoginSerializer(data=request.data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)

        is_expired, token = token_expire_handler(token)
        return Response(
            {
                "token": token.key,
            }
        )
    return Response({"msg": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@permission_classes([AllowAny])
def user_register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {
            "success": True,
            "token": Token.objects.get(
                user=User.objects.get(username=serializer.data["username"])
            ).key,
        }
        return Response(response, status=status.HTTP_200_OK)
    raise ValidationError(serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout_user(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    return Response({"msg": "Successfully Logged out"}, status=status.HTTP_200_OK)
