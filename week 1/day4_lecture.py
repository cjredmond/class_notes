# input 1 = "string"
# input 2 = "l"
# input 3 = [6,7]

sentence = "i decided to learn how to program and it was a good decision"
letter = "p"
output = []

for current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)

# string interpolation
# action = "eats"
# other_act = "plays"
# string = "Connor {} and {}".format(action, other_act)
#
# string2 = "Connor {0} and {1}".format(action, other_act)
#
# print(string)
# print(string2)

mad_lib = """ Dear {name}, I am {action}ing you to {other_action} you to
{action_three} your {noun}.


"""
print(mad_lib.format(name="Connor", action="writ", other_action="inform",
                     action_three="get lost", noun="face"))
marker_action = "erase"
print("Markers are difficult to %s" % marker_action)









print(output)
