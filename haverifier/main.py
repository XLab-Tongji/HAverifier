import os
import sys
import yaml
import logging
from optparse import OptionParser
from haverifier.benchmark.Runner import Runner

if __name__ == '__main__':
    main()


def main():
    HaVerifierCli().main()


class HaVerifierCli(object):

    def __init__(self):
        self.options = ""
        self.args = ""
        self.scenario_cfg  = ""
        self.context_cfg = ""

        parser = OptionParser(usage="%prog [optinos] file_path")
        parser.add_option("-d", "--debug", action="store_true", default = False, help="show the debug information")
        (self.options, self.args) = parser.parse_args()

        if (len(self.args) != 1):
            os.system("haverifier -h")
            sys.exit(-1)

        logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%a, %d %b %Y %H:%M:%S")

    def set_log_level(self):
        logger = logging.getLogger()
        if self.options.debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

    def parse_file(self):
        file_path = self.args[0]    # rain path
        logging.debug(file_path)
        try:
            yaml_content = yaml.load(file(file_path))
        except Exception as e:
            print "Error: Please choice a yaml file from services/ "
            sys.exit(-1)

        self.context_cfg = yaml_content["context"]
        self.scenario_cfg = yaml_content["scenarios"][0]
        self.context_cfg["nodes"] = {}
        logging.debug(self.context_cfg)
        logging.debug(self.context_cfg["file"])

        yaml_pod = yaml.load(file(self.context_cfg["file"]))
        for yaml_node in yaml_pod.get("nodes"):
            name = yaml_node["name"]
            if name in self.scenario_cfg.get("nodes").keys():
                yaml_node["name"] = "%s.%s" % (name, self.context_cfg["name"])
                self.context_cfg["nodes"][name] = yaml_node

    def main(self):

        self.set_log_level()

        self.parse_file()

        Runner().run(self.scenario_cfg, self.context_cfg)
