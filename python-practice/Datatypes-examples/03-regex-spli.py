import re

text= "apple,banana,orange,grape"
pattern= r","
split_text= re.split(pattern,text)
print("Split text is:",split_text)
