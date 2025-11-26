from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @action(detail=False, methods=['get'])
    def visible(self, request):
        """API برای منوهای قابل نمایش"""
        menus = Menu.objects.filter(is_visible=True, parent__isnull=True)
        serializer = self.get_serializer(menus, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def reorder(self, request):
        """مرتب‌سازی منوها"""
        order_data = request.data.get('order', [])
        for index, menu_id in enumerate(order_data):
            Menu.objects.filter(id=menu_id).update(order=index)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
