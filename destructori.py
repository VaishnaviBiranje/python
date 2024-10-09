class employee:
    def __init__(self):

        print('employee created!')
    
    def __del__(self):
        print('Destructor is called,Employee deleted!')
    
       
obj = employee()
del obj