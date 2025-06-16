from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from .serializers import ForgotPasswordSerializer  # ✅ हे पण लागेल

# ✅ 1. Register View
class RegisterView(APIView):

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 2. Login View
class LoginView(APIView):

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


# ✅ 3. Forgot Password View (बाहेर define कर)
class ForgotPasswordView(APIView):

    @swagger_auto_schema(request_body=ForgotPasswordSerializer)
    def post(self, request):
        email = request.data.get('email')
        return Response({"message": f"Password reset link sent to {email}"}, status=status.HTTP_200_OK)
