import os

from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import imgFile
from PIL import Image
from gtts import gTTS
import pytesseract
import os
# Create your views here.
def new(request):
    return render(request, 'new.html')
def home(request):
    if request.method == "POST":
        image = request.FILES['images']
        images = imgFile(imgs=image)
        images.save()
        pytesseract.pytesseract.tesseract_cmd ='static/Tesseracr-OCR'
        img =pytesseract.image_to_string(Image.open(image),lang='hin')
        print(img)
        speech =gTTS(text=img, lang='hi', slow=False)
        speech.save("static/hindi/voice.mp3")
        context = {'imgs': img}

        return render(request,'home.html',context)

    return render(request,'home.html')
def english(request):
    if request.method == "POST":
        image = request.FILES['images']
        images = imgFile(imgs=image)
        images.save()
        pytesseract.pytesseract.tesseract_cmd = 'static/Tesseracr-OCR'

        img =pytesseract.image_to_string(Image.open(image))
        print(img)
        speech =gTTS(text=img, lang='en', slow=False)
        speech.save("static/english/voice.mp3")
        context = {'imgs': img}

        return render(request,'english.html',context)

    return render(request,'english.html')
