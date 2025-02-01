from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Modalite, Appareiltype
from django.views.generic import TemplateView
import subprocess
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.utils.html import format_html
from django.contrib import messages
# from .forms import ModaliteForm

counter = 0

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")  
        password = request.POST.get("password")         
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('imagerie:index')
    return render(request, 'imagerie/signup.html')  

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")  
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('imagerie:index')
    return render(request, 'imagerie/login.html')   

def logout_user(request):
    logout(request)
    return redirect('imagerie:index') 

def index(request):
    return render(request,'imagerie/index.html',{})

def Ping3(request):
    print("on est dans le programme Ping3")
    # if request.method == 'POST':
    command = "./imagerie/management/commands/myscript.sh"
    print("---->  ", command)
    result = subprocess.run([command], shell=True, capture_output=True, text=True)
    html = "<html><body>Script  Output: %s</body></html>" %(result)
    return HttpResponse(html)
    # return render(request, 'imagerie/ping3.html', {} ) 

def pingip(request, ip):
    import ping3
    # print("ip ----> ", ip)    
    try:
        res = ping3.ping(ip, timeout=1)
        print(f"{ip}  ---->  {res} sec.                          ", flush=True, end="\r")
        if res:
            color = "color:#00FF00;"
            mesg = "ping OK"
            messages.success(request, 'ping OK !')
        else:
            color = "color:#FF0000;"
            mesg = "ping KO"
            messages.warning(request, 'ping KO !')
    except: 
        color = "color:#0000FF;"
        mesg = "Network is unreachable"
        messages.error(request, 'Network is unreachable !')
    messageping = format_html("<a style=%s>%s</a>" % (color, mesg ))
    # return render(request, 'imagerie/pingip.html', {'messageping': messageping, 'ip':ip, 'messages':[messages,]} ) 
    # return redirect('admin:imagerie_modalite_show')
    # return redirect("http://127.0.0.1:8000/admin/imagerie/modalite/")
    return redirect('/admin/imagerie/modalite/')
    # from django.utils.http import is_safe_url
    # is_safe_url('/admin/imagerie/modalite/')
    # print(" is_safe_url('/admin/imagerie/modalite/' : ", is_safe_url('/admin/imagerie/modalite/'))

def show_all_modalite(request):
    # modalites = Modalite.objects.prefetch_related('stores').all().order_by('id').all()
    # modalites = Modalite.objects.prefetch_related('stores').all().filter(appareil__nom = 'Scanner')
    modalites = Modalite.objects.prefetch_related('stores', 'printers', 'soft').select_related('appareil', 'appareiltype', 'vlan', 'pacs', 'worklist', 'service', 'loc').order_by('id')
    # print(Modalite.objects.select_related('appareil', 'appareiltype', 'vlan', 'pacs', 'worklist', 'service', 'loc').prefetch_related('stores', 'printers').all().order_by('id').query)
    # modalites = Modalite.objects.prefetch_related('stores', 'printers').all().filter(appareil__nom = 'Scanner').select_related('appareil', 'appareiltype', 'pacs', 'worklist', 'service', 'loc', 'net' )
    maliste=["test1", "test2", "test3", "test4"]
    # for modalite in modalites:   
    #     Stores = ', '.join([store.aet for store in modalite.stores.all()])
   
        # print(modalite.aet, "  ", modalite.port ,"  ", modalite.pacs, "  ", modalite.service, "  ", modalite.worklist, "  ", modalite.appareil, "  ", modalite.appareiltype, "  ", modalite.loc, "  ", modalite.net, "  ", modalite.stores.all())
        # print('stores:', ', '.join([store.nom for store in modalites.stores.all()]))
    return render(request, 'imagerie/show_all_modalite.html', {'modalites': modalites, 'maliste': maliste} ) 

#def edit_modalite(request, id):
#    modalite = get_object_or_404(Modalite, id=id)
#    if request.method == "POST":
#        form = ModaliteForm(request.POST, instance=modalite)
#        if form.is_valid():
#            modalite = form.save(commit=False)
#            modalite.save()
#            return redirect('show_all_modalite')
#    else:
#        form = ModaliteForm(instance=modalite)
#    return render(request, 'imagerie/edit_modalite.html', {'form': form})
    

def show_modalite(request, id):
    modalite = get_object_or_404(Modalite, id=id)
    return render(request, 'imagerie/show_modalite.html', {'modalite': modalite})
    # return render(request, 'imagerie/show_modalite.html', {'form': form})
    
def detail_modalite(request, id):
    modalite = get_object_or_404(Modalite, id=id)
    return render(request, 'imagerie/detail_modalite.html', {'modalite': modalite})
    
def show_appareiltype(request, id):
    appareiltype = get_object_or_404(Appareiltype, id=id)
    form = Appareiltype()
    return render(request, 'imagerie/show_appareiltype.html', {'form': form})

def delete_modalite(request, id):
    modalite = get_object_or_404(Modalite, id=id)
    print("modalite.delete()")
    # modalite.delete()
    # return render(request, 'imagerie/xxxx.html', {'form': form})
    return redirect('show_all_modalite')


def test(request):
    modalites = Modalite.objects.all()
    # if request.method == "POST":
    #     form = ModaliteForm(request.POST)
    #     if form.is_valid():
    #         modalite = form.save(commit=False)
    #         modalite.save()
    #         return redirect('test')
    # else:
    #     form = ModaliteForm()
    #     # form =ModaliteForm()
    
    return render(request, 'imagerie/liste_modalites.html', {'modalites': modalites})


def get_message(request):
    return render(request, 'imagerie/message.html', {'message': "Hello, HTMX!"})


