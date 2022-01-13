from reviews.serializers import ProductSerializer
from reviews.models import Product
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action

class ProductVeiwSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(detail=False)
    def get_list(self, request):
        pass

    @action(detail=True)
    def get_product(self, request, pk=None):
        pass

    @action(detail=True, methods=['post', 'delete'])
    def delete_product(self, request, pk=None):
        pass
