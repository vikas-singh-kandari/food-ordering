import os
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from .models import addshop as AddShop  # Importing the model class with a different name

def addshop(request):
    if request.method == "POST":
        data = request.POST
        shop_name = data.get('shop_name')
        shop_img = request.FILES.get('shop_img')  # Corrected field name
        shop_contact = data.get('shop_contact')
        shop_address = data.get('shop_address')
        # Save the data to the database
        new_shop = AddShop.objects.create(
            shop_name=shop_name,
            shop_img=shop_img,
            shop_contact=shop_contact,
            shop_address=shop_address
        )
        # Optionally, you can redirect to a different page or pass a success message
        return redirect("addshop")
    else:
        shops = AddShop.objects.all()
        return render(request, "addshop.html", {'shops': shops})

def delete_shop(request, id):
    try:
        shop = AddShop.objects.get(id=id)
        image_path = shop.shop_img.path
        shop.delete()
        if os.path.exists(image_path):
            os.remove(image_path)   
        else:
            print("not find")
    except Exception as e:
        print("Error occurred:", e)  # Debugging statement
    return redirect('addshop')
