# This is not an auto-generated file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    txt = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        txt = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        txt = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in txt:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        txt = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(txt):
            if not (txt[index] == " " and txt[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        txt = analyzed

    if charcount == "on":
        analyzed = len(txt)
        params = {'purpose': 'Characters Count', 'analyzed_text': analyzed}
        # txt = analyzed

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse('Error... Something went wrong!!! Select at least one option.')

    return render(request, 'analyze.html', params)
