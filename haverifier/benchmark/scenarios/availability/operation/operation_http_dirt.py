import logging
import base64,urllib,httplib,json,os
from urlparse import urlparse
from baseoperation import BaseOperation
from haverifier.benchmark.scenarios.availability.util import *

LOG = logging.getLogger(__name__)

class HttpOperaion(BaseOperation):

    __operation__type__ = "http-operation-dirt"

    def setup(self):
        LOG.debug("config:%s context:%s" % (self._config, self._context))
        

        self.key = self._config['key']
        self.type = self._config['operation_type']

        if "action_parameter" in self._config:
            actionParameter = self._config['action_parameter']
            str = buildshellparams(actionParameter)
            LOG.debug("inject parameter is: {0}".format(actionParameter))
            LOG.debug("inject parameter values are: {0}".format(actionParameter.values()))
            l = list(item for item in actionParameter.values())
            #self.action_param = str.format(*l)
            self.action_param = actionParameter.values()

        if "rollback_parameter" in self._config:
            rollbackParameter = self._config['rollback_parameter']
            str = buildshellparams(rollbackParameter)
            LOG.debug("recover parameter is: {0}".format(rollbackParameter))
            LOG.debug("recover parameter values are: {0}".format(rollbackParameter.values()))
            l = list(item for item in rollbackParameter.values())
            self.rollback_param = str.format(*l)


    def run(self):
        if "action_parameter" in self._config:

            url1=self.action_param[0]
            #print ("url is %s" % url1)
            component=self.action_param[1]
            params1 = '{"auth": {"tenantName": "admin", "passwordCredentials":{"username": "admin", "password": "admin"}}}'
            headers1 = {"Content-Type": 'application/json'}
            conn1 = httplib.HTTPConnection(url1)
            conn1.request("POST","/v2.0/tokens",params1,headers1)
            response1 = conn1.getresponse()
            data1 = response1.read()
            dd1 = json.loads(data1)
            conn1.close()

            component_dict = dict()
            serviceCatalogList=dd1['access']['serviceCatalog']
            for element in serviceCatalogList:
               #print("list.......:"+str(element))
               component_name= element['name']
               component_endpoints= element['endpoints'][0]
               component_dict[component_name] = component_endpoints

            print ("component_dict.....:"+str(component_dict))
            print ("component %s url: " % component)
            print component_dict[component] 
            LOG.debug("operation success!")
        else:
            LOG.debug("operation fail,no action parameret!")

        

    def rollback(self):
        pass