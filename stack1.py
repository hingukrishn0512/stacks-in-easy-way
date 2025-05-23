#dabba ni andar jovu hoy badhu sarkhu che ke nai to stack kaam lage
#complex problem maths ma jemke 3+2+(52-53)+5 aava problrms ghana bahda
#ama   push pop and peek ave 
#stack is empty list pachi badhu ani andar add katu java nu
#push atle upar jodvu pop atle kadhvu peek atle khali jovu


stack = []

stack.append(5)
stack.append(15)
stack.append(55)

print(f"stack after the pushing is {stack}")


stack.pop()

print(f'stack after pop {stack}')


if stack:
    print(f"the view of the top is {stack[-1]}")

else:
    print("there is no list ")