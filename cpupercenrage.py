#! /usr/bin/env python3.9

import psutil
d = psutil.cpu_percent(0.1)
print(d)
