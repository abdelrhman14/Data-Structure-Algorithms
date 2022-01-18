def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")
    
def pop(stack):
    return stack.pop()

def peek(stack):
    return stack[len(stack) - 1]

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")
print(peek(stack))
