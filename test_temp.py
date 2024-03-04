
def format_string(str_in):
    str_list = str_in.split('\n')
    str_out =""
    for row in str_list:
        str_out +="\t\t"+row+"\n"
    return str_out


str1 = "line2\n""line 2\n""line 3"


print(str1)

print(format_string(str1))

