name_input = input("enter names ")

name_list = name_input.split(',')

#print(name_list)

filtered_name = sorted([ name for name in name_list  if len(name) > 3 and name[0].lower() == "a" ])