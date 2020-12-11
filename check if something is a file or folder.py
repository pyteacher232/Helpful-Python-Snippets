import os

folder_name = 'Result'

# unless folder_name exists, creates a folder
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

result_file_name = 'Result/result.csv'
if os.path.isfile(result_file_name):
    fp = open(result_file_name, 'w', encoding='utf-8')