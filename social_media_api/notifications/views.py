from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        data = []
        for n in notifications:
            data.append({
                'id': n.id,
                'actor': n.actor.username,
                'verb': n.verb,
                'target': str(n.target),
                'timestamp': n.timestamp,
            })
        return Response(data)
