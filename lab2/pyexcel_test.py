import pyexcel
from collections import OrderedDict 

#int()

# prepare data
dic = [OrderedDict({"Name": "Duc",
"age": 5}), 
OrderedDict({'Name': 'Kien', 
'age':6})

]
# List comprehension 
#save file 
pyexcel.save_as(records=dic, dest_file_name="Yes.xlsx")