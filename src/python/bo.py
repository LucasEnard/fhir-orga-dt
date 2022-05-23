from grongier.pex import BusinessOperation

from msg import FhirRequest

from fhirpy import SyncFHIRClient
from fhir.resources.organization import Organization

from fhir.resources import construct_fhir_element

import json

class FhirClient(BusinessOperation):

    def on_init(self):
        """
        It changes the current url and api-key if needed
        :return: None
        """
        if not hasattr(self,'url'):
            self.url = 'https://fhir.8ty581k3dgzj.static-test-account.isccloud.io'
        if not hasattr(self,'apikey'):
            self.apikey = "sVgCTspDTM4iHGn51K5JsaXAwJNmHkSG3ehxindk"

        self.client = SyncFHIRClient(url=self.url, extra_headers={"x-api-key":self.apikey})

        return None


    def on_fhir_request(self, request:FhirRequest):
        resource_type = request.resource["resource_type"]
        resource = construct_fhir_element(resource_type, request.resource)
        self.client.resource(resource_type,**json.loads(resource.json())).save()
        return None

    def on_message(self, request):
        return None