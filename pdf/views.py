from django.shortcuts import render
from django.views.generic.edit import FormView
from pdf.forms import AccessCodeForm
from pdf.models import AccessCode, AccessCodeTracking
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


class AccessCodeView(FormView):
    template_name = "access_code_form.html"
    form_class = AccessCodeForm
    
    def form_valid(self, form):
        object = AccessCode.objects.get(code=form.get_access_code().upper())

        if not object.user.is_superuser:
            object.user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(self.request,object.user)
            access_code_tracking = AccessCodeTracking(access_code=object, action="access")
            access_code_tracking.save()
            
            return redirect("/console")
        else:
            return redirect("/enter")

@login_required(login_url='/enter/')
def console(request):
    context = {}
    return render(request, 'console.html', context)
    

@login_required(login_url='/enter/')
def book_detail(request, book_id):
    context = {"book": book_id, "book1_count": range(1,12), "book2_count": range(1,13)}
    return render(request, 'book_detail.html', context)