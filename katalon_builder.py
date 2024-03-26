import pandas as pd
from imports import *
from webelement_template import *
from outputTCXML import *
from xmlparser import *
import os

input_file_path = 'input_output.xlsx'

final_result = ""

types_names = pd.read_excel(input_file_path,sheet_name="Sheet2", nrows=1).columns.tolist()
field_names = pd.read_excel(input_file_path,sheet_name="Sheet1", nrows=1).columns.tolist()
samples = pd.read_excel(input_file_path,sheet_name="Sheet1", nrows=2).iloc[0]
#print(samples[1])
#print(types_names)
try:
    os.rmdir("result")
except:
    pass
final_result=final_result+"{0}\n\n".format(imports)
final_result=final_result+"WebUI.openBrowser('')\n\n"
final_result=final_result+"WebUI.navigateToUrl('https://iss-mea-188510.workflowcloud.com/forms/f2998e48-ca76-4628-81cf-5ca4925fd2cb')\n\n"

UI_Objects = get_element_data('form.html')
for idx,typee in enumerate(types_names):

    try:
        os.mkdir("result")
        os.mkdir(r"result\CurrentApplication")
        os.mkdir(r"result\CurrentApplication\CurrentForm")
    except:
        pass

    if "Text"  in typee:
        final_result=final_result+"WebUI.{0}(findTestObject('{1}'),'{2}')\n\n".format("setText","Object Repository/CurrentApplication/CurrentForm/input_{0}".format(field_names[idx]),samples[idx])
        #print(web_element_template.format("input_{0}".format(field_names[idx])))
    if "MultiLine"  in typee:
        final_result=final_result+"WebUI.{0}(findTestObject('{1}'),'{2}')\n\n".format("setText","Object Repository/CurrentApplication/CurrentForm/textarea_{0}".format(field_names[idx]),samples[idx])        
    if "File" in typee:
        final_result=final_result+"WebUI.{0}(findTestObject('{1}'),'{2}')\n\n".format("uploadFile","Object Repository/CurrentApplication/CurrentForm/input_{0}".format(field_names[idx]),samples[idx].replace("\\","\\\\"))
    f = open(r"result\CurrentApplication\CurrentForm\input_{0}.rs".format(field_names[idx]), "w")
    try:
        f.write(web_element_template.format("input_{0}".format(field_names[idx]),UI_Objects[field_names[idx]]))
    except:
        pass

final_result=final_result+"WebUI.closeBrowser()"
print(final_result)

'''
try:
    os.rmdir("result")
except:
    pass'''

try:
    #os.mkdir("result")
    os.mkdir(r"result\finaloutput")
except:
    pass
f = open(r"result\finaloutput\finaloutput.groovy", "w")
f.write(final_result)


f = open(r"result\finaloutput.tc", "w")
f.write(outputTCXML)



