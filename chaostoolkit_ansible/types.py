# -*- coding: utf-8 -*-
from typing import Any, Dict

__all__ = ["AnsibleResponse"]

# really dependent on the type of resource called
AnsibleResponse = Dict[str, Any]
