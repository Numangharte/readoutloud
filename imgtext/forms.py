from django.forms import ModelForm
from .models import imgFile

class ImageForm(ModelForm):
    class Meta:
        model = imgFile
        fields = '__all__'