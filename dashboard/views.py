from django.shortcuts import render,redirect, get_object_or_404
from .models import Mahasiswa
from .forms import MahasiswaForm
from django.db.models import Q

from django.http import JsonResponse
from django.template.loader import render_to_string

def mahasiswa_list(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		mahasiswa_list = Mahasiswa.objects.all().order_by('nama')
		return render(request,'dashboard/mahasiswa_list.html',{'mahasiswa_list':mahasiswa_list,'title':'List Mahasiswa'})
	else:
		return redirect('login')

def mahasiswa_cari(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		if request.method == 'GET':
			cari = request.GET['cari']
			mahasiswa_list = Mahasiswa.objects.filter(Q(nim__contains=cari)|Q(nama__contains=cari)|Q(alamat__contains=cari))
			banyak_data = mahasiswa_list.count()
			if banyak_data != 0:
				banyak_data = banyak_data
			else:
				banyak_data = 'tidak ada data'
			context = {
				'mahasiswa_list':mahasiswa_list,
				'banyak_data':banyak_data,
				'title':'List Mahasiswa',
			}
			return render(request,'dashboard/mahasiswa_list.html',context)
		
	else:
		return redirect('login')

def mahasiswa_form_save(request,form,template_name):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		data = dict()
		if request.method == 'POST':
			if form.is_valid():
				form.save()
				data['form_is_valid'] = True
				mahasiswa_list = Mahasiswa.objects.all().order_by('nama')
				data['html_mahasiswa_list'] = render_to_string('dashboard/includes/partial_mahasiswa_list.html', {
	                'mahasiswa_list': mahasiswa_list
	            })
			else:
				data['form_is_valid'] = False
		context = {'form': form}
		data['html_form'] = render_to_string(template_name, context, request=request)
		return JsonResponse(data)
	else:
		return redirect('login')


def mahasiswa_tambah(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		if request.method == 'POST':
			form = MahasiswaForm(request.POST)
		else:
			form = MahasiswaForm()
		return mahasiswa_form_save(request, form, 'dashboard/includes/partial_mahasiswa_tambah.html')
	else:
		return redirect('login')


def mahasiswa_ubah(request,nim_mahasiswa):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		mahasiswa = get_object_or_404(Mahasiswa,nim=nim_mahasiswa)
		if request.method == "POST":
			form = MahasiswaForm(request.POST,instance=mahasiswa)
		else:
			form = MahasiswaForm(instance=mahasiswa)
		return mahasiswa_form_save(request,form,'dashboard/includes/partial_mahasiswa_ubah.html')
	else:
		return redirect('login')




def mahasiswa_hapus(request,nim_mahasiswa):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		mahasiswa = get_object_or_404(Mahasiswa,nim=nim_mahasiswa)
		data = dict()
		if request.method == "POST":
			mahasiswa.delete()
			data['form_is_valid'] = True
			mahasiswa_list = Mahasiswa.objects.all().order_by('nama')
			data['html_mahasiswa_list'] = render_to_string('dashboard/includes/partial_mahasiswa_list.html',{
				'mahasiswa_list':mahasiswa_list
			})
		else :
			context = {
				'mahasiswa':mahasiswa
			}
			data['html_form'] = render_to_string('dashboard/includes/partial_mahasiswa_hapus.html',context,request=request)
		return JsonResponse(data)
	else:
		return redirect('login')
