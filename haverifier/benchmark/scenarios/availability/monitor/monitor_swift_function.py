##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd. and others
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
import logging
import subprocess
import traceback
import haverifier.ssh as ssh
import basemonitor as basemonitor
from monitor_command import MonitorOpenstackCmd
LOG = logging.getLogger(__name__)



class SwiftFunctionMonitor(MonitorOpenstackCmd):
    """docstring for MonitorApi"""

    __monitor_type__ = "swift-monitor-function"

    def setup(self):
        self.connection = None
        node_name = self._config.get("host", None)
        if node_name:
            host = self._context[node_name]
            ip = host.get("ip", None)
            user = host.get("user", "root")
            key_filename = host.get("key_filename", "~/.ssh/id_rsa")
            self.connection = ssh.SSH(user, ip, key_filename=key_filename)
            self.connection.wait(timeout=600)
            LOG.debug("ssh host success!")

        self.check_script = self.get_script_fullpath(self._config["command_name"])



    def monitor_func(self):
        exit_status = 0

        exit_status, stdout, stderr = self.connection.execute(
            "/bin/bash -s ",
            stdin=open(self.check_script, "r"))
        if stderr and "503" not in stderr:
            exit_status = 0
        LOG.debug("the ret stats: %s stdout: %s stderr: %s" %
                  (exit_status, stdout, stderr))

        if exit_status:
            return False
        return True

