from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def indexpage(request):
    # categories = Category.objects.all()
    # items = {category.id: Product.objects.filter(category=category) for category in categories}
    # items = Product.objects.all()
    categories = Category.objects.prefetch_related('products').all()
    context = {
        'categories': categories,
        
    }
    return render(request, 'index.html', context)

# def view_brochure(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if product.brochure:
#         with open(product.brochure.path, 'rb') as f:
#             response = HttpResponse(f.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'inline; filename="{}"'.format(product.brochure.name)
#             return response
#     else:
#         return HttpResponse("No brochure available for this product.")


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def contactpage(request):
    return render(request, 'contact.html')

def teampage(request):
    return render(request, 'team.html')

def productpage(request):
    return render(request, 'productsDetails.html')

def jobpostpage(request):
    return render(request, 'post.html')

def jobpage(request):
    return render(request, 'alljob.html')

def saveEnquiry(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        # Save the data to the database
        en = contactInfo(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, message=message)
        en.save()
        
        email_message = f"First name: {first_name}\nLast name: {last_name}\nEmail: {email}\nPhone number: {phone_number}\nMessage: {message}"
        
        # Send an email
        send_mail(
            'New Contact Enquiry',
            email_message,
            'sw-fazla.rabby@networld-bd.com',
            ['info@networld-bd.com'],
            fail_silently=False,
        )
        
       
    
    # For GET request, render the contact form
    return render(request, "contact.html")

