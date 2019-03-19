from django.db import models

class Mahasiswa(models.Model):
	nim = models.IntegerField(primary_key=True)
	nama = models.CharField(max_length=100)
	jenis_kelamin = models.CharField(max_length=2,choices = (
		('L','Laki-laki'),
		('P','Perempuan'),
	),default=None)
	tempat_lahir = models.CharField(max_length=100)
	tanggal_lahir = models.DateField()
	agama = models.CharField(max_length=10,choices = (
		('islam','Islam'),
		('kristen','Kristen'),
		('protestan','Protestan'),
		('budha','Budha'),
		('hindu','Hindu'),
	),default=None)

	alamat = models.TextField()

	def __str__(self):
		return f"{self.nim}: {self.nama}"

