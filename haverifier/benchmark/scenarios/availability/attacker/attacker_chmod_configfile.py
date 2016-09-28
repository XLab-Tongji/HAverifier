import logging
from attacker_config import ConfigureFileAttacker
from baseattacker import BaseAttacker
import haverifier.ssh as ssh

LOG = logging.getLogger(__name__)

class ChangeConfigPermissionModeAttacker(ConfigureFileAttacker):
    __attacker_type__ = 'chmod-configfile'