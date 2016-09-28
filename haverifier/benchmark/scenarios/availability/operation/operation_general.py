import logging

from baseoperation import BaseOperation
import haverifier.ssh as ssh
from haverifier.benchmark.scenarios.availability.util import *

LOG = logging.getLogger(__name__)

class GeneralOperaion(BaseOperation):

    __operation__type__ = "general-operation"

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
        self.type = self._config['operation_type']

        if "actionParameter" in self._config:
            actionParameter = self._config['actionParameter']
            str = buildshellparams(actionParameter)
            LOG.debug("inject parameter is: {0}".format(actionParameter))
            LOG.debug("inject parameter values are: {0}".format(actionParameter.values()))
            l = list(item for item in actionParameter.values())
            self.action_param = str.format(*l)

        if "rollbackParameter" in self._config:
            rollbackParameter = self._config['rollbackParameter']
            str = buildshellparams(rollbackParameter)
            LOG.debug("recover parameter is: {0}".format(rollbackParameter))
            LOG.debug("recover parameter values are: {0}".format(rollbackParameter.values()))
            l = list(item for item in rollbackParameter.values())
            self.rollback_param = str.format(*l)

        if(self.__operation__type__ == "general-operation"):
            self.operation_cfgs = BaseOperation.operation_cfgs.get(self.key)
        else:
            self.operation_cfgs = BaseOperation.operation_cfgs.get(self.type)

        self.action_script = self.get_script_fullpath(
            self.operation_cfgs['action_script'])
        self.rollback_script = self.get_script_fullpath(
            self.operation_cfgs['rollback_script'])
        self.setup_done = True
        self.value_list = {}
        self.value_prefix = "@_@"

    def run(self):
        if self.is_resetup_necessary():
            self.resetup_parameter()

        if "actionParameter" in self._config:
            exit_status, stdout, stderr = self.connection.execute(
                self.action_param,
                stdin=open(self.action_script, "r"))
        else:
          exit_status, stdout, stderr = self.connection.execute(
            "/bin/sh -s ",
            stdin=open(self.action_script, "r"))

        LOG.debug("action script of the operation is: {0}".format(self.action_script ))
        LOG.debug("action parameter the of operation is: {0}".format(self.action_param ))

        if exit_status == 0:
            LOG.debug("success,the operation's output is: {0}".format(stdout))
        else:
            LOG.error(
                "the operation's error, stdout:%s, stderr:%s" %
                (stdout, stderr))

    def rollback(self):
        if "rollbackParameter" in self._config:
            exit_status, stdout, stderr = self.connection.execute(
                self.rollback_param,
                stdin=open(self.rollback_script, "r"))
            return

        exit_status, stdout, stderr = self.connection.execute(
            "/bin/sh -s ",
            stdin=open(self.rollback_script, "r"))

    def set_value_list(self,value_list):
        self.value_list = value_list

    def is_resetup_necessary(self):
        if "actionParameter" in self._config:
            if self.action_param.find(self.value_prefix)!=-1:
                LOG.debug("result True")
                return True
        if "rollbackParameter" in self._config:
            if self.rollback_param.find(self.value_prefix)!=-1:
                LOG.debug("result True")
                return True
        LOG.debug("result False")
        return False

    def resetup_parameter(self):
        if "actionParameter" in self._config:
            actionParameter = self._config['actionParameter']
            str = buildshellparams(actionParameter)
            l = list(item for item in actionParameter.values())
            # -- convert start
            for i in range(len(l)):
                if l[i].find("@_@") == 0:
                    if self.value_list.has_key(l[i]):
                        l[i] = self.value_list[l[i]]
                        LOG.debug("resetup parameter sucess")
                    else:
                        LOG.debug("resetup parameter error")
            # -- convert finish
            self.action_param = str.format(*l)
            LOG.debug("after resetup {0}".format(self.action_param))

        if "rollbackParameter" in self._config:
            rollbackParameter = self._config['rollbackParameter']
            str = buildshellparams(rollbackParameter)
            l = list(item for item in rollbackParameter.values())
            # -- convert start
            for i in range(len(l)):
                if l[i].find("@_@") == 0:
                    if self.value_list.has_key(l[i]):
                        l[i] = self.value_list[l[i]]
                        LOG.debug("resetup parameter sucess")
                    else:
                        LOG.debug("resetup parameter error")
            # -- convert finish
            self.rollback_param = str.format(*l)
            LOG.debug("after resetup {0}".format(self.action_param))
