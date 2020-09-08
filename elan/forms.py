from django import forms
from .models import elan

class elanform(forms.ModelForm):

    class Meta:
        model = elan
        fields = [
            'cixis_yeri',
            'catma_yeri',
            'cixis_vaxti',
            'catma_vaxti',
            'elaqe_nomresi',
            'elave_melumatlar',
            'sirket',
        ]

        labels = {
            'cixis_yeri':"Çıxış Yeri(Ölkə-Şəhər formatında olmalıdır)",
            'catma_yeri':"Çatma Yeri(Ölkə-Şəhər formatında olmalıdır)",
            'cixis_vaxti':"Çıxış Vaxtı",
            'catma_vaxti':"Çatma Vaxtı",
            'elaqe_nomresi':"Əlaqə Nömrəsi(Ölkə Kodu İlə Birlikdə Olmalıdır!)",
            'elave_melumatlar':"Əlavə Məlumatlar",
            'sirket':"Şirkət",
        }

        widgets = {
            'cixis_yeri': forms.TextInput(attrs = {'class':'form-control kendi','placeholder':'Ölkə-Şəhər','id':"exampleFormControlInput1"}),
            'catma_yeri': forms.TextInput(attrs = {'class':'form-control kendi','placeholder':'Ölkə-Şəhər'}),
            'cixis_vaxti': forms.DateInput(attrs = {'class':'Çıxış Vaxtı','type':'date'}),
            'catma_vaxti': forms.DateInput(attrs = {'class':'Çatma Vaxtı','type':'date'}),
            'elave_melumatlar': forms.Textarea(attrs = {'class':'form-control kendi','placeholder':'Əlave Məlumatlar(Vacib Deyil)','type':'text','id':'exampleFormControlTextarea1','rows':'6','columns':'2'}),
            'sirket': forms.TextInput(attrs = {'class':'form-control kendi','placeholder':'Şirkət(Vacib Deyil)','type':'text','id':'exampleFormControlTextarea1','rows':'6','columns':'2'}),
            'elaqe_nomresi': forms.NumberInput(attrs = {'class':'form-control kendi','placeholder':'Məsələn:+994xxxxxxxxx','id':"exampleFormControlInput1"}),
        }



