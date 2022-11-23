from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    return Response(data)
#        json_data_str = json.dumps(data)
#    return HttpResponse(json_data_str, headers={"content-type": "application/json"})

