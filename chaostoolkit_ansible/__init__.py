# -*- coding: utf-8 -*-
from typing import Any, Dict, List
import ansible_runner
from chaoslib.discovery.discover import discover_actions, discover_probes, initialize_discovery_result
from chaoslib.exceptions import FailedActivity
from chaoslib.types import Discovery, DiscoveredActivities, Secrets
from logzero import logger
#import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#from  executor import execute
"""Top-level package for chaostoolkit-ansible."""

__all__ = ["ansible_api_client", "discover", "__version__"]
__version__ = '0.1.0'

class ansible_api_client:   
    def __init__(self):
        pass

    def run_script(self, host, user, script):
        #item_dir = "/usr/local/lib/python3.6/site-packages/chaosansible/machine/scripts"
        #script = item_dir + '/' + experiment_type + ".sh"
        #cmd = "ansible -u {user} {host} -m script -a '{script}'".format(user = user, host = host, script = script)
        result = ansible_runner.run(private_data_dir='/tmp/', host_pattern=host, module='script', module_args=script)
        return result.status

    def run_cmd(self, host, user, command):
        result = ansible_runner.run(private_data_dir='/tmp/', host_pattern=host, module='shell', module_args=command)
        return result.status


def discover(discover_system: bool = True) -> Discovery:
    """
    Discover SaltStack capabilities offered by this extension.
    """
    logger.info("Discovering capabilities from chaostoolkit-ansible")

    discovery = initialize_discovery_result(
        "chaostoolkit-ansible", __version__, "chaosansible")
    discovery["activities"].extend(load_exported_activities())
    return discovery

# Private functions
def load_exported_activities() -> List[DiscoveredActivities]:
    """
    Extract metadata from actions and probes exposed by this extension.
    """
    activities = []
    activities.extend(discover_actions("chaostoolkit_ansible.machine.actions"))
    #activities.extend(discover_probes("chaosansible.machine.probes"))
    return activities

