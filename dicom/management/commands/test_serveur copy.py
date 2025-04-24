

import logging
import time

from pynetdicom import AE, evt, debug_logger
from pynetdicom.sop_class import Verification

debug_logger()
LOGGER = logging.getLogger('pynetdicom')

def handle_open(event):
    """Print the remote's (host, port) when connected."""
    msg = 'Connected with remote at {}'.format(event.address)
    LOGGER.info(msg)

def handle_close(event):
    """Print the remote's (host, port) when disconnected."""
    msg = 'Disconnected from remote at {}'.format(event.address)
    LOGGER.info(msg)

handlers = [(evt.EVT_CONN_OPEN, handle_open)]

ae = AE()
ae.add_supported_context(Verification)
scp = ae.start_server(("127.0.0.1", 11112), ae_title='KIG_SCP', block=False, evt_handlers=handlers)

time.sleep(20)

scp.unbind(evt.EVT_CONN_OPEN, handle_open)
scp.bind(evt.EVT_CONN_CLOSE, handle_close)

LOGGER.info("Bindings changed")

time.sleep(20)

scp.shutdown()