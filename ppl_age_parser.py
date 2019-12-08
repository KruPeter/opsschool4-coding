This is my homework:
import json
import yaml

jsonString = '{"Dan": 102, "Dana": 2, "Danail": 5, "Dandre": 29, "Dane": 75, "Daneel": 22, "Danell": 57, "Dangelo": 35, "Danger": 11, "Danial": 25, "Danian": 82, "Daniel": 45, "Daniele": 23, "Danielius": 76, "Daniil": 23, "Danijel": 75, "Danilo": 25, "Daniyal": 45, "Danner": 25, "Dannie": 65, "Dannin": 25, "Danny": 52, "Dante": 57, "Dantes": 21, "Danuel": 47, "Danut": 82, "Danyal": 90, "Danyl": 55}'
ppl_list = json.loads(jsonString)
age_0_11 = []
age_11_20 = []
age_20_25 = []
age_25_40 = []
age_40_103 = []
for name, age in ppl_list.items():
    if 0 < age < 11:
        age_0_11.append(name)
    elif 11 <= age < 20:
        age_11_20.append(name)
    elif 20 <= age < 25:
        age_20_25.append(name)
    elif 25 <= age < 40:
        age_25_40.append(name)
    else:
        age_40_103.append(name)

print('People Names between age 0-11:\n', yaml.dump(age_0_11))
print('People Names between age 11-20:\n', yaml.dump(age_11_20))
print('People Names between age 20-25:\n', yaml.dump(age_20_25))
print('People Names between age 25-40:\n', yaml.dump(age_25_40))
print('People Names between age 40-103:\n', yaml.dump(age_40_103))


