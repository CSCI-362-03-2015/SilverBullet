import sys
import re
import subprocess
import webbrowser



sys.path.append("../") #changes the path so new directories can be added
from os import listdir
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
    
    
    
def findMethod(fileName):
    
    test = fileName.read()
    
    lis= re.findall(r"[\s][\w]+[.]+[\)]", test)
    
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
    
def testReq(fileName):
    test= fileName.readlines()

    return test[3]
    
    
def firstTable():
    
        
    string ="""  <table style="width:100%">
  <tr>
    <th>Test Number</th>
    <th>Test Requirements</th>		
    <th>Tested Method</th>
    <th>Inputs</th>		
    <th>Tested Excuable file</th>
    <th>Excepted Outcome</th>		
    <th>Oracle</th>
    <th>Pass/Fail</th>
  </tr>
  
  <p>"""
    
    
    return string
        
        
def tableRow(TestNum,Tr,Tm, testInput, TestFiles, outputs,OracleV, passFail):
        
    string= """<tr>
        <td>%s</td>
        <td>%s</td>		
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>		
        <td>%s</td>
        <td>%s</td>		
        <td>%s</td>
        </tr>""" % (TestNum,Tr,Tm, testInput, TestFiles, outputs, OracleV, passFail)
    
    return string
    
def endTable():
        
    string="""   

        </p>
        
        </div>

        <div id="footer">

        </div>

        </body>
        </html>"""
    
    return string

################################################################
#####Main
#########################################################################
def runAllTest():
    
       
 
    path="/home/jameson/TestAutomation/testCases/"    
    os.chdir(path)
    dirs = os.listdir(path)
    pyFiles =[]
    pyInput =[]
    testMethodL=[]
    dirs= sorted(dirs)
    #########################################
    for file in dirs:
        if file.find("~") != -1:
            continue
        
        else:
            fil = open(file, "r")
        
            inPut= findTestInput(fil)
            
            
            
            pyInput.append(inPut)
       
    print "here ",pyInput
   ######################################## 
    for file in dirs:
        if file.find("~") != -1:
            continue     
        else:
            fil = open(file, "r")
        
            
            ExeFile= findPyfile2(fil)
            
            pyFiles.append(ExeFile)
                
        
   
    
   
   ##########################################
   
   ######################################## 
    #for file in dirs:
      #  if file.find("~") != -1:
      #      continue     
        #else:
           # fil = open(file, "r")
        
            
            #mFile= findMethod(fil)
            
           # testMethodL.append(mFile)
                
        
   
    
   
   ##########################################
    sys.path.insert(0,"/home/jameson/TestAutomation/testCaseExecutables/")
    name= newDir(dirs)
    
    for i in range(len(dirs)):
        print(pyInput[i])
        arg = pyInput[i].split(",")
        importedM = __import__(pyFiles[i])
        
        
        exceptedO = importedM.test(eval(arg[0]),eval(arg[1]))
        oPath= "/home/jameson/TestAutomation/Output/"+ name[i]+"Output.txt"
        
        outfile =open(oPath,"w")
        outfile.write(str(exceptedO))
        
        outfile.close()
        
  ##########################################  
    pathORACLE="/home/jameson/TestAutomation/oracles/"
    pathOutput="/home/jameson/TestAutomation/Output/"
        
    oraclesFiles= newDir(sorted(os.listdir(pathORACLE)))
    outputFiles= newDir(sorted(os.listdir(pathOutput)))
    
    
    
    outputList=[]#outputs
    oracleList=[]#OracleV
    resultList=[]#pass/Fail
        
    for i in range(len(outputFiles)):
        orContents=open("/home/jameson/TestAutomation/oracles/"+oraclesFiles[i],"r")
        
        outContents=open("/home/jameson/TestAutomation/Output/"+outputFiles[i],"r")
        OutcontentString=outContents.read()
        OracleString= orContents.read()
        
        oracleList.append(OracleString)
        outputList.append(OutcontentString)
 
        
        if eval(OracleString) == eval(OutcontentString):
            print "pass"
            resultList.append("Pass")
        else:
            print" fail"
            resultList.append("Fail")
        
    hPath= "/home/jameson/TestAutomation/reports/report.html"
    htmlfile = open(hPath, "w")
    
    htmlfile.write("""
    
     <!DOCTYPE html>
           <html>
            <head>
                <style>
                #header {
                 background-color:black;
                 color:white;
                  text-align:center;
                 padding:5px;
                    }
      

                #section {
                  width:350px;
                  float:center;
                    padding:10px;	
                    text-align:left; 	
     
}
                    #footer {
                     background-color:black;
                     color:white;
                    clear:both;
                    text-align:center;
    
                        padding:5px;	 	 
                        }

                        table, th, td {
                         border: 1px solid black;
                         border-collapse: collapse;
                        }
                        th, td {
                          padding: 5px;
                          text-align: left;
                        }
                        </style>
                         </head>
                          <body>

                        <div id="header">
                        <h1>Silver Bullets</h1>
                        </div>



                        <div id="section">
                        <h2>Test Report</h2>""")
                        
    htmlfile.close()
    with open(hPath,"a") as htmlfile:
        htmlfile.write(firstTable())
        for i in range(len(pyFiles)):
            fileN= open(path+"testCase"+str(i+1),"r")
            htmlfile.write(tableRow(i+1,testReq(fileN),"add(x , y)", pyInput[i], pyFiles[i]+".py", outputList[i],oracleList[i], resultList[i]))
        htmlfile.write(endTable())
        htmlfile.close()
        
        
        url= "file:///home/jameson/TestAutomation/reports/report.html"
        webbrowser.open(url)
        
   
    
    
    
    
    
 
    
        
        
        
    
    
    
    
    #newS = pyFiles[0]+".py " + x[0] +""+x[1]
    #print newS
    
   # os.chdir("/home/jameson/TestAutomation/testCaseExecutables/")
    
    
   # p= subprocess.Popen(newS, shell=True)
    
    #os.system(newS)
    
    
    
    
    
    
    
    
    
    


    


runAllTest()
    
    
    
    
