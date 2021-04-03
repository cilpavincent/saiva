
# open_list = ["[","{","("]
# close_list = ["]","}",")"]

def check(myStr):
    
    open_list = ["[","{","("]
    close_list = ["]","}",")"]

    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack)>0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                print("False")
                return False
    
    if len(stack) == 0:
        print("True")
        return True
    else:
        print("False")
        return False
        

# string = '{[]{()}}'
# print(check(string))

# string = '[{}{})(]'
# print(check(string))

# string = '((()'
# print(check(string))