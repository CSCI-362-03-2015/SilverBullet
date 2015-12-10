import sys
import re
import webbrowser
from os import listdir
import os

def findTestInput(stringFile):
    
    lis= re.findall(r"[\w|\S|.|W]+ [\,] .+", stringFile)
    
    return lis[0]
       
    
def findMethod(stringFile):
    
    
    lis= re.findall(r" .+\(.+\)", stringFile)

    
    return lis[0]
    
def findRequire(stringFile):

    
    lis =re.findall(r"Returns.+", stringFile)
    
    return lis[0]
    
def findPyfiles(stringFile):

    lis= re.findall(r"TestC.+\.py", stringFile)
     
    return lis[0]
    
def filterDir(testCaseList):
    filteredList=[]
    for file in testCaseList:
        if file.find("~") != -1:
            continue     
        else:
            filteredList.append(file)
     
    return filteredList
    
def writeHtml():

    htmlfile = open("../reports/report.html", "w")
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
                   

                    table, th, td {
                        border: 5px solid black;
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
                        <h1>SilverBullet</h1>
                        </div>



                        <div id="section">
                        <h2>Test Report</h2>""")
                        
    htmlfile.close()
    
    
def firstTableRow():
    
        
    string =""" <p> <table style="width:100%">
  <tr>
    <th>Test Number</th>     
    <th>Tested Method</th>
    <th>Inputs</th>     
    <th>Tested Executable file</th>
    <th>Test Results</th>       
    <th>Oracle</th>
    <th>Pass/Fail</th>
  </tr>
  
  """
    
    
    return string
        
        
def addTableRow(TestNum,Tm, testInput, TestFiles, outputs,OracleV, passFail):
        
    string= """<tr>
        <td>%s</td>
        <td>%s</td>     
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>     
        <td>%s</td>
        <td>%s</td>     
        
        </tr>""" % (TestNum,Tm, testInput, TestFiles, outputs, OracleV, passFail)
    
    return string
    
def endHtml():
        
    string="""   

        </p>
        
        </div>

        <div id="footer">
            
        </div>

        </body>
        </html>"""
    
    return string