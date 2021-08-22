from io import BytesIO

import qrcode
from django.core.files import File
from django.db import models
from django.shortcuts import redirect, render
from PIL import Image, ImageDraw

from .forms import ClientForm
from .models import Client, Info


def client_list(request):
    clients = Client.objects.all()
    return render(request, "list.html", {"clients": clients})

def detail(request, id):
    client = Client.objects.get(id=id)
    info = Info.objects.first()
    return render(request, f"{client.qayerga.lower()}.html", {"client": client, "info": info})

def new_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save(commit=False)
            # cd = form.cleaned_data
            # qrcode_img = qrcode.make(f"http://172.20.10.2:8000/people/{cd['id']}")
            # canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
            # draw = ImageDraw.Draw(canvas)
            # canvas.paste(qrcode_img)
            # fname = f"{cd['full_name']}.png"
            # buffer = BytesIO()
            # canvas.save(buffer, 'PNG')
            # qrcode.save(fname, File(buffer), save=False)
            # canvas.close()
            # form.save()
            return redirect('/people/')
    else:
        form = ClientForm()
    return render(request, "forma.html", {"form": form})
