from grongier.pex import BusinessOperation

from fhirpy import SyncFHIRClient
from fhir.resources.organization import Organization
from fhir.resources.resource import Resource

import json

class OperationCSV(BusinessOperation):

    def on_message(self, request):
        client = SyncFHIRClient(url='https://fhir.8ty581k3dgzj.static-test-account.isccloud.io', extra_headers={"x-api-key":"sVgCTspDTM4iHGn51K5JsaXAwJNmHkSG3ehxindk"})
        organization = Organization(**request.organization)
        client.resource(resource_type='Organization',**json.loads(organization.json())).save()
        return None