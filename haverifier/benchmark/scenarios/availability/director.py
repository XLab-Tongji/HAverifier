import logging
from haverifier.benchmark.scenarios import base
from haverifier.benchmark.scenarios.availability.monitor import basemonitor
from haverifier.benchmark.scenarios.availability.attacker import baseattacker
from haverifier.benchmark.scenarios.availability.operation import baseoperation
from haverifier.benchmark.scenarios.availability.result_checker import baseresultchecker
from haverifier.benchmark.scenarios.availability import ActionType
from haverifier.benchmark.scenarios.availability.actionplayers import *
from haverifier.benchmark.scenarios.availability.actionrollbackers import *

LOG = logging.getLogger(__name__)
class Director(object):


    def __init__(self,scenario_cfg, context_cfg):

        self.executionSteps = [];

        self.scenario_cfg = scenario_cfg
        self.context_cfg = context_cfg
        nodes = self.context_cfg.get("nodes", None)

        #setup attackers
        if "attackers" in self.scenario_cfg["options"]:
            LOG.debug("start init attackers..")
            attacker_cfgs = self.scenario_cfg["options"]["attackers"]
            self.attackerMgr = baseattacker.AttackerMgr();
            self.attackerMgr.init_attackers(attacker_cfgs, nodes)
        #setup monitors
        if "monitors" in self.scenario_cfg["options"]:
            LOG.debug("start init monitors...")
            monitor_cfgs = self.scenario_cfg["options"]["monitors"]
            self.monitorMgr = basemonitor.MonitorMgr()
            self.monitorMgr.init_monitors(monitor_cfgs, nodes)
        #setup operations
        if "operations" in self.scenario_cfg["options"]:
            LOG.debug("start init operations...")
            operation_cfgs = self.scenario_cfg["options"]["operations"]
            self.operationMgr = baseoperation.OperationMgr()
            self.operationMgr.init_operations(operation_cfgs,nodes)
        #setup result checker
        if "resultCheckers" in self.scenario_cfg["options"]:
            LOG.debug("start init resultCheckers...")
            result_check_cfgs = self.scenario_cfg["options"]["resultCheckers"]
            self.resultCheckerMgr = baseresultchecker.ResultCheckerMgr()
            self.resultCheckerMgr.init_ResultChecker(result_check_cfgs,nodes)
            self.setup_done = True

    def createActionPlayer(self,type,key):
        LOG.debug("the type of current action is %s ,the key is %s" %(type,key))
        if hasattr(self,'monitorMgr'):
            LOG.debug("monitorMgr length: %s" %(str(len(self.monitorMgr._monitor_list))))
        if hasattr(self,'attackerMgr'):
            LOG.debug("attackerMgr length: %s" %(str(len(self.attackerMgr._attacker_list))))
        if hasattr(self,'resultCheckerMgr'):
            LOG.debug("resultCheckerMgr length: %s" %(str(len(self.resultCheckerMgr._result_checker_list))))
        if type == ActionType.ATTACKER:
            return AttackerPlayer(self.attackerMgr[key])
        if type == ActionType.MONITOR:
            return MonitorPlayer(self.monitorMgr[key])
        if type == ActionType.RESULTCHECKER:
            return ResultCheckerPlayer(self.resultCheckerMgr[key])
        if type == ActionType.OPERATION:
            return OperationPlayer(self.operationMgr[key])
        if type == ActionType.RESULTCOMPARER:
            comparer  = self.resultCheckerMgr[key]
            return ResultCheckerComparerPlayer(comparer)
        LOG.debug("something run when creatactionplayer")

    def createActionRollbacker(self,type,key):
        LOG.debug("the type of current action is %s ,the key is %s" %(type,key))
        if type == ActionType.ATTACKER:
            return AttackerRollbacker(self.attackerMgr[key])
        if type == ActionType.OPERATION:
            return OperationRollbacker(self.operationMgr[key])
        LOG.debug("no rollbacker created for %s" %(key))

    def verify(self):
        result = True;
        if hasattr(self, 'monitorMgr'):
            result &= self.monitorMgr.verify_SLA()
        if hasattr(self, 'resultCheckerMgr'):
            result &= self.resultCheckerMgr.verify()
        if result:
             LOG.debug("monitors are passed")
        return result

    def stopMonitors(self):
        if "monitors" in self.scenario_cfg["options"]:
          self.monitorMgr.wait_monitors()

    def knockoff(self):
         LOG.debug("knock off ....")
         '''
         if "operations" in self.scenario_cfg["options"]:
           self.operationMgr.rollback()
         if "attackers" in self.scenario_cfg["options"]:
           self.attackerMgr.recover()
         '''
         while self.executionSteps:
            singleStep = self.executionSteps.pop()
            singleStep.rollback()
