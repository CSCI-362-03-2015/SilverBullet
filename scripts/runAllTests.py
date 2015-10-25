import sys
import re
import subprocess



sys.path.append("../") #changes the path so new directories can be added
from os import listdir
from os.path import isfile, join
import os

    
#def findPyfile(fileName):

  #  test2 = fileName.readlines()
   # pyfile=""
   # print test2
    
   # for i in test2:
    #    if i.find("py")  != -1:
            
      #      return i 
                      
   # return " No file in this Test Case "
    
def findTestInput(fileName):
    
    test = fileName.read()
    
    lis= re.findall(r"[\w|\S|.|W]+ [\,] .+", test)
    
    return lis[0]
    
 
    
def findPyfile2(fileName):

    test = fileName.read()
    
    start =test.find('TestCase') 
    end = test.find('.py',start) 
    
    return test[start:end]
    
def newDir(dirs):
    newDir=[]
    for file in dirs:
        if file.find("~") != -1:
            continue     
        else:
            newDir.append(file)
    
    
    return newDir


def runAllTest():
    #path="/home/jameson/TestAutomation/"
    #dirs=listdir(path )   
        
    #for file in dirs:
       # print file
       
 
    path="/home/jameson/TestAutomation/testCases/"    
    os.chdir(path)
    dirs = os.listdir(path)
    pyFiles =[]
    pyInput =[]
    
    #########################################
    for file in dirs:
        if file.find("~") != -1:
            continue
        
        else:
            fil = open(file, "r")
        
            inPut= findTestInput(fil)
            ExeFile= findPyfile2(fil)
            
            
            pyInput.append(inPut)
       
    #print pyInput
   ######################################## 
    for file in dirs:
        if file.find("~") != -1:
            continue     
        else:
            fil = open(file, "r")
        
            
            ExeFile= findPyfile2(fil)
            
            pyFiles.append(ExeFile)
                
        
    #print pyFiles
    
   
   ##########################################
    sys.path.insert(0,"/home/jameson/TestAutomation/testCaseExecutables/")
    name= newDir(dirs)
    
    for i in range(len(dirs)):
        arg = pyInput[i].split(",")
        importedM = __import__(pyFiles[i])
        
        exceptedO = importedM.test(eval(arg[0]),eval(arg[1]))
        oPath= "/home/jameson/TestAutomation/Output/"+ name[i]+"Output.txt"
        
        outfile =open(oPath,"w")
        outfile.write(str(exceptedO))
        
        outfile.close()
        
  ##########################################  
    
    
    
    
    
    #newS = pyFiles[0]+".py " + x[0] +""+x[1]
    #print newS
    
   # os.chdir("/home/jameson/TestAutomation/testCaseExecutables/")
    print os.getcwd()
    
   # p= subprocess.Popen(newS, shell=True)
    
    #os.system(newS)
    
    
    
    
    
    
    
