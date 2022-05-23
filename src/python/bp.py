from grongier.pex import BusinessProcess

from msg import FhirOrgaRequest

import json

from fhir.resources.organization import Organization
from fhir.resources.address import Address
from fhir.resources.contactpoint import ContactPoint


class ProcessCSV(BusinessProcess):

    def on_request(self, request):

        # Create a new Organization and fill it with the information from request
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

        msg = FhirOrgaRequest()
        msg.organization = organization

        self.send_request_sync("Python.OperationCSV", msg)

        return None
