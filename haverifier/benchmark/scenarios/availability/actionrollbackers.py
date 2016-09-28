import logging
from haverifier.benchmark.scenarios import base
from haverifier.benchmark.scenarios.availability.monitor import basemonitor
from haverifier.benchmark.scenarios.availability.attacker import baseattacker
from haverifier.benchmark.scenarios.availability.operation import baseoperation
from haverifier.benchmark.scenarios.availability.result_checker import baseresultchecker

LOG = logging.getLogger(__name__)
class ActionRollbacker(object):

    def rollback(self):
        pass

class AttackerRollbacker(ActionRollbacker):

    def __init__(self,attacker):
        self.underlyingAttacker = attacker

    def rollback(self):
        LOG.debug("\033[93m recovering attacker %s \033[0m" %(self.underlyingAttacker.key))
        self.underlyingAttacker.recover()

class OperationRollbacker(ActionRollbacker):

    def __init__(self,operation):
        self.underlyingOperation = operation

    def rollback(self):
        LOG.debug("\033[93m rollback operation %s \033[0m" %(self.underlyingOperation.key))
        self.underlyingOperation.rollback()
