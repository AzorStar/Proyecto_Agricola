from rest_framework.views import APIView
from rest_framework.response import Response
from prinapp.api.serializers import *
from prinapp.models import *
from rest_framework.decorators import api_view
from rest_framework import status

#client api
@api_view(['GET','POST'])
def client_api_view(request):

    if request.method == 'GET':
        clients = client.objects.all()
        clients_serializer = ClientSerializer(clients, many = True)
        return Response(clients_serializer.data)
    elif request.method == 'POST':
        client_serializer = ClientSerializer(data = request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data)
        return Response(client_serializer.errors)

#client detail
@api_view(['GET','PUT','DELETE'])
def client_detail_api_view(request,pk=None):
    #queryset
    clients = client.objects.filter(id=pk).first()

    #validation
    if clients:

        #retrieve
        if request.method == 'GET':
            clients_serializer = ClientSerializer(clients)
            return Response(clients_serializer.data,status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            clients_serializer = ClientSerializer(clients,data = request.data)
            if clients_serializer.is_valid():
                clients_serializer.save()
                return Response(clients_serializer.data,status = status.HTTP_200_OK)
            return Response(clients_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            clients.delete()
            return Response({'message':'Cliente Eliminado Correctamente'},status = status.HTTP_200_OK)
    return Response({'message':'Nose ha encontrado un cliente con estos datos'},status = status.HTTP_400_BAD_REQUEST)


#supplier api
@api_view(['GET','POST'])
def supplier_api_view(request):

    if request.method == 'GET':
        suppliers = supplier.objects.all()
        suppliers_serializer = SupplierSerializer(suppliers, many = True)
        return Response(suppliers_serializer.data)
    elif request.method == 'POST':
        supplier_serializer = SupplierSerializer(data = request.data)
        if supplier_serializer.is_valid():
            supplier_serializer.save()
            return Response(supplier_serializer.data)
        return Response(supplier_serializer.errors)

#supplier detail
@api_view(['GET','PUT','DELETE'])
def supplier_detail_api_view(request,pk=None):
    #queryset
    suppliers = supplier.objects.filter(id=pk).first()

    #validation
    if suppliers:

        #retrieve
        if request.method == 'GET':
            suppliers_serializer = SupplierSerializer(suppliers)
            return Response(suppliers_serializer.data,status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            suppliers_serializer = SupplierSerializer(suppliers,data = request.data)
            if suppliers_serializer.is_valid():
                suppliers_serializer.save()
                return Response(suppliers_serializer.data,status = status.HTTP_200_OK)
            return Response(suppliers_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            suppliers.delete()
            return Response({'message':'Proveedor Eliminado Correctamente'},status = status.HTTP_200_OK)
    return Response({'message':'Nose ha encontrado un proveedor con estos datos'},status = status.HTTP_400_BAD_REQUEST)

#producto api
@api_view(['GET','POST'])
def product_api_view(request):

    if request.method == 'GET':
        products = product.objects.all()
        products_serializer = ProductSerializer(products, many = True)
        return Response(products_serializer.data)
    elif request.method == 'POST':
        product_serializer = ProductSerializer(data = request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors)    

#product detail
@api_view(['GET','PUT','DELETE'])
def product_detail_api_view(request,pk=None):
    #queryset
    products = product.objects.filter(id=pk).first()

    #validation
    if products:

        #retrieve
        if request.method == 'GET':
            products_serializer = ProductSerializer(products)
            return Response(products_serializer.data,status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            products_serializer = ProductSerializer(products,data = request.data)
            if products_serializer.is_valid():
                products_serializer.save()
                return Response(products_serializer.data,status = status.HTTP_200_OK)
            return Response(products_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            products.delete()
            return Response({'message':'Producto Eliminado Correctamente'},status = status.HTTP_200_OK)
    return Response({'message':'Nose ha encontrado un producto con estos datos'},status = status.HTTP_400_BAD_REQUEST)


#driver api
@api_view(['GET','POST'])
def driver_api_view(request):

    if request.method == 'GET':
        drivers = driver.objects.all()
        drivers_serializer = DriverSerializer(drivers, many = True)
        return Response(drivers_serializer.data)
    elif request.method == 'POST':
        driver_serializer = DriverSerializer(data = request.data)
        if driver_serializer.is_valid():
            driver_serializer.save()
            return Response(driver_serializer.data)
        return Response(driver_serializer.errors)      

#driver detail
@api_view(['GET','PUT','DELETE'])
def driver_detail_api_view(request,pk=None):
    #queryset
    drivers = driver.objects.filter(id=pk).first()

    #validation
    if drivers:

        #retrieve
        if request.method == 'GET':
            drivers_serializer = DriverSerializer(drivers)
            return Response(drivers_serializer.data,status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            drivers_serializer = DriverSerializer(drivers,data = request.data)
            if drivers_serializer.is_valid():
                drivers_serializer.save()
                return Response(drivers_serializer.data,status = status.HTTP_200_OK)
            return Response(drivers_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            drivers.delete()
            return Response({'message':'Conductor Eliminado Correctamente'},status = status.HTTP_200_OK)
    return Response({'message':'Nose ha encontrado un conductor con estos datos'},status = status.HTTP_400_BAD_REQUEST)



#times api
@api_view(['GET','POST'])
def times_api_view(request):

    if request.method == 'GET':
        times = time.objects.all()
        times_serializer = TimeSerializer(times, many = True)
        return Response(times_serializer.data)
    elif request.method == 'POST':
        time_serializer = TimeSerializer(data = request.data)
        if time_serializer.is_valid():
            time_serializer.save()
            return Response(time_serializer.data)
        return Response(time_serializer.errors)  

#times detail
@api_view(['GET','PUT','DELETE'])
def times_detail_api_view(request,pk=None):
    #queryset
    times = time.objects.filter(id=pk).first()

    #validation
    if times:

        #retrieve
        if request.method == 'GET':
            times_serializer = TimeSerializer(times)
            return Response(times_serializer.data,status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            times_serializer = TimeSerializer(times,data = request.data)
            if times_serializer.is_valid():
                times_serializer.save()
                return Response(times_serializer.data,status = status.HTTP_200_OK)
            return Response(times_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            times.delete()
            return Response({'message':'Fecha Eliminada Correctamente'},status = status.HTTP_200_OK)
    return Response({'message':'Nose ha encontrado una fecha con estos datos'},status = status.HTTP_400_BAD_REQUEST)



#reports api
@api_view(['GET','POST'])
def reports_api_view(request):

    if request.method == 'GET':
        reportss = reports.objects.all()
        reportss_serializer = ReportsSerializer(reportss, many = True)
        return Response(reportss_serializer.data)
    elif request.method == 'POST':
        reports_serializer = ReportsSerializer(data = request.data)
        if reports_serializer.is_valid():
            reports_serializer.save()
            return Response(reports_serializer.data)
        return Response(reports_serializer.errors) 

#reports detail
@api_view(['GET','PUT','DELETE'])
def reports_detail_api_view(request,pk=None):
    #queryset
    reportss = reports.objects.filter(id=pk).first()

    #validation
    if reportss:

        #retrieve
        if request.method == 'GET':
            reports_serializer = ReportsSerializer(reportss)
            return Response(reports_serializer.data,status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            reports_serializer = ReportsSerializer(reportss,data = request.data)
            if reports_serializer.is_valid():
                reports_serializer.save()
                return Response(reports_serializer.data,status = status.HTTP_200_OK)
            return Response(reports_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            reports.delete()
            return Response({'message':'Reporte Eliminado Correctamente'},status = status.HTTP_200_OK)
    return Response({'message':'Nose ha encontrado un reporte con estos datos'},status = status.HTTP_400_BAD_REQUEST)