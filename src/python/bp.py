from grongier.pex import BusinessProcess

from msg import FhirRequest,OrgaRequest

from fhir.resources.organization import Organization
from fhir.resources.address import Address
from fhir.resources.contactpoint import ContactPoint


class ProcessCSV(BusinessProcess):

    def on_request(self, request):
        """
        If the bp receives an OrgaRequest,iIt creates a new Organization object, 
        fills it with the information from the request and sends it to the FhirClient

        If the request is a FhirRequest, it sends it to the FhirClient.
        
        :param request: The request object that was sent to the service
        :return: None
        """
        if isinstance(request, OrgaRequest):
            # Creates a new Organization and fill it with the information from request
            # This is the DataTransformation step
            organization = Organization()

            organization.name = request.organization.name

            organization.active = request.organization.active

            adress = Address()
            adress.country = request.organization.country
            adress.city = request.organization.city
            organization.address = [adress]

            telecom = ContactPoint()
            telecom.value = request.organization.value
            telecom.system = request.organization.system
            organization.telecom = [telecom]

            msg = FhirRequest()
            msg.resource = organization

            self.send_request_sync("Python.FhirClient", msg)
        
        if isinstance(request,FhirRequest):
            self.send_request_sync("Python.FhirClient", request)       

        return None
