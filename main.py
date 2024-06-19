# check if data_copied file is exist or not if not we will create file and name it data_copied.txt
# get data from data_copied.txt file
# assign it in dictionary
# save_function and append data at data_copied.txt
# load_function
# list to get all data in dictionary
import os
import clipboard


def save_data():
    key = input("enter a key ").lower()
    value = clipboard.paste()
    data = open(txt_file_loc, "a")
    data.write(f"{key}|{value}\n")
    data.close()
    print("Data Saved")


def load_data(load_data):

    while True:
        if load_data.lower() in data.keys():
            clipboard.copy(data[load_data])
            return data[load_data]
            break
        else:
            load_data = input("Enter key correctly")
            continue


txt_file_loc = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

txt_file_loc = txt_file_loc + "\data.txt"# create a txt file and name it data.txt

data = {}

try:  # to create the file
    data_file = open(txt_file_loc, "x")

except:  # to assign data inside file at variable data
    for line in open(txt_file_loc):
        data.update({line.split("|")[0]: line.split("|")[1]})


print('''
[1] => to save data you have copied
[2] => to load specific text you have copied before
[3] => to get list of all data you have copied before
''')

while True:
    user_input = input("choose what do you want. ")
    if user_input == "1":  # to save data
        save_data()
        break
    elif user_input == "2":  # to load data
        key = input("enter the key ")
        print(load_data(key))
        break
    elif user_input == "3":
        print(data)
        break
    else:
        print("Please enter the instruction you need correctly")
