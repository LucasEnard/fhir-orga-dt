from grongier.pex import BusinessOperation

from msg import FhirRequest

from fhirpy import SyncFHIRClient
from fhir.resources import construct_fhir_element

import json

class FhirClient(BusinessOperation):
    client: SyncFHIRClient = None

    def on_init(self):
        """
        It changes the current url if needed using the params of the
        management portal

        :return: None
        """
        if not hasattr(self,'url'):
            self.url = 'http://localhost:52773/fhir/r4'

        self.client = SyncFHIRClient(url=self.url,extra_headers={"Content-Type":"application/json+fhir"})

        # Using an InterSystems server that need an api key, using the header x-api-key
        #self.client = SyncFHIRClient(url='https://fhir.8ty581k3dgzj.static-test-account.isccloud.io', extra_headers={"x-api-key":"sVgCTspDTM4iHGn51K5JsaXAwJNmHkSG3ehxindk"})

        return None


    def on_fhir_request(self, request:FhirRequest):
        """
        > When a FHIR request is received, create a FHIR resource from the request,
        and save it to the FHIR server. It can be any resource from the FHIR R4
        specification in a dict format.
        
        :param request: The FHIR request object
        :type request: FhirRequest
        :return: None
        """
        # Get the resource type from the request ( here "Organization" )
        resource_type = request.resource["resource_type"]

        # Create a resource of this type using the request's data
        resource = construct_fhir_element(resource_type, request.resource)

        # Save the resource to the FHIR server using the client
        self.client.resource(resource_type,**json.loads(resource.json())).save()

        return None

    def on_message(self, request):
        return None