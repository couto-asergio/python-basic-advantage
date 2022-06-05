"""
    Dictionary
"""

released = {
  "iphone": 2007,
  "iphone 3G": 2008,
  "iphone 3GS": 2009,
  "iphone 4": 2010,
  "iphone 4S": 2011,
  "iphone 5": 2012
  }

print(released)


# Add a value to the dictionary
# the syntax is: mydict[key] = "value"
released["iphone 5S"] = 2013
print(released)


# Remove a key and it’s value
# You can remove an element with the del operator
del released["iphone"]
print(released)

# Check the length
print(len(released))


# Test the dictionary
# Check if a key exists in a given dictionary by using the 
# in operator like this:

for item in released:
    if "iphone 5" in released:
        print("Key found")
        break
    else:
        print("No keys found")


# Get a value of a specified key
print(released.get("iphone 3G", "none"))

# Print all keys with a for loop
print("-" * 10)
print("iphone releases so far: ")
print("-" * 10)

for release in released:
    print(release)


# Print all key and values
for key, val in released.items():
    print(key, "=>", val)


# Sorting the dictionary
# In addition to printing, let’s sort the data so we 
# have an expected output.

for key, value in sorted(released.items()):
    print(key, value)

