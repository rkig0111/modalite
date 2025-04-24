from pynetdicom import AE, build_context
from pynetdicom.sop_class import Verification

ae = AE()
ae.add_supported_context(Verification)

supported_cx = [build_context('1.2.840.10008.1.1')]
# Blocks
ae.start_server(("127.0.0.1", 11113), ae_title='STORE_SCP', contexts=supported_cx, block=True)

