import random
import pandas as pd

targetted_excel = "generated_output.xlsx"

input_excel_df = pd.read_excel(targetted_excel,sheet_name="Sheet1")

names = input_excel_df.iloc[:,0]
lastnames = input_excel_df.iloc[:,1]
comments = input_excel_df.iloc[:,2]
files = input_excel_df.iloc[:,3]
'''
names = ["Johnny","","name3","name4","name5"]
lastnames = ["Abou Haidar","","lname3","lname4","lname5"]
comments = ["sample comment1","test","hello",""]
files='''

#print(random.choice(names))
#print(random.choice(lastnames))

final_result = []

for i in range (100):
    final_result.append([random.choice(names),random.choice(lastnames),random.choice(comments),random.choice(files)])


print(final_result)
final_df=pd.DataFrame(final_result,columns=["name","fname","comment","file2upload"])
print(final_df)

final_df.to_excel(targetted_excel,index=False)