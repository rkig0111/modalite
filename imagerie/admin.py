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

class TousLesServeursListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("tous les serveurs")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "serveur"

    def lookups(self, request, model_admin):
        print("request : ", request)
        print("model_admin : ", model_admin)
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
        if self.value()== 'SE':
            print("self.value() : ",  self.value())
            return queryset.filter().exclude(serveur='PC').exclude(serveur='NA').exclude(serveur='PR').exclude(serveur='OT')
        elif self.value() in ['IN', 'PC', 'NA', 'PA', 'WL', 'DA', 'ST', 'PR', 'OT']:            
            return queryset.filter(serveur=self.value())
        else:
            return queryset


class ModaliteAdmin(admin.ModelAdmin):
    # list_select_related = ["net", "appareil", "appareiltype"]

    list_display = ('hostname', 'colored_addrip', 'aet', 'port', 'appareil', 'appareiltype', 'pacs', 'worklist', 'service', 'vlan', 'macaddr')    
    ordering = ('addrip',)
    # list_editable = ('appareil', 'appareiltype')

    # list_filter = [VlanFilterSearchForm, 'appareil']   # , 'net__vlan__nom'
    list_filter= ['reforme', 'ping', TousLesServeursListFilter, 'vlan' ] # , 'serveur', 'vlan'  , 'appareil'
    
    list_display_links = (
        'aet',
        'appareil',
        'appareiltype',
        'colored_addrip',
    )
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

    """def pagar_pase(modeladmin, request, queryset):
        'Does something with each objects selected '
        selected_objects = queryset.all()
        
        for i in selected_objects:
            # return '''<form action="." method="post">Action</form> '''
            print(i.addrip)
            # do something with i

    pagar_pase.short_description = "Testing form output"
    pagar_pase.allow_tags = True

    actions = ["pagar_pase"]"""




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
