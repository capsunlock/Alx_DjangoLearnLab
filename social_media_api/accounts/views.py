from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import CustomUser

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.GenericAPIView):
    """
    View to follow a user.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        # Use get_object_or_404 to ensure the user exists
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return Response({"message": f"Successfully followed {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    """
    View to unfollow a user.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"Successfully unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)