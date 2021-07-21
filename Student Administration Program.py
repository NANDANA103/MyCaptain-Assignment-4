#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv


def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["NAME", "AGE", "CLASS", "SECTION", "CONTACT NUMBER", "E-MAIL ID"])
        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1

    while condition:
        student_info = input(
            "Enter student information for student #{} in the following format(Name Age Class Section Contact_Number E-mail Id): ".format(
                student_num))
        student_info_list = student_info.split(' ')

        print(
            "\nThe entered information is-\nName: {}\nAge: {}\nClass: {}\nSection: {}\nContact_Number: {}\nE-mail Id: {}"
            .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3],
                    student_info_list[4], student_info_list[5]))
        print(' ')

        info_check = input("Is the entered information correct(Yes/No): ")
        if info_check == 'Yes':
            write_into_csv(student_info_list)

            condition_check = input("Do you want to enter information for another student (Yes/No): ")
            print(' ')
            if condition_check == "Yes":
                condition = True
                student_num += 1
            else:
                condition = False
        else:
            print("\nKindly re-enter the values!")

# In[ ]:
