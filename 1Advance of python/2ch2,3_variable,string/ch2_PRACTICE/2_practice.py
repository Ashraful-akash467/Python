'''
 2. Write a program to fill in a letter template given below with name and date.
letter = 
Dear <|Name|>,
You are selected!
<|Date|>

 '''



later='''Dear <|Name|>,
You are selected 
<|Date|>'''

print(later.replace("<|Name|>","Akash").replace("<|Date|>","2/8/2024"))         