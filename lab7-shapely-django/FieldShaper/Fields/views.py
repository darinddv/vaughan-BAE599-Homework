from django.shortcuts import render
from django.http import HttpResponse
from .forms import FieldForm
from .forms import FieldSelect
from .utils import shapely_module
# Create your views here.

def index(request):

    form = FieldForm()
    select = FieldSelect()
    if request.method == "POST":
        form = FieldForm(request.POST)
        select = FieldSelect(request.POST)
        coord1 = request.POST['poly_coord1']
        coord2 = request.POST['poly_coord2']
        coord3 = request.POST['poly_coord3']
        coord4 = request.POST['poly_coord4']
        if form.is_valid():
            form.save()
        
    context = {
                'form': form,
                'select':select,
                'plot_div': shapely_module.polygon()
              }

    url = "Fields/Fields.html"
    return render(request, url, context)