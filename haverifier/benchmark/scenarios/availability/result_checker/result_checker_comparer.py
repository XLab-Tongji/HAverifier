import logging

from baseresultchecker import BaseResultChecker
from haverifier.benchmark.scenarios.availability import Condition
import haverifier.ssh as ssh
from result_checker_general import GeneralResultChecker

LOG = logging.getLogger(__name__)

class ResultCheckerComparer(GeneralResultChecker):

    __result_checker__type__ = "result-checker-comparer"

    def setup(self):
        GeneralResultChecker.setup(self)
        self.leftLegKey = self._config['leftLegKey']
        self.rightLegKey = self._config['rightLegKey']
        self.setup_done = True

    def verify(self,leftLeg,rightLeg):

      if self.condition == Condition.EQUAL:
           self.success = leftLeg.actualResult == rightLeg.expectedResult
      elif self.condition == Condition.GREATERTHAN:
           self.success = leftLeg.actualResult > rightLeg.expectedResult
      elif self.condition == Condition.LESSTHAN:
           self.success = leftLeg.actualResult < rightLeg.expectedResult
      elif self.condition == Condition.IN:
           self.success = leftLeg.actualResult in rightLeg.expectedResult
      else:
          self.success = False
          LOG.debug("error happened when resultchecker: {0} Invalid condition".format(self.key))
      return self.success


