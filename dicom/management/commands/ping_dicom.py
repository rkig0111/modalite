from django.core.management.base import BaseCommand
from imagerie.models import Modalite
from modalite.settings import BASE_DIR
from django.utils import timezone
from pathlib import Path
from dicom.management.commands.echoscu import echoscu
from pynetdicom import AE, evt, debug_logger
from pynetdicom.sop_class import Verification
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
        
    args = ''
    help = " utilitaire pour faire un test DICOM sur les modalités désignées  \
        on prend comme AET celui de notre PACS et nous faisons une <vérification>  sur l' AET désignée "
    
    def horodat(self):
        return timezone.now().strftime('%Y/%m/%d, %H:%M:%S')

    def handle(self, *args, **options):
                
        '''AET_SCP = "EE2006194AMIP"
        PORT_SCP = 11112
        IP_SCP = "172.19.32.28"'''
        
        AET_SCU = "KIG-SCU"        
        AET_SCP = "KIG-SCP"
        PORT_SCP = 11112
        IP_SCP = "127.0.0.1"
        
              
        def handle_open(event):
            """Print the remote's (host, port) when connected."""
            msg = 'Connected with remote at {}'.format(event.address)
            print("# LOGGER.info(msg)  :  ", msg)
            logger.info(msg)
            # logger(msg, 'debug', 'modlite')
            
        def handle_accepted(event, arg1, arg2):
            """Demonstrate the use of the optional extra parameters"""
            print("# LOGGER.info('Extra args: '{}' and '{}''.format(arg1, arg2))")
            # logger.info(f"Extra args: {arg1} and {arg2}")
            # logger(f"Extra args: {arg1} and {arg2}", 'debug', 'modalite')
            
        # If a 2-tuple then only `event` parameter
        # If a 3-tuple then the third value should be a list of objects to pass the handler
        handlers = [
            (evt.EVT_CONN_OPEN, handle_open),
            # (evt.EVT_ACCEPTED, handle_accepted, ['optional', 'parameters']),
        ]
        # ae = AE(ae_title="IMA0209")
        ae = AE(ae_title=AET_SCU)
        ae.add_requested_context(Verification)
        # assoc = ae.associate("172.19.32.28", 11112, ae_title='EE2006194AMIP', evt_handlers=handlers)
        assoc = ae.associate(IP_SCP, PORT_SCP, ae_title=AET_SCP, evt_handlers=handlers) 
        
        try:
            resp = assoc.send_c_echo(1)
            print(f'Modality responded with status: {resp.Status}')
            logger.info(f'Modality responded with status : {resp.Status}')
            assoc.release()
            # recup_info()
        except Exception as e:
            assoc.release()
            raise e
    
 
                    