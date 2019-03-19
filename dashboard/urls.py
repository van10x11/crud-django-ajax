from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
	path('',views.mahasiswa_list,name='mahasiswa-list'),
	path('mahasiswa/add/',views.mahasiswa_tambah,name='mahasiswa-tambah'),
	path('mahasiswa/<int:nim_mahasiswa>/delete/',views.mahasiswa_hapus,name='mahasiswa-hapus'),
	path('mahasiswa/<int:nim_mahasiswa>/update/',views.mahasiswa_ubah,name='mahasiswa-ubah'),
	path('mahasiswa/cari/hasil',views.mahasiswa_cari,name='mahasiswa-cari'),
]