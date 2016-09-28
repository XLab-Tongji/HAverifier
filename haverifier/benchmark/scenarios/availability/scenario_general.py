##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd. and others
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
import logging
import traceback

from haverifier.benchmark.scenarios import base
from haverifier.benchmark.scenarios.availability.monitor import basemonitor
from haverifier.benchmark.scenarios.availability.attacker import baseattacker
from haverifier.benchmark.scenarios.availability.operation import baseoperation
from haverifier.benchmark.scenarios.availability.result_checker import baseresultchecker
from haverifier.benchmark.scenarios.availability.director import Director



LOG = logging.getLogger(__name__)

class ScenarioGeneral(base.Scenario):
     __scenario_type__ = "general_scenario"

     def __init__(self, scenario_cfg, context_cfg):

         LOG.debug(
            "scenario_cfg:%s context_cfg:%s" %
            (scenario_cfg, context_cfg))
         self.scenario_cfg = scenario_cfg
         self.context_cfg = context_cfg
         self.value_list = {}
         self.setup_done = False

     def setup(self):
        self.director = Director(self.scenario_cfg,self.context_cfg)
        self.setup_done = True

     def run(self, args):
        steps = self.scenario_cfg["options"]["steps"]
        orderedSteps = sorted(steps,key = lambda x:x['index'])
        excetionSteps = []
        for step in orderedSteps:
            LOG.debug("\033[94m running step: {0} .... \033[0m".format(orderedSteps.index(step)+1))
            try:
                actionPlayer = self.director.createActionPlayer(step['actionType'],step['actionKey'])
                LOG.debug("mmm001")
                if step['actionType'] == 'operation' or step['actionType'] == 'attacker' or step['actionType'] == 'resultchecker':
                    actionPlayer.set_value_list(self.value_list)
                LOG.debug("mmm002")
                actionPlayer.action()
                LOG.debug("the value_list after floatingip created")
                LOG.debug(self.value_list)
                actionRollbacker = self.director.createActionRollbacker(step['actionType'],step['actionKey'])
                if actionRollbacker:
                    self.director.executionSteps.append(actionRollbacker)
            except Exception,e:
                LOG.debug(e.message)
                traceback.print_exc()
                LOG.debug("\033[91m exception when running step:{0} .... \033[0m".format(orderedSteps.index(step)))
                break
            finally:
                pass

        self.director.stopMonitors()
        if self.director.verify():
            LOG.debug("\033[92m congratulations,the test cases scenario is pass! \033[0m")
        else:
            LOG.debug("\033[91m aoh,the test cases scenario failed,please check the detail debug information! \033[0m")

     def teardown(self):
         self.director.knockoff()
