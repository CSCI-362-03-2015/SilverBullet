import sys
from sys import argv
#pythonpath is the default path.
 

sys.path.append("../project/src/") #changes the path so new directories can be added

from functions import *


def testDriver(x, y):
    
	
    # Calculates the results of the mod method.
	try:
		
		result= mod(x, y)
		
		
		return result
            
            
	except TypeError:
		result= "TypeError"
		
	except ValueError:

		result= "ValueError"
		
		return result
