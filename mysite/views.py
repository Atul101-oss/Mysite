from django.shortcuts import render
from . import utils

# Create your views here.
def index(request):
    context = {}
    return render(request, 'cards.html', context)

def removePunc(request):
    context={}
    if request.method == 'POST':
        original_text = request.POST.get('text')
        context['original_text'] = original_text
        context['Analysed_text'] = utils.remove_punctuation(original_text)

    return render(request, 'removePunc.html',context)