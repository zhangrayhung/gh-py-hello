#!/usr/bin/env python3

import os
who = os.getenv("WHO", "Action")
print(f"Hello, {who} from GitHub Actions!")