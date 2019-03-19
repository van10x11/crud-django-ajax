from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
	class Meta:
		model = Mahasiswa

		fields = '__all__'

		widgets = {
			'nim':forms.NumberInput(attrs={'placeholder':'Nim Mahasiswa'}),
			'nama':forms.TextInput(attrs={'placeholder':'Nama Mahasiswa'}),
			'jenis_kelamin':forms.Select(),
			'tempat_lahir':forms.TextInput(attrs={'placeholder':'Tempat Lahir'}),
			'tanggal_lahir':forms.DateInput(attrs={'type':'date'}),
			'agama':forms.Select(),
			'alamat':forms.Textarea(attrs={'placeholder':'Alamat'}),


		}