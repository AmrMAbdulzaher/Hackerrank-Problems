#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n in range(1,101):
        if n%2!=0 or (n%2==0 and n in range(6,21) ):
            print("Weird")
        else:
            print("Not Weird")