#!/bin/bash

if [ -z "$process_name" ]; then
    echo "Please provide process name."
    exit 1
fi

pid=$(ps -ef | grep $process_name | grep -v 'grep' | awk '{ print $2 }' | head -n 1)
experiment=$(killall $signal $pid)

ret=$?
if [ $ret -eq 0 ]; then
    echo "experiment killall_processes -> processes <$process_name> on <$instance_id>: success"
else
    echo "experiment killall_processes -> processes <$process_name> on <$instance_id>: fail"
fi
#Sleep $duration
sleep $duration
