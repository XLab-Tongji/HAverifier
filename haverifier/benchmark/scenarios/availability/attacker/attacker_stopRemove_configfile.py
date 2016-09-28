import logging
from attacker_config import ConfigureFileAttacker
from baseattacker import BaseAttacker
import haverifier.ssh as ssh

LOG = logging.getLogger(__name__)

class RemoveConfigAttacker(ConfigureFileAttacker):
    __attacker_type__ = 'stopRemove-configfile'