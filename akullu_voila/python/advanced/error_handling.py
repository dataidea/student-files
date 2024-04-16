def greet(name=''):
    if name == '':
        raise Exception('No name specified')
    return f'Hello {name}'

message = greet()
print(message)
