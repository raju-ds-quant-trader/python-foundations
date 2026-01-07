age =23
message ="wish you happy"+(age)+"rd birthday" 
print(message)
#the above program errorr because python wont take age in between strings as string 
#python can only concatinate string not integers 
# to make the above program work we have to onvert int to str by using str() function
age =23
message="i wish you a happy "+str(age)+"rd birthday"
print (message)