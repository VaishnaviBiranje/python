class student:
    _name =None
    _roll =None
    _branh= None

    def __init__ (self,name,roll,branch):
        self._name = name
        self._roll = roll
        self._branch=branch

    def _displayRollAndBranch(self):
        print("roll:",self._roll)
        print("branch:",self._branch)


