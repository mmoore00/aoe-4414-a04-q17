# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converts Gregorian calendar date to Fractional Julian date
# 
# Parameters:
#  Y: Gregorian year
#  M: Gregorian month
#  D: Gregorian day
#  h: Gregorian hour
#  m: Gregorian minute
#  s: Gregorian second
#  
# Output:
#  Print the Fractional Julian date
#
# Written by Matthew Moore
# Other contributors: none
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import math # math module
import sys # argv

# helper functions         

def int_div(l):
    if (l > 0):
        return math.floor(l)
    if (l == math.floor(l)):
        return l
    return math.ceil(l)

# initialize script arguments
JDf = float('nan')

# parse script arguments
if len(sys.argv)==7:
    Y = float(sys.argv[1])
    M = float(sys.argv[2])
    D = float(sys.argv[3])
    h = float(sys.argv[4])
    m = float(sys.argv[5])
    s = float(sys.argv[6])
else:
    print('Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km ')
    exit()

# write script below this line

# insert JDfractional equation, utilizing int_div method that ensures "Division is integer division with truncation toward zero"
JD = D - 32075 + int_div(int_div(1461 * (Y + 4800 + int_div((M - 14)/12)))/4) + int_div(int_div(367 * (M - 2 - int_div((M - 14)/12) * 12))/12) - int_div(int_div(3 * int_div((Y + 4900 + int_div((M - 14)/12))/100))/4)
JDmidnight = JD - 0.5
Dfractional = (s + 60.0*(m+60.0*h))/86400.0
JDf = JDmidnight + Dfractional

print(JDf)
