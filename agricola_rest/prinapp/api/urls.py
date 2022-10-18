from django.urls import URLPattern, path
from prinapp.api.api import *

urlpatterns = [
    #urls api
    path('cliente/', client_api_view, name = 'cliente_api'),
    path('proveedor/', supplier_api_view, name = 'proveedor_api'),
    path('producto/', product_api_view, name = 'producto_api'),
    path('conductor/', driver_api_view, name = 'conductor_api'),
    path('fechas/', times_api_view, name = 'fechas_api'),
    path('reportes/', reports_api_view, name = 'reportes_api'),
    #urls details
    path('cliente/<int:pk>/',client_detail_api_view,name='cliente_detail_api_view'),
    path('proveedor/<int:pk>/',supplier_detail_api_view,name='proveedor_detail_api_view'),
    path('producto/<int:pk>/',product_detail_api_view,name='producto_detail_api_view'),
    path('conductor/<int:pk>/',driver_detail_api_view,name='conductor_detail_api_view'),
    path('fechas/<int:pk>/',times_detail_api_view,name='fechas_detail_api_view'),
    path('reportes/<int:pk>/',reports_detail_api_view,name='reportes_detail_api_view')
]
