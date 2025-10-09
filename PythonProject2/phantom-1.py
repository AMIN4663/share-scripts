name_input = input("enter names ")

name_list = name_input.split(',')
print(name_list)
filtered_name = [ name for name in name_list  if len(name) > 3 and name[0].lower() == "a" ]
print(filtered_name)
#git@github.com:AMIN4663/share-scripts.git
