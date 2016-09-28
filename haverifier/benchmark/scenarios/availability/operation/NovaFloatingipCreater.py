import logging
from baseoperation import BaseOperation
from operation_general import GeneralOperaion
import haverifier.ssh as ssh
from haverifier.benchmark.scenarios.availability.stdout_reader import StdoutReader

LOG = logging.getLogger(__name__)

class NovaFloatingipCreater(GeneralOperaion):

    __operation__type__ = "nova-create-floatingip"

    def setup(self):
        GeneralOperaion.setup(self)
        self.parameter = self._config['parameter']
        self.network = self.parameter['network']
        self.value_list = {}
        if "returnValue" in self._config:
            self.value = self._config['returnValue']['floatingip']

    def run(self):
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/bash -s {0}".format(self.network),
            stdin=open(self.action_script, "r"))
        self.floatingip = StdoutReader.readLineItem(stdout,"IP")
        LOG.debug("created floatingip: %s" %(self.floatingip));
        if "returnValue" in self._config:
            self.value_list[self.value] = self.floatingip;

    def rollback(self):
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/bash -s {0}".format(self.floatingip),
            stdin=open(self.rollback_script, "r"))

    def set_value_list(self,value_list):
        self.value_list = value_list