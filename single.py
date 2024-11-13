class A:
    def fun_l(self):
        print("this function is defind inside the person class")
class B(A):
    def fun_2(self):
        print("this function inside the child class.")

object = B()
object.fun_l()
object.fun_2()
