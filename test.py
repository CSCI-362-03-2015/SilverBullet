import re
import os

def runAllTest():

	print ("string" - "hi")
	#print os.getcwd()
	
	
# 	print "jameson jdkfjaklsdjlfjkadsjklfjl;ajsdjfj"
# 	for i in range (26):

# 		if (i >=6):
# 			string = "TestCase%d.py" % i
# 			fil= open("/home/jameson/TestAutomation/testCaseExecutables/"+string,'w')
# 			fil. write("""import sys
# from sys import argv
# #pythonpath is the default path.
 

# sys.path.append("../project/src/") #changes the path so new directories can be added

# from functions import *


# def testDriver(x, y):
    
	
#     # Calculates the results of the add method.
# 	try:
		
# 		result= add(x, y)
		
		
# 		return result
            
            
# 	except TypeError:
# 		result= "TypeError"
		
# 		return result""")
# 			fil.close()
    
    


runAllTest()








# import sys
# import re
# import webbrowser
# from os import listdir
# import os
# import helper

    
    
# ################################################################
# #####Main
# ################################################################
# def main():
         
#     testCasesPath="/home/jameson/TestAutomation/testCases/"   

#     os.chdir(testCasesPath)#changes current directory 

#     testCaseList = helper.filterDir(sorted(os.listdir(testCasesPath)))# Store a list of files in the directory

#     pyFiles =[]# List to store py execuable file
#     pyInput =[]# List of inputs for each testCase file
#     testMethodList=[]# list of methods for each testCase
#     testReqs=[]# List of Tested Requirements from each file testCase file

    
#     ################################################
#     for file in testCaseList: 
        
#         fil = open(file, "r")

#         string = fil.read()

#         pyFiles.append(helper.findPyfiles(string))       
#         pyInput.append(helper.findTestInput(string))
#         testMethodList.append(helper.findMethod(string))
#         testReqs.append(helper.findRequire(string))
        
#         fil.close()
       
#    # ################################################ 
#    #  for file in testCaseList:

#    #      fil2 = open(file, "r")
           
#    #      ExeFile= helper.findPyfiles(fil2)         
#    #      pyFiles.append(ExeFile)

#    #      fil.close()
                
#    # #################################################
#    #  for file in testCaseList:

#    #      fil3= open(file, "r")

#    #      Require= helper.findRequire(fil3)
#    #      testReqs.append(Require)
   
#    #      fil.close()
   
#    # ##########################################
#    #  for file in testCaseList:

#    #      fil4= open(file, "r")

#    #      methods= helper.findMethod(fil4)
#    #      testMethodList.append(methods)
   
#    #      fil.close()


#    # ##########################################


#     sys.path.insert(0,"/home/jameson/TestAutomation/testCaseExecutables/")
#     for i in range(len(testCaseList)):
        
#         arg = pyInput[i].split(",")
#         importedM = __import__(pyFiles[i])
        
        
#         exceptedOutput = importedM.test(eval(arg[0]),eval(arg[1]))
#         oPath= "/home/jameson/TestAutomation/Output/"+ testCaseList[i]+"Output.txt"
        
#         outfile =open(oPath,"w")
#         outfile.write(str(exceptedOutput))
        
#         outfile.close()
        
#   ##########################################  

#     pathOracle="/home/jameson/TestAutomation/oracles/"
#     pathOutput="/home/jameson/TestAutomation/Output/"
        
#     oraclesFiles= helper.filterDir(sorted(os.listdir(pathOracle)))# Creates a list of the files in the oracle directory
#     outputFiles= helper.filterDir(sorted(os.listdir(pathOutput))) #Creates a list of the files in the Output directory
    
    
    
#     outputList=[]#List of contents in each output file
#     oracleList=[]#List of contents in each oracle file
#     resultList=[]#List of Pass/Fail
        
#     for i in range(len(outputFiles)):

#         oracleContents=open(pathOracle+oraclesFiles[i],"r") #opens oracle file
        
#         outContents=open(pathOutput+outputFiles[i],"r")# opens output put file

#         OracleString= oracleContents.read() #reads oracle file

