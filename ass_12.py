#1
'''An access token is an object encapsulating the security identity of a process or thread.
A token is used to make security decisions and to store tamper-proof information about some system entity.
While a token is generally used to represent only security information, it is capable of holding additional
free-form data that can be attached while the token is being created.

it is of two types:-
1.Impersonation token
2.primary token'''


#2
import socket
print (socket.gethostbyname('google.com'))


#3

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

#4

'''API is part of library that defines how it will interact with external code.
Every library has API, API is sum of all public/exported stuff. Nowadays meaning of API is widened.
we might call the way web site/service interact with code as API also.
You can also tell that some device has API - the set of commands you can call.

Sometimes this terms can be mixed together. For example you have some server app (like TFS for example). 
It has API with it, and this API is implemented as a library. 
But this library is just a middle layer between you and not the one who executes your calls. 
But if library itself contains all action code then we can't say that this library is API'''

'''Library is a set of all classes and functions that can be used from our code to do our task easily.
But the library can contain some of its private functions for its usage which it does not want to expose.

API is a part of library which is exposed to the user.
So whatever documentation we have regarding a library,
we call it an API Documentation because it contains only those classes and functions to which we have access'''



#5
import winsound
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

