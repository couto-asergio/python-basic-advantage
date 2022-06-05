"""
For in
iterating string with for
range(start=0, stop, step=1)
"""
text = 'python'
new_string = ''

for letter in text:
    if letter == 't':
        new_string = new_string + letter.upper()
    elif letter == 'h':
        new_string += letter.upper()
        break
    else:
        new_string += letter

print(new_string)