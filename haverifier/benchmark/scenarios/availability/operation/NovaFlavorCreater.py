import logging
from baseoperation import BaseOperation
from operation_general import GeneralOperaion
import haverifier.ssh as ssh

LOG = logging.getLogger(__name__)

class NovaFlavorCreater(GeneralOperaion):

    __operation__type__ = "nova-create-flavor"

    def setup(self):
        GeneralOperaion.setup(self)
        self.parameter = self._config['parameter']
        self.flavorid = self.parameter['flavorid']
        self.flavorname = self.parameter['flavorname']
        self.ram = self.parameter['ram']
        self.disk = self.parameter['disk']
        self.vcpus = self.parameter['vcpus']

    def run(self):
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/bash -s {0} {1} {2} {3} {4}".format(self.flavorname , self.flavorid , self.ram , self.disk , self.vcpus),
            stdin=open(self.action_script, "r"))

    def rollback(self):
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/bash -s {0}".format(self.flavorid),
            stdin=open(self.rollback_script, "r"))
