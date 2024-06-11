# -*- coding: utf-8 -*-

str1 = "-+-+-+"
str2 = "-+-+-+"

print(f"String 1: {str1}")
print(f"String 2: {str2}")
print("")

str1_list = []
str2_list = []
neu_list = []

for i in str1:
    str1_list.append(i)

for i in str2:
    str2_list.append(i)
    
for i in range(len(str1)):
    if str1[i] == "+" and str2[i] == "+":
        neu_list.append("+")
    elif str1[i] == "-" and str2[i] == "-":
        neu_list.append("-")
    else:
        neu_list.append("0")
        
neu_str = "".join(neu_list)
print(f"Neutralisation: {neu_str}")