from enum import Enum
import threading
import psutil
import datetime
import os
import json

class Status:
    not_started = "not_started"
    running = "running"
    failed = "failed"


class ServiceStatus:
    # Module-level variables, to hold the date that the app was started
    _lock = threading.Lock()
    _start_time = datetime.datetime.now()

    def __init__(self, status, operations, exceptions):
        self.status = status
        self.operations = operations
        self.exceptions = exceptions


    def update(self, status, operations_successful = 0, operations_failed = 0):
        self.status = status
        self.operations += operations_successful
        self.exceptions += operations_failed
        self._update()


    def _update(self):
        self.datetime = datetime.datetime.now()
        self.working_set = ServiceStatus.memory_usage_psutil()
        with ServiceStatus._lock:
            self.uptime_seconds = (datetime.datetime.now() - ServiceStatus._start_time).total_seconds


    def memory_usage_psutil():
        # return the memory usage in MB
        process = psutil.Process(pid=os.getpid())
        mem = process.memory_info()[0] / float(2 ** 20)
        return mem
