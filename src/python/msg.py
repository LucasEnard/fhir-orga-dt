from grongier.pex import Message
from dataclasses import dataclass

from obj import BaseOrganization, BasePatient

from fhir.resources.resource import Resource

# Here you can add your own classes like PatientRequest, ObservationRequest, etc
# to prepare a new DataTransformation

@dataclass
# > The OrgaRequest class is a Message class that has an organization attribute
# that is a BaseOrganization class ( see the obj.py file and the BaseOrganization
# class).
class OrganizationRequest(Message):
    resource:BaseOrganization = None

@dataclass
class PatientRequest(Message):
    resource:BasePatient = None

@dataclass
# > The FhirRequest class is a Message class that has an resource attribute 
# that is a Resource class ( see the fhir.resources.resource.py file and the
#  Resource class).
# It can be an Organization, a Patient or any other FHIR R4 resource.
class FhirRequest(Message):
    resource:Resource = None