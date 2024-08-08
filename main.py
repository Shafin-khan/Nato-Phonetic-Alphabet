
''' Example related to this project
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
     #Access key and value
    # print(key)
    # print(value)

#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     # print(index)
#     print(row.student)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}'''

# #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
import pandas
'''
Made by me!
# nato_p_a_df = pandas.read_csv('nato_phonetic_alphabet.csv')
# # print(nato_p_a_df)
# letter = nato_p_a_df['letter'].to_list()
#
# code = nato_p_a_df['code'].to_list()
#
# dict_l_c = {letter[i]:code[i] for i in range(len(letter))}
# print(dict_l_c)'''

data = pandas.read_csv('nato_phonetic_alphabet.csv')
# letter = data.letter.to_list()
#
# code = data.code.to_list()
dict_data = {row.letter: row.code for (index, row) in data.iterrows()}



# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input('Enter Your Name: ').upper()
# u_letters = list(user_word)
# print(u_letters)
output_list = [dict_data[letter] for letter in user_word]
print(output_list)

