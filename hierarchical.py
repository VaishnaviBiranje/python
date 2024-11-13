class parent:
    def fun_1(self):
        print("this function is define inside parent class.")

class child_1(parent):
    def fun_2(self):
        print("this function is define inside the class1.")

class child_2(parent):
    def fun_3(self):
        print("this function is define inside the class2.")   

ob1 =child_1()
ob2 =child_2() 
ob1.fun_1()
ob1.fun_2()
ob2.fun_1()
ob2.fun_3()