#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

        
        
    

    if year == 1918:
        return("26.09."+str(year))

    elif year in range(1700,1918):
        if year % 4 == 0:
            return("12.09."+str(year))
        return("13.09."+str(year))
    elif year in range(1919,2701):
        if year % 400 == 0:
            return(("12.09."+str(year)))

        elif year % 4 == 0 and year % 100 != 0:
            return(("12.09."+str(year)))

        else:
            return(("13.09."+str(year)))
   


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)
