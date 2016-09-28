import logging
import base64,urllib,httplib,json,os
from urlparse import urlparse
from baseoperation import BaseOperation
from haverifier.benchmark.scenarios.availability.util import *

LOG = logging.getLogger(__name__)

class HttpOperaion(BaseOperation):

    __operation__type__ = "http-operation"

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
            service=self.action_param[1]
            params1 = '{"auth": {"tenantName": "admin", "passwordCredentials":{"username": "admin", "password": "admin"}}}'
            headers1 = {"Content-Type": 'application/json'}
            conn1 = httplib.HTTPConnection(url1)
            conn1.request("POST","/v2.0/tokens",params1,headers1)
            response1 = conn1.getresponse()
            data1 = response1.read()
            dd1 = json.loads(data1)
            conn1.close()

            apitoken = dd1['access']['token']['id']
            apitenant= dd1['access']['token']['tenant']['id']
            apiurl = dd1['access']['serviceCatalog'][0]['endpoints'][0]['publicURL']
            apiurlt = urlparse(dd1['access']['serviceCatalog'][0]['endpoints'][0]['publicURL'])
            #print ("the apiurl is %s ,the apiurlt is %s" %(apiurl,apiurlt))

            """
            component_name= dd1['access']['serviceCatalog'][0]['name']
            component_endpoints= dd1['access']['serviceCatalog'][0]['endpoints']
            component_dict = dict()
            component_dict[component_name] = component_endpoints
            print component_dict[component_name] 
            """

            url2 = apiurlt[1]
            params2 = urllib.urlencode({})
            headers2 = { "X-Auth-Token":apitoken, "Content-type":"application/json" }
            conn2 = httplib.HTTPConnection(url2)
            conn2.request("GET", "%s/%s" % (apiurlt[2],service), params2, headers2)
            response2 = conn2.getresponse()
            data2 = response2.read()
            dd2 = json.loads(data2)
            conn2.close()
            print (dd2)
            LOG.debug("operation success!")
        else:
            LOG.debug("operation fail,no action parameret!")

        

    def rollback(self):
        pass