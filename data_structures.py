''' Lesson on Data Collection 

Lists           []          Ordered Data
Tuples          ()          Ordered Collection of Data  "locked in"
Sets            {}          Unordered Data
Dictionaries    {key:value} Unordered collection of data; ("associative array")

"ARRAYS ALWAYS START AT 0"
'''

search_user = 'sykohpath'


list_example = ['sykohpath', 'ironchristr', 'RWDion']

list_example.append('streamlabs')

print( "List Example:", list_example )

user = list_example.pop(2)

print( "Popped User:", user )

list_example.sort() # sort ascending
print( "List Example (ascending):", list_example )
list_example.reverse() # sort descending
print( "List Example (descending):", list_example )

print( "List Example (final):", list_example )

print( "How many times " + search_user + " appears: ", list_example.count(search_user))


# ===========================
tuple_example = ('sykohpath', 'ironchristr', 'RWDion', 'sykohpath')

#tuple_example.add('streamlabs') #AttributeError: 'tuple' object has no attribute 'add'
# You can't add/remove with tuples

print( "Tuple Example:", tuple_example )

print( "How many times " + search_user + " appears: ", tuple_example.count(search_user))
# ===========================
set_example = {'sykohpath', 'ironchristr', 'RWDion', 'sykohpath'} # Sets don't allow duplicates!

print( "Set Example (begin):", set_example )

set_example.add('streamlabs')

user = set_example.pop() # grabs a random user from the "unordered" set

print( "User (pop):", user )

print( "Set Example (final):", set_example )

# ===========================

dictionary_example = [{'red':'sykohpath', 'blue':'ironchristr', 'green':'RWDion', 'black':'garbage'}] # key->value pair is "unique"

print( "Dictionary Example (begin):", dictionary_example )

for row in dictionary_example:
    status = row # copies the *reference* to the list
    status = row.copy() # copies the actual fricking list
    print(row['red'])
    status['red'] = 'AteoCeritus'
    print(row['red'])

exit()




dictionary_example.update({'yellow':'streamlabs'})

user = dictionary_example.pop('blue')

print( "User (pop):", user )

keys_list = list(dictionary_example.keys()) # convert keys to a list
keys_list.sort()

print("Keys (list): ", keys_list) # sort

sorted_dict = {} # empty
for key in keys_list:
    print( dictionary_example[key] )
    sorted_dict.update( {key:dictionary_example[key]} )

print( "Dictionary Example (sorted):", sorted_dict )

print( "Dictionary Example (final):", dictionary_example )
