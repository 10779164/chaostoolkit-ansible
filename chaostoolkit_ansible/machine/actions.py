# -*- coding: utf-8 -*-
import os
import json
import time
from time import sleep

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets
from logzero import logger

from .. import ansible_api_client
#     from ..types import SaltStackResponse
#from .constants import OS_LINUX, OS_WINDOWS
from .constants import BURN_CPU, FILL_DISK, NETWORK_UTIL, \
    BURN_IO, KILLALL_PROCESSES, KILL_PROCESS, SHELL


__all__ = ["burn_cpu", "fill_disk", "network_latency", "burn_io",
           "network_loss", "network_corruption", "network_advanced",
           "killall_processes", "kill_process","shell"]


def burn_cpu(host: str = None,
             user: str = "root",
             execution_duration: str = "60",
             configuration: Configuration = None):
    """
    burn CPU up to 100% at random machines.

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional
        Duration of the stress test (in seconds) that generates high CPU usage.
        Defaults to 60 seconds.
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """

    logger.debug("Start burn_cpu")

    param = dict()
    param["duration"] = execution_duration
    param["host"] = host

    return __default_ansible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=BURN_CPU,
                                       configuration=configuration,                                   
                                       )


def fill_disk(host: str = None,
              user: str = "root",
              execution_duration: str = "120",
              size: str = "1000",
              configuration: Configuration = None):
    """
    For now do not have this scenario, fill the disk with random data.

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional
        Lifetime of the file created. Defaults to 120 seconds.
    size : str
        Size of the file created on the disk. Defaults to 1GB(1000M).
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """

    logger.debug(
        "Start fill_disk: configuration='{}', host='{}'".format(
            configuration, host))

    param = dict()
    param["execution_duration"] = execution_duration
    param["size"] = size

    return __default_ansible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=FILL_DISK,
                                       configuration=configuration,
                                       )


def burn_io(host: str = None,
            execution_duration: str = "60",
            configuration: Configuration = None):
    """
    Increases the Disk I/O operations per second of the virtual machine.

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional
        Lifetime of the file created. Defaults to 120 seconds.
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """

    logger.debug(
        "Start burn_io: configuration='{}', host='{}'".format(
            configuration, host))

    param = dict()
    param["duration"] = execution_duration
    param["host"] = host

    return __default_ansible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=BURN_IO,
                                       configuration=configuration,
                                       )


def network_advanced(host: str = None,
                     execution_duration: str = "60",
                     command: str = "",
                     device: str = "eth0",
                     configuration: Configuration = None):
    """
    do a customized operations on the virtual machine via Linux - TC.
    For windows, no solution as for now.

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional
        Lifetime of the file created. Defaults to 60 seconds.
    command : str
        the tc command, e.g.  loss 15%
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """

    logger.debug(
        "Start network_advanced: configuration='{}', host='{}'".format(
            configuration, host))

    param = dict()
    param["duration"] = execution_duration
    param["param"] = command
    param["device"] = device
    param["host"] = host

    return __default_ansible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=NETWORK_UTIL,
                                       configuration=configuration,
                                       )


def network_loss(host: str = None,
                 execution_duration: str = "60",
                 loss_ratio: str = "5%",
                 device: str = "eth0",
                 configuration: Configuration = None):
    """
    do a network loss operations on the virtual machine via Linux - TC.
    For windows, no solution as for now.

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional
        Lifetime of the file created. Defaults to 60 seconds.
    loss_ratio : str:
        loss_ratio = "30%"
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """

    logger.debug(
        "Start network_advanced: configuration='{}', host='{}'".format(
            configuration, host))

    param = dict()
    param["duration"] = execution_duration
    param["param"] = "loss " + loss_ratio
    param["device"] = device
    param["host"] = host
    
    return __default_ansible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=NETWORK_UTIL,
                                       configuration=configuration,
                                       )


def network_corruption(host: str = None,
                       execution_duration: str = "60",
                       corruption_ratio: str = "5%",
                       device: str = "eth0",
                       configuration: Configuration = None):
    """
    do a network loss operations on the virtual machine via Linux - TC.
    For windows, no solution as for now.

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional
        Lifetime of the file created. Defaults to 60 seconds.
    corruption_ratio : str:
        corruption_ratio = "30%"
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """

    logger.debug(
        "Start network_corruption: configuration='{}', "
        "host='{}'".format(configuration, host))

    param = dict()
    param["duration"] = execution_duration
    param["param"] = "corrupt " + corruption_ratio
    param["device"] = device
    param["host"] = host

    return __default_snaible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=NETWORK_UTIL,
                                       configuration=configuration
                                       )


def network_latency(host: str = None,
                    execution_duration: str = "60",
                    delay: str = "1000ms",
                    variance: str = "500ms",
                    ratio: str = "",
                    device: str = "eth0",
                    configuration: Configuration = None):
    """
    Increases the response time of the virtual machine.

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional
        Lifetime of the file created. Defaults to 120 seconds.
    delay : str
        Added delay in ms. Defaults to 1000ms.
    variance : str
        Variance of the delay in ms. Defaults to 500ms.
    ratio: str = "5%", optional
        the specific ratio of how many Variance of the delay in ms.
        Defaults to "".
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """
    logger.debug(
        "Start network_latency: configuration='{}', host='{}'".format(
            configuration, host))

    param = dict()
    param["duration"] = execution_duration
    param["param"] = "delay " + delay + " " + variance + " " + ratio
    param["device"] = device
    param["host"] = host

    return __default_ansible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=NETWORK_UTIL,
                                       configuration=configuration
                                       )


