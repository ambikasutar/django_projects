from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    input_txt = request.GET.get('input_txt', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    removeextraspace = request.GET.get('removeextraspace', 'off')
    fullcap = request.GET.get('fullcap', 'off')    
    action_on_txt = []

    #if no action select then show error
    if removepunc == "off" and removeextraspace =='off' and fullcap=='off':
        return HttpResponse("No action is selected.")
    else: #if selected option then perform action
        
        #if remove punctuation action is selected
        if removepunc == 'on':
            final_txt  = ""
            puncList = '''<>,*\():,{-}"";'...!_?/[]'''
            action_on_txt.append("removepunc")
            for char in input_txt:
                if char not in puncList:
                    final_txt = final_txt + char  

        #if remove extra space action is selected
        if removeextraspace =='on' :
            action_on_txt.append("removeextraspace")
            if ('final_txt' in locals()) and final_txt !="":
                input_txt = final_txt
            final_txt = ''        
            final_txt = input_txt.replace("  ", " ")

        #if uppercase action is selected
        if fullcap=='on':
            action_on_txt.append("fullcap")
            if ('final_txt' in locals()) and final_txt !="":
                input_txt = final_txt
            final_txt = ''
            for char in input_txt:
                final_txt = final_txt + char.upper()
        
        #render to analyze page with params value
        params = {'input_txt':input_txt,'action_on_txt': action_on_txt,'final_txt':final_txt}
        return render(request, 'analyze.html', params)
    
    
