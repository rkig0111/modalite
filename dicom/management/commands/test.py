from pydicom.uid import UID
from pynetdicom import AE
from pynetdicom.sop_class import CTImageStorage
from pynetdicom import AE, StoragePresentationContexts

ae = AE()
print(len(ae.requested_contexts))
ae.add_requested_context('1.2.840.10008.1.1')
ae.add_requested_context(UID('1.2.840.10008.5.1.4.1.1.4'))
print(len(ae.requested_contexts))
ae.add_requested_context(CTImageStorage)
print('CTImageStorage : ', CTImageStorage)
print(len(ae.requested_contexts))
print('ae.requested_contexts : ', ae.requested_contexts)
print()
for a in ae.requested_contexts:
    print(a)

# ae.requested_contexts = StoragePresentationContexts