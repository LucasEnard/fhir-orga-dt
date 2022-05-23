from grongier.pex import BusinessService

from dataclass_csv import DataclassReader

from obj import BaseOrganization
from msg import OrgaRequest

import os

class ServiceCSV(BusinessService):

    def get_adapter_type():
        """
        Name of the registred adaptor
        """
        return "Ens.InboundAdapter"

    def on_init(self):
        """
        It changes the current path to the file to the one specified in the path attribute of the object,
        or to '/irisdev/app/misc/' if no path attribute is specified
        :return: None
        """
        if not hasattr(self,'path'):
            self.path = '/irisdev/app/misc/'
        if not hasattr(self,'filename'):
            self.filename = 'organization.csv'
        return None

    def on_tear_down(self):
        os.rename("/irisdev/app/misc/used/organization.csv", "/irisdev/app/misc/organization.csv")
        return None

    def on_process_input(self,request):
        """
        It reads the organization.csv file, creates an OrgaRequest message for each row, and sends it to
        the Python.Router process.
        
        :param request: the request object
        :return: None
        """
        with open(self.path + self.filename,encoding="utf-8") as orga_csv:
            reader = DataclassReader(orga_csv, BaseOrganization,delimiter=";")
            for row in reader:
                msg = OrgaRequest()
                msg.organization = row
                self.send_request_sync('Python.ProcessCSV',msg)

        os.rename("/irisdev/app/misc/organization.csv", "/irisdev/app/misc/used/organization.csv")

        return None

