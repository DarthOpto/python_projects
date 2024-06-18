# list comprehension
# new_list = [new_item for item in list]
# numbers = [1, 2, 3]
# new_list = [n ** 2 for n in numbers]
# print(new_list)
#
# name = "Curtis"
# letter_list = [letter for letter in name]
# print(letter_list)
#
# range_list = [number * 2 for number in range(1, 5)]
# print(range_list)
#
# # Conditional List Comprehension
# # new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)

# List Comprehension Squaring Numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number ** 2 for number in numbers]
# print(squared_numbers)

# List Comprehension Filtering Even Numbers
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

# List Comprehension Data Overlap
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# result = [int(num) for num in list1 if num in list2]
# print(result)

# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)
#
#
# sentence = "What is the airspeed velocity of an unladen swallow?"
# result = {word: len(word) for word in sentence.split()}
#
# print(result)

# temp_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21}
#
# temp_f = {day: temp * 9/5 + 32 for (day, temp) in temp_c.items()}
# print(temp_c)
# print(temp_f)