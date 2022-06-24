def f1():
    print('파라미터와 리턴값이 없는 함수')

def f2(num):
    print('입력받은 숫자:',num)

def f3(name, age):
    print('당신의 이름은:',name)
    print('당신의 나이는:',age)

def f4(name, age):
    msg = '당신의 이름은: '+name+' / 당신의 나이는: '+str(age)
    return msg

def f5(name, age):
    return name, age    #리턴값이 여러개인 하나의 튜플로 반환함

f1()
f2(3)
f3('aaa',31)
hola = f4('bbb',12)
print(hola)
amigo = f5('ccc',24)
print(amigo)

print(type(amigo))
print('name:',amigo[0],' age:',amigo[1])