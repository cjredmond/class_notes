def adder(number_one, number_two, message="No message Passed", happy=True):
    print(message)
    print(happy)
    return print(number_one + number_two)
#print(adder(12, 900))

adder("Connor", "programming", "Do math", happy=False)
adder("programming", "Connor")

def add(*args):
    return (sum(args))
print(add(1,5,16,304,2))

print(add(*[9,4]))

print(add(*range(100)))

def beginners_luck(name, account_number, *args, **kwargs):

    print(args)
    print(kwargs)
    return 1

print(beginners_luck("Connor", 4124412414, 1,1,3,4,41,4,4,4,1,"string", True, thing = "hi", monday = True))
