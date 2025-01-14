from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Modalite
from django.views.generic import TemplateView
import subprocess
# from .forms import ModaliteForm

counter = 0

def Ping(request):
    if request.POST:
        subprocess.run(['./imagerie/management/commands/myscript.sh'])

    return render(request,'imagerie/ping.html',{})

def Inc(request):
    global counter
    counter = counter + 1
    return HttpResponse("The counter is now set to " + str(counter))


def Ping2(request):
    print("on est dans le programme Ping2")
    if request.method == 'POST':
        command = "./imagerie/management/commands/myscript.sh"
        print("---->  ", command)
        try:
            result = subprocess.run([command], shell=True, capture_output=True, text=True)
            print(result.stdout)
            # process = subprocess.Popen(command, stdout=PIPE, stderr=STDOUT)
            output = process.stdout.read()
            exitstatus = process.poll()
            if (exitstatus==0):
                result = {"status": "Success", "output":str(output)}
            else:
                result = {"status": "Failed", "output":str(output)}
        except Exception as e:
            result =  {"status": "failed", "output":str(e)}
        html = "<html><body>Script  Output: %s</body></html>" %(result)
        # html = "<html><body>Script status: %s \n Output: %s</body></html>" %(result['status'],result['output'])
        # return HttpResponse(html)
        return render(request, 'imagerie/ping2.html', {} ) 


def Ping3(request):
    print("on est dans le programme Ping3")
    # if request.method == 'POST':
    command = "./imagerie/management/commands/myscript.sh"
    print("---->  ", command)
    result = subprocess.run([command], shell=True, capture_output=True, text=True)
    html = "<html><body>Script  Output: %s</body></html>" %(result)
    return HttpResponse(html)
    # return render(request, 'imagerie/ping3.html', {} ) 


def Ajax(request):
    #print(request.__dict__)
    print(request.META['REMOTE_ADDR'])
    string = request.GET['name']
    return HttpResponse("Bonjour %s!" % string)
    if request.method == "POST":
        #form = ModaliteForm(request.POST)
        #if form.is_valid():
        #    modalite = form.save(commit=False)
        #    modalite.save()
            return redirect('show_all_modalite')
    else:
        pass
        #form = ModaliteForm()
        # form =ModaliteForm()
    #return render(request, 'imagerie/delete.html', {'form': form})
    #print("on est dans le programme Ping3")
    # if request.method == 'POST':
    command = "./imagerie/management/commands/myscript.sh"
    #print("---->  ", command)
    result = subprocess.run([command], shell=True, capture_output=True, text=True)
    #print(result)
    result = ['test1', 'test2', 'test3']
    # html = "<html><body>Script  Output: %s</body></html>" %(result)
    return render(request, 'imagerie/ajax.html', {'result':result} ) 


def show_all_modalite(request):
    # modalites = Modalite.objects.prefetch_related('stores').all().order_by('id').all()
    # modalites = Modalite.objects.prefetch_related('stores').all().filter(appareil__nom = 'Scanner')
    modalites = Modalite.objects.prefetch_related('stores', 'printers', 'soft').select_related('appareil', 'appareiltype', 'vlan', 'pacs', 'worklist', 'service', 'loc').all().order_by('id')
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
    return render(request, 'imagerie/show_modalite.html', {'form': form})

def delete_modalite(request, id):
    modalite = get_object_or_404(Modalite, id=id)
    print("modalite.delete()")
    # modalite.delete()
    # return render(request, 'imagerie/xxxx.html', {'form': form})
    return redirect('show_all_modalite')


def test(request):
    modalite = Modalite.objects.get(id=106)
    pass
    # if request.method == "POST":
    #     form = ModaliteForm(request.POST)
    #     if form.is_valid():
    #         modalite = form.save(commit=False)
    #         modalite.save()
    #         return redirect('test')
    # else:
    #     form = ModaliteForm()
    #     # form =ModaliteForm()
    # return render(request, 'imagerie/delete.html', {'form': form})