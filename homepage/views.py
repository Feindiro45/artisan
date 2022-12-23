from django.shortcuts import render, redirect
from .models import DernierPublication, Imagepricipale, Entete, Menbre, Blog
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    product = DernierPublication.objects.all()
    product1 = Imagepricipale.objects.all()
    product2 = Entete.objects.all()
    product3 = Menbre.objects.all()
    paginator = Paginator(product, 3)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    context = {
        'product':product,
        'product1':product1,
        'product2':product2,
        'product3':product3
    }
    return render(request,'base.html', context)


def list_techniciens(request):
    return render(request,'list-tech.html')

def blog(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog,1)
    page = request.GET.get('page')
    blog = paginator.get_page(page)
    context = {
        'blog': blog
    }
    return render(request,'blog.html', context)

def contact(request):
    
    if request.method == 'POST':  
      form = ContactForm(request.POST)
      
      if form.is_valid():
          name = form.cleaned_data['name']
          email = form.cleaned_data['email']
          subject = form.cleaned_data['subject']
          content = form.cleaned_data['content']
          
          
          html = render_to_string('emails/contactform.html', {
              'name': name,
              'email': email,
              'subject' : subject,
              'content': content
          })
          
          send_mail(subject, 'This is the message', email, ['codewithtestein@gmail.com'], html_message=html)
          
          return redirect('contact')
    else:
        form = ContactForm()
          
          
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def don(request):
    return render(request,'don.html')

def handel404(request, exception):
    return render(request, '404.html')