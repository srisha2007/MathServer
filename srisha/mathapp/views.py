from django.shortcuts import render
def power(request):
    context = {}
    context['power'] = "0"
    context['i'] = "0"
    context['r'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        print('request.POST:', request.POST)
        i = request.POST.get('intensity', '0') 
        r = request.POST.get('resistance', '0') 
        print('intensity =', i)
        print('resistance =', r)
        power =  int(i) * int(i) * int(r)
        context['power'] = power
        context['i'] = i
        context['r'] = r
        print('Power =', power)
    
    return render(request, 'mathapp/math.html',context)