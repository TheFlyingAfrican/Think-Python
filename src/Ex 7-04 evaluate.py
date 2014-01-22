def evaluate():
    data = ''
    while data != 'done':
        data = input('please input some data: \n')
        print (eval(str(data)))
    
evaluate()
    