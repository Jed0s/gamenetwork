from django.shortcuts import render
from .forms import WidgetForm

# Create your views here.
def widgets_view(request):
    widget = WidgetForm()
    context = {
        'widget': widget
    }
    return render(request, 'cool_stuff/widgets.html', context)