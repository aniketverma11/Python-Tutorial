#!/usr/bin/env python
import re
import os

def rearrange_name(name):
    result  = re.search(r"^([\w.]*),([\w.]*)$", name)
    return "{} {}".format(result[2], result[1])