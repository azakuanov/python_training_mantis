from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login (self, username, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_of_the_projects(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            return client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return False