from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class loginform(forms.Form):
    username = forms.CharField(max_length=100,label='Adınız')
    password = forms.CharField(max_length=20,widget=forms.PasswordInput,label='Şifrəniz')



    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('Şifrəniz və ya Adınız Səhvdir!')
            return super(loginform,self).clean()




class registerform(forms.ModelForm):
    username = forms.CharField(max_length=100,label='Adınız')
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput,label='Şifrəniz')
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput,label='Şifrəniz(Təkrar)')
    

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Şifrələr eyni deyil!')
        return password2





# class RegisterForm(forms.ModelForm):
#     username = forms.CharField(max_length=100, label='Kullanıcı Adı')
#     password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password1',
#             'password2',
#         ]

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Şifreler eşleşmiyor!")
#         return password2
