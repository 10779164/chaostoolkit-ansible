#!/bin/bash

if [ -z "$process_name" ]; then
    echo "Please provide process name."
    exit 1
fi

pid=$(ps -ef | grep $process_name | grep -v 'grep' | awk '{ print $2 }' | head -n 1)
experiment=$(kill $signal $pid)

ret=$?
if [ $ret -eq 0 ]; then
    echo "experiment kill_process -> process <$process_name> on <host>: success"
else
    echo "experiment kill_process -> process <$process_name> on <host>: fail"
fi
#Sleep $duration
sleep $duration
