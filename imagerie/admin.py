from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import MUser
from imagerie.models import Appareil, Marque, Appareiltype, Vlan, Etablissement, Service, Connection  # , Testlan
from imagerie.models import Modalite, Localisation, Contact, Soft, Bdd, Ras, Resspartage, Identifiant, Projet, Hard
from django.utils.translation import gettext as _

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

class AppareiltypeAdmin(admin.ModelAdmin):
    list_display = ('nom',)

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

#class NetAdmin(admin.ModelAdmin):
#    # inlines = [ModaliteLine, ServeurLine ]
#    inlines = [ModaliteLine ]
#    fieldsets = [
#    ('Net Details', {'fields': [ 'addrip', 'macaddr', 'vlan', 'mask', 'gw', 'dns1', 'dns2', 'dhcp']}),
#    #('Net Dates', {'fields': ['', '', '']}),
#    ]
#
#    # addrip, hostname, macaddr, vlan, mask, gw, dns1, dns2, dhcp
#
#    # readonly_fields = ('datecreat',)
#    list_display = ('addrip', 'macaddr', 'hostname','vlan')
#    # list_editable = ('appareil',)
#    # list_display_links = ('addrip', 'macaddr')
#    # list_filter = ('addrip',)
#    # search_fields = ['appareil', 'appareiltype'] 


# col = [addrip, aet, port, mask, hostname, modalite, hostname, systeme, macadresse, dicom, inventaire \
# remarque, appareil, etablissement, localisation, marque, typeappareil, vlan ]

"""class VlanFilterSearchForm(admin.SimpleListFilter):
    title = _('Vlan')
    parameter_name = 'vlan'
    # template = 'admin/vlan_search_filter.html'

    def lookups(self, request, model_admin):
        # Get a list of vlans for the dropdown
        vlans = [(str(vlan.id), vlan.nom) for vlan in Vlan.objects.all()]
        # Add an option for "All" at the beginning
        # vlans.insert(0, ('', _('All')))
        print('vlans :  ', vlans)
        return vlans

    def queryset(self, request, queryset):
        vlan_id = self.value()
        print('vlan_id  :  ', vlan_id)
        modalite = Modalite.objects.all()
        if vlan_id:
            return queryset.filter(vlan__id=vlan_id)

    def choices(self, changelist):
        super().choices(changelist)
        return (
            *self.lookup_choices,
        )"""

class ModaliteAdmin(admin.ModelAdmin):
    # list_select_related = ["net", "appareil", "appareiltype"]

    list_display = ('addrip', 'aet', 'port', 'appareil', 'appareiltype', 'pacs', 'worklist', 'service', 'vlan', 'macaddr' )    
    # list_editable = ('appareil', 'appareiltype')
    list_filter= ('reforme', 'serveur', 'vlan' ) # , 'appareil'
    list_display_links = (
        'aet',
        'appareil',
        'appareiltype',
        'addrip',
    )
    autocomplete_fields = ('vlan',)

    # list_filter = [VlanFilterSearchForm, 'appareil']   # , 'net__vlan__nom'

    search_fields = (
        'aet',
        'appareil__nom',
        'appareiltype__nom',
        'hostname',
        'addrip',
        'macaddr',
        'vlan__nom',
    )

"""addrip, aet, appareil, appareil_id, appareiltype, appareiltype_id, dhcp, dns1, dns2, gw, hostname, id, loc, loc_id, macaddr, mask, modalite_pacs, modalite_printers, modalite_stores, modalite_worklist, pacs, pacs_id, port, printers, serveur, service, service_id, stores, vlan, vlan_id, worklist, worklist_id"""


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
