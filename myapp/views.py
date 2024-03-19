from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# class Index(View):
#     def get(seft, req):
#         return render(req, "index.html")
class Index(View):
    def get(seft, req):
        soa = 0
        sob = 0
        if req.GET:
            soa = req.GET.get('sothunhat')
            sob = req.GET.get('sothuhai')

        context = {
            'tong': int (soa) + int (sob)
        }
        return render(req, "index.html", context)
    def post (seft,req):
        soa = 0
        sob = 0
        if  req.POST:
            soa = req.POST.get('sothunhat')
            sob = req.POST.get('sothuhai')
        
        context = {
            'tong' : int(soa) + int (sob)
        }
        return render (req,"index.html", context)
