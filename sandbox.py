# print("Welcome to Ops School, winter 2020")
# print(dir("aaa"))

# def sum_positive_numbers(num_list):
#     final_sum = 0
#     for index, num in enumerate(num_list):
#        print(num)
#        if num > 0:
#            final_sum += num
#      print(final_sum)
#
# if __name__ == '__main__':
#    list_of_numbers = [12, 2, -6, 34, 344, -8]
#    sum_positive_numbers(list_of_numbers)


# ppl_ages = {'david': 20, 'itsik': 30, 'yaron': 40, 'arie': 34}
# for name, age in ppl_ages.items():
#     if age >= 30:
#         print(name + " is older than 30")
#     else:
#         print(name + " is younger than 30")



# import json
ppl_ages = {"Dan": 102, "Dana": 2, "Danail": 5, "Dandre": 29, "Dane": 75, "test": 11, "test_2": 11, "test_3": 15}
# age_range = {20, 40, 25, 11}
for name, age in ppl_ages.items():
    if 0 < age <= 11:
        print("ages between 0-11" + " " + name)
    elif 11 < age <= 20:
        print("ages between 11-20" + " " + name)
    elif 20 < age <= 40:
        print("ages between 20-40" + " " + name)
    else:
        print("ages between 40-103" + " " + name)




