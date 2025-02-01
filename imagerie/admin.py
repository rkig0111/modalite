from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import MUser
from imagerie.models import Appareil, Marque, Appareiltype, Vlan, Etablissement, Service, Connection  # , Testlan
from imagerie.models import Modalite, Localisation, Contact, Soft, Bdd, Ras, Resspartage, Identifiant, Projet, Hard
from django.utils.translation import gettext as _
#from django.db.models import Q
from django.contrib import messages
from django.utils.translation import ngettext
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from django.utils.html import format_html
import ping3
import logging
logger = logging.getLogger(__name__)

# class MUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         ('Extra', {'fields': ('is_premium', 'good_reputation')}),
#     )

class AppareilAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('code',)

class MarqueAdmin(admin.ModelAdmin):
    list_display = ('nom',)

# class AppareiltypeAdmin(admin.ModelAdmin):
#     list_display = ('nom',)

class AppareiltypeAdmin(admin.ModelAdmin):
    list_display = ( "nom",)    

class VlanAdmin(admin.ModelAdmin):
    list_display = ('nom','num', 'divers')
    search_fields = ('nom', 'num')

class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    
class IdentifiantAdmin(admin.ModelAdmin):
    list_display = ('login',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class RasAdmin(admin.ModelAdmin):
    list_display = ('denom',)
    
class ResspartageAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class BddAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    
class SoftAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class HardAdmin(admin.ModelAdmin):
    list_display = ('description',)
     
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class ModaliteLine(admin.StackedInline):
    model = Modalite
    extra = 0

class TousLesServeursListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("tous les serveurs")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "serveur"

    def lookups(self, request, model_admin):
        # print("request : ", request)
        return [
            ("SE", "INF+PACS+STORE+WL+DACS"),
            ("IN", "INFORMATIQUE"),
            ("PC", "ORDINATEUR"), 
            ("NA", "N/A"),
            ("PA", "DICOM PACS"),
            ("WL", "DICOM WORKLIST"),
            ("DA", "DICOM DACS"),
            ("ST", "DICOM STORE"),
            ("PR", "DICOM PRINT"),
            ("OT", "DICOM OTHER"),                       
        ]

    def queryset(self, request, queryset):
        # print("request : ", request)
        # print("queryset : ", queryset)
        if self.value()== 'SE':
            return queryset.exclude(serveur='PC').exclude(serveur='NA').exclude(serveur='PR').exclude(serveur='OT')
        elif self.value() in ['IN', 'PC', 'NA', 'PA', 'WL', 'DA', 'ST', 'PR', 'OT']:            
            return queryset.filter(serveur=self.value())
        else:
            return queryset


class ModaliteAdmin(admin.ModelAdmin):
    list_select_related = ["vlan", "appareil", "appareiltype", 'pacs', 'worklist', 'service']
    # list_prefetch_related   pour les tables many to many 
    
    # list_display = ('aet', 'hostname', 'colored_addrip', 'appareil_link', 'appareiltype_link', 'port', 'pacs', 'worklist', 'service', 'macaddr')   #  'vlan'
    list_display = ('aet', 'hostname', 'colored_addrip', 'appareil', 'appareiltype', 'port', 'pacs', 'worklist', 'service', 'macaddr')
    ordering = ('addrip',)
    # list_editable = ('appareil', 'appareiltype')

    # list_filter = [VlanFilterSearchForm, 'appareil']   # , 'net__vlan__nom'
    list_filter= ['reforme', 'ping', TousLesServeursListFilter, 'vlan' ] # , 'serveur', 'vlan'  , 'appareil'

    """list_display_links = (
        'aet',
        'appareil',
        'appareiltype', 
        'colored_addrip',
    )"""

    autocomplete_fields = ('vlan',)

    search_fields = (
        'aet',
        'appareil__nom',
        'appareiltype__nom',
        'hostname',
        'addrip',
        'macaddr',
        'vlan__nom',
    )

    """def appareiltype_link(self, obj):
        if obj.appareiltype:
            url = reverse('admin:imagerie_appareiltype_change', args=[obj.appareiltype.id])           
            link = '<a href="%s">%s</a>' % (url, obj.appareiltype.nom)
            # print("url ----> ", url)
            return mark_safe(link)
        return "N/A"

    appareiltype_link.short_description = 'Appareiltype'


    def appareil_link(self, obj):
        if obj.appareil:
            url = reverse('admin:imagerie_appareil_change', args=[obj.appareil.id])          
            link = '<a href="%s">%s</a>' % (url, obj.appareil.nom)
            # print("url ----> ", url)
            return mark_safe(link)
        return "N/A"

    appareil_link.short_description = 'Appareil'"""

    def select_addrip(modeladmin, request, queryset):
        'Does something with each objects selected '
        selected_objects = queryset.all()
        listip = []
        for i in selected_objects:
            listip.append((i.addrip, i.aet, i.hostname))
        setlistip = set(listip)
        print("setlistip : ", setlistip)
        listemsgping = []
        for modal in setlistip: 
            msgping = []
            ip = modal[0] if modal[0] else '---'
            aet = modal[1] if modal[1] else '---'
            hostname = modal[2] if modal[2] else '---'
            try:
                res = ping3.ping(ip, timeout=1)
                print(f"{ip}  ---->  {res} sec.                          ", flush=True, end="\r")
                if res:
                    color = "color:#00FF00;"
                    mesg = "ping OK"
            #         messages.success(request, 'ping OK !')
                else:
                    color = "color:#FF0000;"
                    mesg = "ping KO"
            #         messages.warning(request, 'ping KO !')
            except: 
                color = "color:#0000FF;"
                mesg = "Network is unreachable"
            #     messages.error(request, 'Network is unreachable !')
            msgeip = format_html(f"<a style={color}>{ip}</a>" )
            msgeaet = format_html(f"<a style={color}>{aet}</a>" )
            msgehost = format_html(f"<a style={color}>{hostname}</a>" )
            msgping.append(msgeip)
            msgping.append(msgeaet)
            msgping.append(msgehost)
            listemsgping.append(msgping)
            
        # print("listemesgping : ", listemsgping)
        return render(request, 'imagerie/pingip.html', {'listemsgping': listemsgping } )         

    select_addrip.short_description = "TESTS PING"
    select_addrip.allow_tags = True

    actions = ["select_addrip"]



# class TestlanAdmin(admin.ModelAdmin):
#     list_display = ('modalite',)

# admin.site.register(MUser, UserAdmin)
admin.site.register(Appareil, AppareilAdmin)
admin.site.register(Localisation, LocalisationAdmin)
admin.site.register(Marque, MarqueAdmin)
admin.site.register(Appareiltype, AppareiltypeAdmin)
admin.site.register(Vlan, VlanAdmin)
admin.site.register(Etablissement, EtablissementAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Identifiant, IdentifiantAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Ras, RasAdmin)
admin.site.register(Resspartage, ResspartageAdmin)
admin.site.register(Bdd, BddAdmin)
admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Soft, SoftAdmin)
admin.site.register(Hard, HardAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(Modalite, ModaliteAdmin)
# admin.site.register(Testlan, TestlanAdmin)
