from django.http import HttpResponse
# from django.shortcuts import render
#
# def index(request):
#     return render(request,'index.html')
#     # return HttpResponse("Hello World!!")


#################################################################
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
#
# def removepunc(request):
#     t=request.GET.get('text','default')
#     print(t)
#     return HttpResponse("Remove punc")
#################################################################


# def analyze(request):
#     tt= request.GET.get('text','default')
#     removepunc = request.GET.get('removepunc','off')
#     fullcaps = request.GET.get('fullcaps','off')
#     newlineremover = request.GET.get('newlineremover','off')
#     extraspaceremover = request.GET.get('extraspaceremover','off')
#
#     if removepunc == 'on':
#         punctuations = '''!()-[]{};:'"\,<>./.?@#$%^&*_~'''
#         analyzed = ""
#         for char in tt:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose':'Removed Punctuations' , 'analyzed_text': analyzed }
#     # return HttpResponse("remove punc")
#         return render(request,'analyze.html',params)
#
#     elif(fullcaps == 'on'):
#         analyzed = ""
#         for char in tt:
#             analyzed = analyzed + char.upper()
#
#         params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
#         # return HttpResponse("remove punc")
#         return render(request, 'analyze.html', params)
#
#     elif(newlineremover == 'on'):
#         analyzed = ""
#         for char in tt:
#             if char != "\n":
#                 analyzed = analyzed + char.upper()
#         params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
#         # return HttpResponse("remove punc")
#         return render(request, 'analyze.html', params)
#
#     elif(extraspaceremover == 'on'):
#         analyzed = ""
#         for index, char in enumerate(tt):
#             if not (tt[index] == " " and tt[index+1] == "  "):
#                 analyzed = analyzed + char
#         params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
#         # return HttpResponse("remove punc")
#         return render(request, 'analyze.html', params)

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

##################<TRAVEL TO END POINTS>#######################
# def facebook(request):
#     return HttpResponse('''<a href="https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C550525804944%7Ce%7Cfacebook%7C&placement=&creative=550525804944&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696220912%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-1001394929%26loc_physical_ms%3D9302130%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQjwntCVBhDdARIsAMEwACk5CCc6fqPyqXzARhbIFHmEtXw_0ESP0BWfqr6tTa3_gNY7BSdSzZIaAguQEALw_wcB">facebook</a>''')
#
# def instagram(request):
#     return HttpResponse('''<a href="https://www.instagram.com/?hl=en">instagram</a>''')


# def removepunc(request):
#     djtext = (request.GET.get('text','default'))
#     print(djtext)
#     return HttpResponse("Remove Punctuation")
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("new line remover")
# def spaceremover(request):
#     return HttpResponse("space remover")
# def charcount(request):
#     return HttpResponse("count the character")

####################################################################################################


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext= request.GET.get('text','default')
    removepunc= request.GET.get('removepunc','default')
    fullcaps = request.GET.get('fullcaps','default')
    newlineremover = request.GET.get('newlineremover','default')
    extraspaceremover = request.GET.get('extraspaceremover','default')
    charcount = request.GET.get('charcount','default')
    print(djtext)

    # Remove the punctuation:-
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation','analyzed_text':analyzed}

        return render(request,'analyze.html',params)

    #Changed to uppercase
    elif fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    #newline remover
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !='/n' and char != '/r':
                analyzed=analyzed+char
        params = {'purpose':'new line remover','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    #remove extra space
    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove the extra space', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)

    #character count
    elif charcount == 'on':
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose':'count the character','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("<h1>Error 404 page not found</h1> ")
