immutable_var = 1,2,3,4, True, 'sport'
print('Immutable tuple:', immutable_var)
 #immutable_var[1]= 45,   File "C:\Users\Елена\PycharmProjects\pythonProject10\'module_1_5.py'.py", line 3
    #immutable_var[1]= 45
#IndentationError: unexpected indent

mutable_list=[7,9,11,'pen', False]
mutable_list[3]=275
print('Mutable list:',mutable_list)