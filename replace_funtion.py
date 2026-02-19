letter = '''
Dear <|Name|>,
you are selected!
<|Date|>
'''

new_letter = letter.replace("<|Name|>","Mrudula")
new_letter = new_letter.replace("<|Date|>","24 Nov 2025")
print(new_letter)