'''This module provides various time-related functions. For related functionality,
 see also the datetime and calendar modules.

Although this module is always available, not all functions are available on all platforms.
Most of the functions defined in this module call platform C library functions with the same name.
 It may sometimes be helpful to consult the platform documentation,
  because the semantics of these functions varies among platforms.

An explanation of some terminology and conventions is in order.

The epoch is the point where the time starts. On January 1st of that year, at 0 hours,
 the “time since the epoch” is zero. For Unix, the epoch is 1970. To find out what the epoch is, look at gmtime(0).

The functions in this module do not handle dates and times before the epoch or far in the future.
The cut-off point in the future is determined by the C library; for Unix, it is typically in 2038.
'''
'''
The time value as returned by gmtime(), localtime(), and strptime(), and accepted by asctime(), mktime() and strftime(), is a sequence of 9 integers. The return values of gmtime(), localtime(), and strptime() also offer attribute names for individual fields.


The module defines the following functions and data items:

time.accept2dyear
Boolean value indicating whether two-digit year values will be accepted. This is true by default, but will be set to false if the environment variable PYTHONY2K has been set to a non-empty string. It may also be modified at run time.
time.altzone
The offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Only use this if daylight is nonzero.
time.asctime([t])
Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a 24-character string of the following form: 'Sun Jun 20 23:21:05 1993'. If t is not provided, the current time as returned by localtime() is used. Locale information is not used by asctime().

Note Unlike the C function of the same name, there is no trailing newline.
time.clock()
On Unix, return the current processor time as a floating point number expressed in seconds. The precision, and in fact the very definition of the meaning of “processor time”, depends on that of the C function of the same name, but in any case, this is the function to use for benchmarking Python or timing algorithms.

On Windows, this function returns wall-clock seconds elapsed since the first call to this function, as a floating point number, based on the Win32 function QueryPerformanceCounter. The resolution is typically better than one microsecond.

time.ctime([secs])
Convert a time expressed in seconds since the epoch to a string representing local time. If secs is not provided or None, the current time as returned by time() is used. ctime(secs) is equivalent to asctime(localtime(secs)). Locale information is not used by ctime().
time.daylight
Nonzero if a DST timezone is defined.
time.gmtime([secs])
Convert a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero. If secs is not provided or None, the current time as returned by time() is used. Fractions of a second are ignored. See above for a description of the struct_time object. See calendar.timegm() for the inverse of this function.
time.localtime([secs])
Like gmtime() but converts to local time. If secs is not provided or None, the current time as returned by time() is used. The dst flag is set to 1 when DST applies to the given time.
time.mktime(t)
This is the inverse function of localtime(). Its argument is the struct_time or full 9-tuple (since the dst flag is needed; use -1 as the dst flag if it is unknown) which expresses the time in local time, not UTC. It returns a floating point number, for compatibility with time(). If the input value cannot be represented as a valid time, either OverflowError or ValueError will be raised (which depends on whether the invalid value is caught by Python or the underlying C libraries). The earliest date for which it can generate a time is platform-dependent.
time.sleep(secs)
Suspend execution for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time. The actual suspension time may be less than that requested because any caught signal will terminate the sleep() following execution of that signal’s catching routine. Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.
time.strftime(format[, t])
Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. If t is not provided, the current time as returned by localtime() is used. format must be a string. ValueError is raised if any field in t is outside of the allowed range.

0 is a legal argument for any position in the time tuple; if it is normally illegal the value is forced to a correct one.

The following directives can be embedded in the format string. They are shown without the optional field width and precision specification, and are replaced by the indicated characters in the strftime() result:

'''





#formatted time

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#time using localtime

import time
t = time.localtime()
print(time.asctime(t))

#extract month

import datetime
d=datetime.date.today()
print(d.month)

#exract day

import datetime
d=datetime.date.today()
print(d.day)

#extract date

import datetime
d=datetime.date.today()
print(d.day)

#factorial

import math
num=int(input("enter the number"))
print("the factorial of entered number is : ",end="")
print(math.factorial(num))


#gcd

def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd
a = 23
b = 29
print("The gcd  is : ", end="")
print(computeGCD(23,29))


#use o.s. package
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

#import os
for a in os.environ:
    print('Var: ', a, 'Value: ', os.getenv(a))
print("all done")