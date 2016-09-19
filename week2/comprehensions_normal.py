from statistics import mean
with open("data.txt") as better_open_file:
    data = better_open_file.read()


data = data.split("\n")

new_list = []

for x in range(0,31):
    new_list.append(data[x].split(","))




water_temps = []
for row in new_list:
    water_temps.append(row[4])
water_floats = [float(x) for x in water_temps if not x == "Water Temp"]

farenheit = [int((x*1.8) + 32) for x in water_floats]


# date_height = {x[5]: x[1] for x in new_list}
# print(date_height)

def date_height(list):
    return {x[5]: x[1] for x in list}
#print(date_height(new_list))


gradebook = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
             'Jordan': {'Homework 1': 92, 'Homework 2': 87},
             'Peyton': {'Homework 1': 84, 'Homework 2': 77},
             'River': {'Homework 1': 85, 'Homework 2': 91}}
def grade_avg(gradebook):
    return mean([(value['Homework 1']) for key, value in gradebook.items()])


#print(grade_avg(gradebook))
# print(water_temps)
# print(water_floats)
# print(farenheit)
# print(date_height)



sentence = "List comprehensions are the Greatest!"

vowel = "aeiou"
for item in sentence:
    if item in vowel:
        sentence = sentence.replace(item, "")
print(sentence)
