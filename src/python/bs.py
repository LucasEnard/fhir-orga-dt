from grongier.pex import BusinessService

from dataclass_csv import DataclassReader

import obj
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
        It changes the current path to the file to the one specified in the path 
        attribute of the object, or to '/home/irisowner/fhirapp/python/csv/' if no path attribute
        is specified, it changes the filename and the fhir_type used for mapping if needed.
        :return: None
        """
        if not hasattr(self,'path'):
            self.path = '/home/irisowner/fhirapp/src/python/csv/'
        if not hasattr(self,'filename'):
            self.filename = 'Organization.csv'
        if not hasattr(self,'fhir_type'):
            self.fhir_type = "BaseOrganization"

        try:
            os.rename(self.path + "used/" + self.filename  , self.path + self.filename)
        except:
            pass

        return None

    def on_process_input(self,request):
        """
        It reads the organization.csv file, creates an OrgaRequest message for 
        each row following the BaseOrganization dataclass, and sends it to the
        Python.ProcessCSV process.
        
        :param request: the request object
        :return: None
        """
        # Find the class to use to map the csv ( specified in the settings )
        class_to_read = getattr(obj, self.fhir_type)
        # We open the file
        with open(self.path + self.filename,encoding="utf-8") as csv:
            # We read it and map it using the object BaseOrganization from earlier
            reader = DataclassReader(csv, class_to_read ,delimiter=";")
            # For each of those organization, we can create a request and send it to the process
            for row in reader:
                msg = OrgaRequest()
                msg.organization = row
                self.send_request_sync('Python.ProcessCSV',msg)

        # Once the file is read, it is moved to the used folder
        os.rename(self.path + self.filename, self.path + "used/" + self.filename)

        return None

