a = ("a","b","1","2","c")
string = filter(str.isalpha,a)
number = filter(str.isdigit,a)
print(*string)
print(*number)