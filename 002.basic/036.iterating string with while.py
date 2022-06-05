"""
036. Iterating string with while
"""
phrase = 'The mouse gnawed the clothes of the king of rome'
len_phrase = len(phrase)
counter = 0
new_string = ''

while counter < 10:
    new_string += phrase[counter]
    print(new_string)
    counter += 1

print(new_string)