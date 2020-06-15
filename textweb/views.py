from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')

    remove_punctuation = request.POST.get('remove_punctuation','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    #clashes

    if remove_punctuation == 'on':
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        a = ''
        for char in djtext:
            if char not in punctuation:
                a += char
        params = {'purpose' : 'remove punctuation' ,'output' : a}
        djtext = a
        # return render(request,'analyze.html',params)

    if (capitalize == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'capitalize', 'output':analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed


    if (newlineremove=='on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'newlineremove', 'output': analyzed}
        djtext = analyzed
    # else:
    #     return HttpResponse("--ERROR--")

    return render(request, 'analyze.html',params)

    