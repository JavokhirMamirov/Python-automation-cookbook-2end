import os
import re

################ Print all filenames in the dir

# for root, dirs, files in os.walk('dir'):
#     for file in files:
#         print(file)

################## Print full path of the files

# for root, dirs, files in os.walk('dir'):
#     for file in files:
#         full_file_path = os.path.join(root, file)
#         print(full_file_path)

################ Print only .pdf files

# for root, dirs, files in os.walk('dir'):
#     for file in files:
#         if file.endswith('.pdf'):
#             full_file_path = os.path.join(root, file)
#             print(full_file_path)


################ Print only files that contain an even number

# for root, dirs, files in os.walk('documents\dir'):
#     for file in files:
#         if re.search(r'[13579]', file):
#             full_file_path = os.path.join(root, file)
#             print(full_file_path)