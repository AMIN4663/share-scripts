new_dict={'appel':60,'benana':40,'orange':45,'grapes':80}

new_dict_price={key:value-(value*0.1)for key,value in new_dict.items() if value>50}

print(new_dict_price)