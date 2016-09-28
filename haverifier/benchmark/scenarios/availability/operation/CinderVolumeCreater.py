import logging
from baseoperation import BaseOperation
from operation_general import GeneralOperaion
import haverifier.ssh as ssh
from haverifier.benchmark.scenarios.availability.stdout_reader import StdoutReader
from haverifier.benchmark.scenarios.availability.util import *

LOG = logging.getLogger(__name__)

class CinderVolumeCreater(GeneralOperaion):

    __operation__type__ = "cinder-create-volume"

    def setup(self):
        GeneralOperaion.setup(self)
        actionParameter = self._config['actionParameter']
        str = buildshellparams(actionParameter)
        LOG.debug("inject parameter is: {0}".format(actionParameter))
        LOG.debug("inject parameter values are: {0}".format(actionParameter.values()))
        l = list(item for item in actionParameter.values())
        self.action_param = str.format(*l)

        self.value_list = {}
        if "returnValue" in self._config:
            self.volume_id = self._config['returnValue']['volumeID']

    def run(self):
        exit_status, stdout, stderr = self.connection.execute(
            self.action_param,
            stdin=open(self.action_script, "r"))
        self.volumeID = StdoutReader.read_line_from_map(stdout,"id")
        LOG.debug("created volumeID: %s" %(self.volumeID));
        if "returnValue" in self._config:
            self.value_list[self.volume_id] = self.volumeID;

    def rollback(self):
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/bash -s {0}".format(self.volumeID),
            stdin=open(self.rollback_script, "r"))

    def set_value_list(self,value_list):
        self.value_list = value_list