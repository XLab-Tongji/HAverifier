import logging

from baseresultchecker import BaseResultChecker
from haverifier.benchmark.scenarios.availability import Condition
import haverifier.ssh as ssh
import types
from haverifier.benchmark.scenarios.availability.util import *

LOG = logging.getLogger(__name__)

class GeneralResultChecker(BaseResultChecker):

    __result_checker__type__ = "general-result-checker"

    def setup(self):
        LOG.debug("config:%s context:%s" % (self._config, self._context))
        host = self._context.get(self._config['host'], None)
        ip = host.get("ip", None)
        user = host.get("user", "root")
        key_filename = host.get("key_filename", "~/.ssh/id_rsa")

        self.connection = ssh.SSH(user, ip, key_filename=key_filename)
        self.connection.wait(timeout=600)
        LOG.debug("ssh host success!")

        self.key = self._config['key']
        self.type = self._config['checker_type']
        self.condition = self._config['condition']
        self.expectedResult = self._config['expectedValue']
        self.actualResult = object()

        self.key = self._config['key']
        if "parameter" in self._config:
            parameter = self._config['parameter']
            str = buildshellparams(parameter)
            l = list(item for item in parameter.values())
            self.shell_cmd = str.format(*l)

        if self.__result_checker__type__ == "general-result-checker":
          self.resultchecker_cfgs = BaseResultChecker.resultchecker_cfgs.get(self.key)
          self.verify_script = self.get_script_fullpath(self.resultchecker_cfgs['verify_script'])
        self.setup_done = True
        self.value_list = {}
        self.value_prefix = "@_@"

    def verify(self):
        if self.is_resetup_necessary():
            self.resetup_parameter()
            
        if "parameter" in self._config:
          exit_status, stdout, stderr = self.connection.execute(
            self.shell_cmd,
            stdin=open(self.verify_script, "r"))
          LOG.debug("action script of the operation is: {0}".format(self.verify_script))
          LOG.debug("action parameter the of operation is: {0}".format(self.shell_cmd))

        else:
            exit_status, stdout, stderr = self.connection.execute(
                "/bin/bash -s ",
                stdin=open(self.verify_script, "r"))
            LOG.debug("action script of the operation is: {0}".format(self.verify_script))

        LOG.debug("exit_status ,stdout : {0} ,{1}".format(exit_status,stdout))
        if exit_status == 0 and stdout:
            self.actualResult = stdout
            LOG.debug("verifying resultchecker: {0}".format(self.key))
            LOG.debug("verifying resultchecker,expected: {0}".format(self.expectedResult))
            LOG.debug("verifying resultchecker,actual: {0}".format(self.actualResult))
            LOG.debug("verifying resultchecker,condition: {0}".format(self.condition))
            if (type(self.expectedResult) is int):
                self.actualResult = int(self.actualResult)
            if self.condition == Condition.EQUAL:
                self.success = self.actualResult == self.expectedResult
            elif self.condition == Condition.GREATERTHAN:
                self.success = self.actualResult > self.expectedResult
            elif self.condition == Condition.GREATERTHANEQUAL:
                self.success = self.actualResult >= self.expectedResult
            elif self.condition == Condition.LESSTHANEQUAL:
                self.success = self.actualResult <= self.expectedResult
            elif self.condition == Condition.LESSTHAN:
                self.success = self.actualResult < self.expectedResult
            elif self.condition == Condition.IN:
                self.success = self.expectedResult in self.actualResult
            else:
                self.success = False
                LOG.debug("error happened when resultchecker: {0} Invalid condition".format(self.key))
        else:
            self.success = False
            LOG.debug("error happened when resultchecker: {0} verifying the result".format(self.key))
            LOG.error(stderr)

        BaseResultChecker.logResult(self)
        LOG.debug("verifying resultchecker: {0},the result is : {1}".format(self.key, self.success))
        return self.success

    def set_value_list(self,value_list):
        self.value_list = value_list

    def is_resetup_necessary(self):
        if self.expectedResult.find(self.value_prefix)!=-1:
            LOG.debug("result True")
            return True
        return False

    def resetup_parameter(self):
        # -- convert start
        if self.value_list.has_key(self.expectedResult):
            self.expectedResult = self.value_list[self.expectedResult]
            LOG.debug("resetup expectedResult sucess")
        else:
            LOG.debug("resetup expectedResult error")
        # -- convert finish
        LOG.debug("after resetup {0}".format(self.expectedResult))

    # def buildshellparams(self,param):
    #    i = 0
    #    values = []
    #    result = '/bin/bash -s'
    #    for key in param.keys():
    #        values.append(param[key])
    #        result += " {%d}" % i
    #        i=i+1
    #    return result;
