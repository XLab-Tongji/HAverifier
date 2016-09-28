import logging
from attacker_config import ConfigureFileAttacker
from baseattacker import BaseAttacker
import haverifier.ssh as ssh

LOG = logging.getLogger(__name__)

class ChangeConfigAttacker(ConfigureFileAttacker):
    __attacker_type__ = 'change-configfile'

    def setup_scripts_config(self):
        self.cfg_name = self._config['conf_name']
        self.match_content_to_modify=self._config['match_content_to_modify']
        self.content_to_modify=self._config['content_to_modify']
        self.fault_cfg = BaseAttacker.attacker_cfgs.get(self.__attacker_type__)

        self.check_script = self.get_script_fullpath(
            self.fault_cfg['check_script'])
        self.inject_script = self.get_script_fullpath(
            self.fault_cfg['inject_script'])
        self.recovery_script = self.get_script_fullpath(
            self.fault_cfg['recovery_script'])

    def check(self):
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/sh -s",
            stdin=open(self.check_script, "r"))

        if not stderr:
            LOG.info("check the envrioment success!")
            return True
        else:
            LOG.error(
                "the host envrioment is error when doing check(), stdout:%s, stderr:%s" %(stdout, stderr))
        return False

    def inject_fault(self):
        LOG.info("start modifying config file: %s!" %(self.cfg_name))
        LOG.info("match content to modify: %s!" %(self.content_to_modify))
        LOG.info("current user is %s:" %(self.connection.user))
        LOG.info("executing command:%s" %("/bin/sh -s \"{0}\" \"{1}\" {2}".format(self.match_content_to_modify,self.content_to_modify,self.cfg_name)))
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/sh -s \"{0}\" \"{1}\" {2}".format(self.match_content_to_modify,self.content_to_modify,self.cfg_name),
            stdin=open(self.inject_script, "r"))
        if not stderr:
            LOG.info("inject successfully!")
        else:
             LOG.error(
                "failed when doing inject, stdout:%s, stderr:%s" %(stdout, stderr))

    def recover(self):
        exit_status, stdout, stderr = self.connection.execute(
            "/bin/sh -s {0}".format(self.cfg_name),
            stdin=open(self.recovery_script, "r"))