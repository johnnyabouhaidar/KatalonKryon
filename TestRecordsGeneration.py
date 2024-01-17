import random
import pandas as pd

names = ["Johnny","","name3","name4","name5"]
lastnames = ["Abou Haidar","","lname3","lname4","lname5"]
comments = ["sample comment1","test","hello",""]
files=[r"C:\users\johnny\file1.pdf",r"C:\users\johnny\file2.pdf",r"C:\users\johnny\file3.pdf",""]

#print(random.choice(names))
#print(random.choice(lastnames))

final_result = []

for i in range (100):
    final_result.append([random.choice(names),random.choice(lastnames),random.choice(comments),random.choice(files)])


print(final_result)
final_df=pd.DataFrame(final_result,columns=["name","fname","comment","file2upload"])
print(final_df)

final_df.to_excel("generated_output.xlsx",index=False)