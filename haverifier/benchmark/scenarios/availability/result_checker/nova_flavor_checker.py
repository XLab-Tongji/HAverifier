import logging

from baseresultchecker import BaseResultChecker
from haverifier.benchmark.scenarios.availability import Condition
import haverifier.ssh as ssh
import types
LOG = logging.getLogger(__name__)

class NovaFlavorChecker(BaseResultChecker):

    __result_checker__type__ = "nova-flavor-checker"

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

        self.resultchecker_cfgs = BaseResultChecker.resultchecker_cfgs.get(self.type)
        self.verify_script = self.get_script_fullpath(self.resultchecker_cfgs['verify_script'])
        self.setup_done = True

    def verify(self):
          LOG.debug("verifying script is %s" %(self.verify_script))
          exit_status, stdout, stderr = self.connection.execute(
            "/bin/bash -s",
            stdin=open(self.verify_script, "r"))
          if exit_status == 0 and stdout:
              self.actualResult = stdout
              LOG.debug("verifying resultchecker: {0}".format(self.key))
              LOG.debug("verifying resultchecker,expected: {0}".format(self.expectedResult))
              LOG.debug("verifying resultchecker,actual: {0}".format(self.actualResult))
              LOG.debug("verifying resultchecker,condition: {0}".format(self.condition))
              if(type(self.expectedResult) is int):
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
              
          self.logResult()
          return self.success

    def logResult(self):
      self.logColor = "\033[91m"
      if self.success:
        self.logColor = "\033[92m"

      LOG.debug("\033[94m verifying resultchecker: {0},the result is : {1} {2} \033[0m".format(self.key,self.logColor,self.success))
