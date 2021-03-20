a = 5

def change_a ():
    global a
    a = 6

change_a()
print(a)