from haverifier.benchmark.scenarios.availability.monitor import basemonitor
from haverifier.benchmark.scenarios.availability.attacker import baseattacker
from haverifier.benchmark.scenarios.availability.operation import baseoperation
from haverifier.benchmark.scenarios.availability.result_checker import baseresultchecker

class ActionPlayers(object):

    def action(self):
        pass

    def set_value_list(self,value_list):
        pass

class AttackerPlayer(ActionPlayers):

    def __init__(self,attacker):
        self.underlyingAttacker = attacker

    def action(self):
        self.underlyingAttacker.inject_fault()

    def set_value_list(self,value_list):
        self.underlyingAttacker.set_value_list(value_list)

class OperationPlayer(ActionPlayers):

    def __init__(self,operation):
        self.underlyingOperation = operation

    def action(self):
        self.underlyingOperation.run()

    def set_value_list(self,value_list):
        self.underlyingOperation.set_value_list(value_list)

class MonitorPlayer(ActionPlayers):

    def __init__(self,monitor):
        self.underlyingmonitor = monitor

    def action(self):
        self.underlyingmonitor.start_monitor()

class ResultCheckerPlayer(ActionPlayers):

    def __init__(self,resultChecker):
        self.underlyingresultChecker = resultChecker

    def action(self):
        self.underlyingresultChecker.verify()

    def set_value_list(self,value_list):
        self.underlyingresultChecker.set_value_list(value_list)

class ResultCheckerComparerPlayer(ActionPlayers):

    def __init__(self,comparer):
        self.underlyingresultChecker = comparer

    def action(self):
        self.underlyingresultChecker.verify(self.underlyingresultChecker.leftLeg,self.underlyingresultChecker.rightLeg)