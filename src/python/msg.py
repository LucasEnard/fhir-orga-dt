
from grongier.pex import Message
from dataclasses import dataclass

from obj import BaseOrganization
from fhir.resources.organization import Organization

@dataclass
class OrgaRequest(Message):
    organization:BaseOrganization = None

@dataclass
class FhirOrgaRequest(Message):
    organization:Organization = None