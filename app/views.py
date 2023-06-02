from django.shortcuts import render

# Create your views here.
# def conditionals(request):
#     d={'a':30}
#     return render(request,'conditionals.html',context=d)

# def conditionals(request):
#     d={'a':38,'b':32,'c':20}
#     return render(request,'conditionals.html',context=d)
def conditionals(request):
    d={'a':38,'b':32}
    return render(request,'conditionals.html',context=d)


# def loops(request):
#     d={'name':'bhavani'}
#     return render(request,'loops.html',context=d)
