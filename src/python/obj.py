from dataclasses import dataclass

@dataclass
class BaseOrganization:
    active:bool = None
    name:str = None
    id:int = None
    city:str = None
    country:str = None
    system:str = None
    value:str = None
