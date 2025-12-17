from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests
    Displays an individual instance of :model:`about.About`.
    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    **Template:**
    :template:`about/about.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            # The CollaborateRequest model was removed; do not attempt to save.
            # We still acknowledge the submission to the user. If you want to
            # persist requests later, replace this with email sending or
            # another storage mechanism.
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond within 2 working days.",
            )
            
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )