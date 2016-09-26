print("Connor" + " programming")
#print("Connor" + 1) -> error
print("Connor " + str(1))

class SuperNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return SuperNumber(str(self.value) + str(other.value))

    def __str__(self):
        return str(self.value)

s_number_1 = SuperNumber(1)
s_number_2 = SuperNumber("Connor")
x = s_number_1 + s_number_2 + s_number_1
print(x)
#