#         OutcontentString=outContents.read()#reads output file
        
        
#         oracleList.append(OracleString)
#         outputList.append(OutcontentString)
 
        
#         #Compares the tested result with the oracle 
#         #and appends Pass to $resultList if they are equal 
#         #and Fail if not
#         if eval(OracleString) == eval(OutcontentString):
            
#             resultList.append("Pass")
#         else:
            
#             resultList.append("Fail")


#     # creates a html file and write to it.   
#     helper.writeHtml()# see method
    
    
#     # appends  to the report.html file
#     with open("/home/jameson/TestAutomation/reports/report.html","a") as htmlfile:
#         htmlfile.write(helper.firstTableRow())

#         #Creates a row in the table for each test case
#         for i in range(len(pyFiles)):


#             #Create a row in the table and writes in the data from the lists
#             htmlfile.write(helper.addTableRow(i+1,testReqs[i],testMethodList[i], pyInput[i], pyFiles[i]+".py", outputList[i],oracleList[i], resultList[i]))

#         #writes the closing to the  file html(</html>)     
#         htmlfile.write(helper.endHtml())

#         htmlfile.close()
        
        
#     url= "file:///home/jameson/TestAutomation/reports/report.html"
        
#     webbrowser.open(url)
        

# main()

# import sys
# import re
# import webbrowser
# from os import listdir
# import os

# def findTestInput(stringFile):
    
#     lis= re.findall(r"[\w|\S|.|W]+ [\,] .+", stringFile)
    
#     return lis[0]
       
    
# def findMethod(stringFile):
    
    
#     lis= re.findall(r" .+\(.+\)", stringFile)
    
#     return lis[0]
    
# def findRequire(stringFile):

    
#     lis =re.findall(r"TestedRequirement:.+", stringFile)
    
#     return lis[0]
    
# def findPyfiles(stringFile):

#     lis= re.findall(r" TestC.+\.py", stringFile)
     
#     return lis[0]
    
# def filterDir(testCaseList):
#     filteredList=[]
#     for file in testCaseList:
#         if file.find("~") != -1:
#             continue     
#         else:
#             filteredList.append(file)
     
#     return filteredList
    
# def writeHtml():

#     htmlfile = open("/home/jameson/TestAutomation/reports/report.html", "w")
#     htmlfile.write("""
    
#      <!DOCTYPE html>
#            <html>
#             <head>
#                 <style>
#                     #header {
#                         background-color:black;
#                         color:white;
#                         text-align:center;
#                         padding:5px;
#                             }
      
#                     #section {
#                         width:350px;
#                         float:center;
#                         padding:10px;   
#                         text-align:left;    
     
#                              }
                   

#                     table, th, td {
#                         border: 5px solid black;
#                         border-collapse: collapse;
#                                     }
#                     th, td {
#                           padding: 5px;
#                           text-align: left;
#                         }
#                 </style>
#             </head>
#             <body>

#                         <div id="header">
#                         <h1>Silver Bullets</h1>
#                         </div>



#                         <div id="section">
#                         <h2>Test Report</h2>""")
                        
#     htmlfile.close()
    
    
# def firstTableRow():
    
        
#     string =""" <p> <table style="width:100%">
#   <tr>
#     <th>Test Number</th>
#     <th>Test Requirements</th>		
#     <th>Tested Method</th>
#     <th>Inputs</th>		
#     <th>Tested Executable file</th>
#     <th>Test Results</th>		
#     <th>Oracle</th>
#     <th>Pass/Fail</th>
#   </tr>
  
#   """
    
    
#     return string
        
        
# def addTableRow(TestNum,Tr,Tm, testInput, TestFiles, outputs,OracleV, passFail):
        
#     string= """<tr>
#         <td>%s</td>
#         <td>%s</td>		
#         <td>%s</td>
#         <td>%s</td>
#         <td>%s</td>		
#         <td>%s</td>
#         <td>%s</td>		
#         <td>%s</td>
#         </tr>""" % (TestNum,Tr,Tm, testInput, TestFiles, outputs, OracleV, passFail)
    
#     return string
    
# def endHtml():
        
#     string="""   

#         </p>
        
#         </div>

#         <div id="footer">
            
#         </div>

#         </body>
#         </html>"""
    
#     return string
