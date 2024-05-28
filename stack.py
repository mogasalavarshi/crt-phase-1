def push(stack,ele):
    stack.append(ele)
    print(ele, "inserted into stack successfully")
def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return
    print(stack[-1], "deleted successfully")
    stack.pop()
    
stack = []
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,90)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)


