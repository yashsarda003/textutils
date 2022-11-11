from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # By defaut index takes an arguement otherwise it throws an error
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    removeNum = request.POST.get('removeNum', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcap == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            'purpose': 'Changed to Upper Case',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            'purpose': 'New Line Removed ',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = len(djtext)
        params = {
            'purpose': 'N0. of Characters are:',
            'analyzed_text': analyzed
        }
    
    if(removeNum == "on"):
        analyzed = ''.join([i for i in djtext if not i.isdigit()])
        print("no num final string is: ",analyzed)
        params = {'purpose': 'Integer Removed', 'analyzed_text': analyzed}
        djtext = analyzed


    if (removepunc != "on" and newlineremover !="on" and extraspaceremover != "on" and fullcap != "on" and charcount != "on" and removeNum != "on"):
            return HttpResponse('''<h1> YOU HAVEN'T SELECTED ANY OPERATIONS PLEASE SELECT ANY OPERATION </h1>
        <a href = "/"> HOME </a>''')
    


    return render(request, 'analyze.html', params)




