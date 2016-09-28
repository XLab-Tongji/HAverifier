import os
import time
import logging
import multiprocessing
from haverifier.benchmark.scenarios.availability.serviceha import ServiceHA
from haverifier.benchmark.scenarios.availability.scenario_general import ScenarioGeneral


def _worker_process(cls, method_name, scenario_cfg, context_cfg):
    # queue = {}

    # sequence = 1

    runner_cfg = scenario_cfg['runner']
    runner_cfg['runner_id'] = os.getpid()

    interval = runner_cfg.get("interval", 1)
    duration = runner_cfg.get("duration", 60)

    benchmark = cls
    benchmark.setup()
    method = getattr(benchmark, method_name)
    logging.debug(method)

    if "sla" in scenario_cfg:
        sla_action = scenario_cfg["sla"].get("action", "assert")
    else:
        pass

    start = time.time()
    while True:

        data = {}
        errors = ""

        try:
            method(data)
        except AssertionError as assertion:
            # SLA validation failed in scenario, determine what to do now
            if sla_action == "assert":
                raise
            elif sla_action == "monitor":
                errors = assertion.args
        except Exception as e:
            errors = traceback.format_exc()

        time.sleep(interval)

        # benchmark_output = {
        #     'timestamp': time.time(),
        #     'sequence': sequence,
        #     'data': data,
        #     'errors': errors
        # }

        # record = {'runner_id': runner_cfg['runner_id'],
        #           'benchmark': benchmark_output}
        #
        #
        # sequence += 1

        if (errors and sla_action is None) or \
                (time.time() - start > duration or aborted.is_set()):
            break

    benchmark.teardown()


class Runner(object):

    def __init__(self):
        pass

    def run(self, scenario_cfg, context_cfg):

        scenario_type = scenario_cfg["type"]
        if scenario_type == "ServiceHA":
            cls = ServiceHA(scenario_cfg, context_cfg)
        elif scenario_type == "general_scenario":
            cls = ScenarioGeneral(scenario_cfg, context_cfg)
        else:
            pass

        process = multiprocessing.Process(target=_worker_process,
                                          args=(cls, "run", scenario_cfg, context_cfg))
        process.start()
