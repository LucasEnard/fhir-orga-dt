
from grongier.pex import Message
from dataclasses import dataclass

from obj import BaseOrganization

from fhir.resources.resource import Resource

@dataclass
class OrgaRequest(Message):
    organization:BaseOrganization = None

@dataclass
class FhirRequest(Message):
    resource:Resource = None