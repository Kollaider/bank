from django.db.models import F
from django.shortcuts import render
from app.models import LoanApplication


def index(request):
    """View with getting context for HomePage"""
    loan_applications = LoanApplication.objects.all()
    return render(request, 'app/index.html', {'loan_application': loan_applications})


def loan_application(request, pk):
    """View for handling LaonApllication info"""
    uniq_man_pk = LoanApplication.objects.filter(pk=pk).\
        annotate(uniq=F('products__manufacturer__pk')).\
        exclude(uniq__isnull=True).\
        values('uniq')
    return render(request, 'app/index.html', {'uniq_man_pk': uniq_man_pk})

