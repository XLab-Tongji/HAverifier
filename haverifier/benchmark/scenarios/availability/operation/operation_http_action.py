import logging
import base64,urllib,httplib,json,os
import pkg_resources
import yaml
from urlparse import urlparse
from baseoperation import BaseOperation
from haverifier.benchmark.scenarios.availability.util import *

LOG = logging.getLogger(__name__)

operation_conf_path = pkg_resources.resource_filename(
    "haverifier.benchmark.scenarios.availability",
    "http_conf.yaml")

class HttpOperaion(BaseOperation):

    __operation__type__ = "http-operation-action"
    operation_cfgs = {}

    def setup(self):
        LOG.debug("config:%s context:%s" % (self._config, self._context))
        self.type = self._config['operation_type']
        self.key = self._config['key']
        #read config yaml file
        if not HttpOperaion.operation_cfgs:
            with open(operation_conf_path) as stream:
                HttpOperaion.operation_cfgs = yaml.load(stream)

        if "action_parameter" in self._config:
            #actionParameter = self._config['action_parameter']
            self.url = self._config['action_parameter']['url']
            self.action_type = self._config['action_parameter']['action_type']
            urlParameter = self._config['action_parameter']['url_parameter']
            requestParameter = self._config['action_parameter']['request_parameter']
            self.url_param = urlParameter.values()
            self.request_param = requestParameter.values()

            LOG.debug("url parameter is: {0}".format(urlParameter))
            LOG.debug("url parameter values are: {0}".format(urlParameter.values()))
            #str = buildshellparams(actionParameter)
            #l = list(item for item in actionParameter.values())
            #self.action_param = str.format(*l)

            #self.action_param = actionParameter.values()


        if "rollback_parameter" in self._config:
            rollbackParameter = self._config['rollback_parameter']
            str = buildshellparams(rollbackParameter)
            LOG.debug("recover parameter is: {0}".format(rollbackParameter))
            LOG.debug("recover parameter values are: {0}".format(rollbackParameter.values()))
            l = list(item for item in rollbackParameter.values())
            self.rollback_param = str.format(*l)

        self.http_action_path = HttpOperaion.operation_cfgs.get(self.action_type)
         
        
        
    def run(self):
        if "action_parameter" in self._config:
            tenant_name = self.request_param[0]
            user_name = self.request_param[1]
            pass_word = self.request_param[2]
            params1 = '{"auth": {"tenantName": "%s", "passwordCredentials":{"username": "%s", "password": "%s"}}}'%(tenant_name,user_name,pass_word)
            
            #params1=str(params_dict)
            print ("the params1 is %s" % params1)
            headers1 = {"Content-Type": 'application/json'}
            conn1 = httplib.HTTPConnection(self.url)
            conn1.request("POST","/v2.0/tokens",params1,headers1)
            response1 = conn1.getresponse()
            data1 = response1.read()
            dd1 = json.loads(data1)
            print (dd1)
            conn1.close()

            apitoken = dd1['access']['token']['id']
            apitenant= dd1['access']['token']['tenant']['id']
            apiurl = dd1['access']['serviceCatalog'][0]['endpoints'][0]['publicURL']
            apiurlt = urlparse(dd1['access']['serviceCatalog'][0]['endpoints'][0]['publicURL'])
            print ("the apiurl is %s ,the apiurlt is %s" %(apiurl,apiurlt))


            url2 = apiurlt[1]
            #params2 = urllib.urlencode({})
            #params2 = '{"os-start" : null}'
            headers2 = { "X-Auth-Token":apitoken, "Content-type":"application/json" }
            server_id = self.url_param[0]
            params2 = self.url_param[1]
            action_path=self.http_action_path.format(server_id = server_id)
            #action_path = "%s/%s/%s" % (http_action_path,server_id,action)
            print ("the action_path is %s" % action_path)
            conn2 = httplib.HTTPConnection(url2)
            conn2.request("POST", "%s/%s" % (apiurlt[2],action_path), params2, headers2)
            response2 = conn2.getresponse()
            data2 = response2.read()
            dd2 = json.loads(data2)
            conn2.close()
            print (dd2)
            LOG.debug("operation success!")
        else:
            LOG.debug("operation fail,no action parameret!")

    def set_value_list(self,value_list):
        pass    

    def rollback(self):
        pass