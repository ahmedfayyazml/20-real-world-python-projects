from django.shortcuts import render
from .forms import ApplicationForm
from django.contrib import messages
from .models import Form

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)

            # clear the form after successful submission so it looks empty
            messages.success(request, "Form submitted successfully!")  # Optional
            form = ApplicationForm()

    else:
        # This runs for GET requests (initial page load)
        form = ApplicationForm()

    # This line is crucial! It renders the template with the form
    return render(request, "index.html", {"form": form})