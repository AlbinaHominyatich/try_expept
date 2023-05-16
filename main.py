try:
    print("start code")
    print(error)
    print("end")
except:
    print("no problems")
print("any code..")

def checker(var):
    if type(var) != str:
        raise TypeError(f'Ми не працюємо з {type(var)}, нам треба str')
    else:
        return var
a = '1234'
checker(a)
