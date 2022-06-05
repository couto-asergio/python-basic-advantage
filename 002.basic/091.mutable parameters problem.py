"""
Mutable Parameters Problem
Mutable: List, Dictionary
Immutable: Tuples, Strings, number, True, False, None
"""

def list_client(client_iterable, lista=[]):
  list.extend(client_iterable)
  return list

client1 = list_client(['john', 'Mary', 'Oliver'])
client2 = list_client(['john', 'Mary', 'Zic'])

print(client1)
print(client2)
