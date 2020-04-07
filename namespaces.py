namespaces = {'global': None}
variables = {}

def get(namespace,arg):
    #ищем аргумент arg в значениях ключа неймспейса. если такого значения нет, смотрим родительскую переменную ключа
    #неймспейса и ищем переменную в ней и т.д. пока он не найдется, или будет значение none
    if not namespace in variables:
        return None
    else:
        if arg in variables[namespace]:
            return namespace
        else:
            return get(namespaces[namespace], arg)


while True:
    cmd, namespace, arg = input().split()
    if not namespace in variables:
        variables[namespace] = []
    if cmd == 'create':
        namespaces[namespace] = arg
    elif cmd == 'add':
        if namespace in namespaces:
            variables[namespace].append(arg)
        else:
            print('there is no', namespace, 'in namespaces. Create it first')
    elif cmd == 'get':
        print(get(namespace, arg))

