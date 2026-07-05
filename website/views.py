from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm
from django.http import HttpResponse


def home(request):

    form = ContactForm()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                send_mail(
                    subject=f"Portfolio Contact from {name}",
                    message=f"""
        📩 New Portfolio Contact

        👤 Name: {name}
        📧 Email: {email}

        💬 Message:
        {message}
        """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent successfully!")
                return redirect("home")

            except Exception as e:
                return HttpResponse(str(e))
        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")

    return render(
        request,
        "home.html",
        {
            "form": form,
        },
    )