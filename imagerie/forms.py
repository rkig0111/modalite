from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Modalite, Service
    
class ModaliteForm(forms.ModelForm):
    # modalite = forms.ModelChoiceField(queryset = Modalite.objects.prefetch_related('stores', 'printers').all().filter(appareil__nom = 'Scanner').select_related('appareil', 'appareiltype', 'net', 'pacs', 'worklist', 'service', 'loc'))  # , Label = "Modalité"
    # form.fields['modalite'].queryset = Service.objects.all().order_by('nom')

    class Meta:
        model = Modalite
        fields = ('aet', 'appareil', 'appareiltype', 'addrip', 'port', 'pacs', 'worklist', 'stores', 'printers', 'service', 'loc')    


class AppareiltypeForm(forms.ModelForm):

    class Meta:
        model = Appareiltype
        fields = ('nom', )