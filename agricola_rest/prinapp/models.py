from django.db import models
from simple_history.models import HistoricalRecords


#tabla del cliente
class client(models.Model):
	username = models.CharField(max_length=255, unique = True)
	name = models.CharField('Nombres', max_length = 50)
	last_name = models.CharField('Apellidos', max_length = 255)
	cell_phone = models.CharField('Telefono', max_length = 10, unique = True)
	RFC = models.CharField('RFC', max_length = 13, unique = True)
	email = models.EmailField('Correo Electronico', max_length = 100, unique = True)
	street = models.CharField('Calle', max_length = 255)
	suburb = models.CharField('Colonia', max_length = 255)
	postal_code = models.CharField('Código Postal', max_length = 5)
	outdoor_num = models.CharField('Numero Exterior', max_length = 5, blank = True)
	historical = HistoricalRecords()
	def __str__(self):
		return f'{self.name} {self.last_name} {self.cell_phone} {self.RFC} {self.email}'
	class Meta:
		verbose_name = 'Cliente'

#tabla del proveedor
class supplier(models.Model):
	tradename = models.CharField('Nombre Comercial', max_length = 255)
	business_name = models.CharField('Razon Social', max_length = 255)
	cell_phone = models.CharField('Telefono', max_length = 10, unique = True)
	RFC = models.CharField('RFC', max_length = 13, unique = True)
	email = models.EmailField('Correo Electronico', max_length = 100, unique = True)
	street = models.CharField('Calle', max_length = 255)
	suburb = models.CharField('Colonia', max_length = 255)
	postal_code = models.CharField('Código Postal', max_length = 5)
	outdoor_num = models.CharField('Numero Exterior', max_length = 5, blank = True)
	historical = HistoricalRecords()
	def __str__(self):
		return f'{self.tradename} {self.business_name} {self.cell_phone} {self.RFC} {self.email}'
	class Meta:
		verbose_name = 'Proveedore'
#nombre y detalle de producto
class product(models.Model):
	product_name = models.CharField('Nombre del producto', max_length = 255)
	registry_resp = models.CharField('Responsable del registro', max_length = 255)
	image =  models.ImageField('Imagen del prodcuto', upload_to= 'producto/', max_length=255, null =True, blank = True)
	amount_kg = models.CharField('Cantidad en kilo gramo', max_length = 10, unique = True)
	price = models.IntegerField('Precio', default = 0)
	historical = HistoricalRecords()	
	def __str__(self):
		return f'{self.product_name} {self.registry_resp} {self.amount_kg}'	
	class Meta:
		verbose_name = 'Producto'

#tabla del chofer o distribución
class driver(models.Model):
	name = models.CharField('Nombre del chofer', max_length = 255)
	last_name = models.CharField('Apellidos', max_length = 255)
	cell_phone = models.CharField('Telefono', max_length = 10, unique = True)
	tuition = models.CharField('Matricula', max_length = 8)
	type_vehicle = models.CharField('Tipo de vehiculo', max_length = 255)
	historical = HistoricalRecords()
	def __str__(self):
		return f'{self.name} {self.last_name} {self.cell_phone} {self.tuition}'
	class Meta:
		verbose_name = 'Distribucione'


#tablas de fechas
class time(models.Model):
	date_in = models.DateTimeField('Fecha de ingreso')
	date_out = models.DateTimeField('Fecha de salida')
	arrival_date = models.DateTimeField('Fecha de llegada')
	def __str__(self):
		return f'{self.date_in} {self.date_out} {self.arrival_date}'

#tabla sobre los reportes
class reports(models.Model):
	name_reports = models.CharField('Nombre del reporte', max_length = 255)
	def __str__(self):	
		return f'{self.name_reports}'
