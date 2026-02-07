from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER

# Create your views here.
def contact(request):
        if request.method == 'POST':         #en este caso procesaremos el formulario
            form = ContactForm(request.POST) #aquí almacenamos los datos del formulario
            if form.is_valid(): #comprobamos que los datos del formulario son válidos
                cd = form.cleaned_data

                #enviaremos el email y redireccionamos
                email = EmailMessage (
                            'Nuevo mensaje de MISITIOWEB', # Asunto
                            'De {} <{}>\n\nMensaje:\n\n{}'.format(cd['name'], cd['email'], cd['content']), #Cuerpo
                            EMAIL_HOST_USER, #Origen (Mi servidor de correo)
                            ['mbarruti5@gmail.com'], #Destino(Para quien es el correo)
                            reply_to=[cd['email']], #email de respuesta(a quien hay que contestar)
                )
                try:
                    #raise Exception("Forzando fallo")  # <--- línea para probar fail
                    email.send()
                    #si todo va ok, redireccionamos a ?ok
                    return redirect(reverse('contact')+'?ok')
                except:
                    #si algo falla, redireccionamos a ?fail
                    return redirect(reverse('contact')+'?fail')
        else:
            form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})