def killall_processes(host: str = None,
                      execution_duration: str = "60",
                      process_name: str = None,
                      configuration: Configuration = None,
                      signal: str = ""):
    """
    The killall utility kills processes selected by name
    refer to https://linux.die.net/man/1/killall

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional default to 1 second
        This is not technically not useful as the process usually is killed
        without and delay, however you can set more seconds here to let the
        thread wait for more time to extend your experiment execution in case
        you need to watch more on the observation metrics.
    process_name : str
        Name of the process to be killed
    signal : str , default to ""
        The signal of killall command, e.g. use -9 to force kill
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """
    logger.debug(
        "Start network_latency: configuration='{}', host='{}'".format(
            configuration, host))

    param = dict()
    param["duration"] = execution_duration
    param["process_name"] = process_name
    param["signal"] = signal
    param["host"] = host

    return __default_ansible_experiment__(host=host,
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=KILLALL_PROCESSES,
                                       configuration=configuration
                                       )


def kill_process(host: str = None,
                 execution_duration: str = "60",
                 process: str = None,
                 configuration: Configuration = None,
                 signal: str = ""):
    """
    kill -s [signal_as_below] [processname]
    HUP INT QUIT ILL TRAP ABRT EMT FPE KILL BUS SEGV SYS PIPE ALRM TERM URG
    STOP TSTP CONT CHLD TTIN TTOU IO XCPU XFSZ VTALRM PROF WINCH INFO USR1 USR2

    Parameters
    ----------
    host: str
        Filter the virtual machines. If the filter is omitted all machines in
        the subscription will be selected as potential chaos candidates.
    execution_duration : str, optional default to 1 second
        This is not technically not useful as the process usually is killed
        without and delay, however you can set more seconds here to let the
        thread wait for more time to extend your experiment execution in case
        you need to watch more on the observation metrics.
    process : str
        pid or process that kill command accepts
    signal : str , default to ""
        The signal of kill command, use kill -l for help
    configuration : Configuration
        Chaostoolkit Configuration
    secrets : Secrets
        Chaostoolkit Secrets
    """
    logger.debug(
        "Start network_latency: configuration='{}', host='{}'".format(
            configuration, host))

    param = dict()
    param["duration"] = execution_duration
    param["process_name"] = process
    param["signal"] = signal
    param["host"] = host

    return __default_ansible_experiment__(host=host,
                                       user="root",
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type="kill_process",
                                       configuration=configuration
                                       )
        

def shell(host: str = None,
                execution_duration: str = "1",
                command: str = None,
                configuration: Configuration = None,
                ):
    """
    Execute the Ansible shell module

    Parameters
        ----------
        host: str
            Filter the virtual machines. If the filter is omitted all machines in
            the subscription will be selected as potential chaos candidates.
        execution_duration : str, optional default to 1 second
            This is not technically not useful as the process usually is killed
            without and delay, however you can set more seconds here to let the
            thread wait for more time to extend your experiment execution in case
            you need to watch more on the observation metrics.
        command : str
            Shell command
        configuration : Configuration
            Chaostoolkit Configuration
        secrets : Secrets
            Chaostoolkit Secrets
    """

    logger.debug(
        "Start execute shell command: configuration='{}', host='{}'".format(
            configuration, host))
    
    param = dict()
    param["duration"] = execution_duration
    param["command"] = command
    param["host"] = host

    return __shell_ansible_experiment__(host=host,
                                       user="root",
                                       execution_duration=execution_duration,
                                       param=param,
                                       experiment_type=SHELL,
                                       configuration=configuration
                                       )


###############################################################################
# Private helper functions
###############################################################################

def  __default_ansible_experiment__(host: str = None,
                                user: str = "root",
                                execution_duration: str = "60",
                                param: dict = None,
                                experiment_type: str = None,
                                configuration: Configuration = None,
                                #user: user
                                ):
    #user = configuration['ansible_instance']['user']
    if host == None:
        raise FailedActivity("No host be found...")

    #script
    # 
    script_content = __construct_script_content__(experiment_type, param)
    cur_time = str(time.strftime('%Y-%m-%d_%H:%M:%S'))
    script_filename = experiment_type + cur_time + ".sh"
    script = "/tmp/" + script_filename
    file = open(script, 'w+', encoding='UTF-8')
    file.write(script_content)
    file.close()


    client = ansible_api_client()
    try:
        response = client.run_script(host, user, script)
        return response
    except Exception as e:
        raise FailedActivity(
            "failed issuing a execute of shell script via ansible API " + str(e)
        )


def __shell_ansible_experiment__(host: str = None,
                                user: str = "root",
                                execution_duration: str = "60",
                                param: dict = None,
                                experiment_type: str = None,
                                configuration: Configuration = None,
                                ):
    if host == None:
        raise FailedActivity("No host be found...")

    #shell
    command = str(param["command"])
    if command == None:
        raise FailedActivity("Command not be empty...")

    client = ansible_api_client()
    try:
        response = client.run_cmd(host, user, command)
        return response
    except Exception as e:
        raise FailedActivity(
            "failed issuing a execute of shell command via ansible API " + str(e)
        )



def __construct_script_content__(experiment_type, parameters):
    script_name = experiment_type +".sh"
    cmd_param = '\n'.join(['='.join([k, "'"+v+"'"]) for k, v in parameters.items()])

    with open(os.path.join(os.path.dirname(__file__),"scripts", script_name)) as file:
        script_content = file.read()
    # merge duration
    script_content = cmd_param + "\n" + script_content

    return script_content
