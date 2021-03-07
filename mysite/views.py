from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    
    #check checkbox value
    removepunc = request.POST.get('removepunc','off')
    capatalize = request.POST.get('captalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')
    
    #check checkbox value is on or not
    if (removepunc == "on"):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation','analyzed_text':analyzed}
        
        djtext = analyzed
        
    
    if (capatalize == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Captalized','analyzed_text':analyzed}
        
        djtext = analyzed
        
    
    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        
        params = {'purpose':'New Line Removed','analyzed_text':analyzed}
        
        djtext = analyzed
        
        
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
                
        params = {'purpose':'Extra Space Removed','analyzed_text':analyzed}
        
        djtext = analyzed
        
    
    if (charcounter == "on"):
        counter = 0
        for char in djtext:
            counter = 1 + counter
        params = {'purpose':'Your character count is below','analyzed_text':counter}
  
    if (removepunc != "on" and capatalize != "on" and newlineremove != "on" and extraspaceremover != "on" and  charcounter != "on"):
        
        return HttpResponse("Please select any mode of operation to be performed.")
    
    
    return render(request, 'analyze.html', params)
