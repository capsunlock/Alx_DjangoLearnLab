from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    Returns all notifications for the authenticated user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notifications.all().order_by('-timestamp')

class MarkNotificationAsReadView(generics.UpdateAPIView):
    """
    Allows a user to mark a specific notification as read.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.request.user.notifications.all()

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)