# import os

# for i in range(3, 21):
#     folder_name = f"lec{i}"
#     os.makedirs(folder_name)  # Create the folder

#     # Create files in the folder
#     with open(os.path.join(folder_name, "index.html"), "w") as f:
#         pass  # You can add content here

#     with open(os.path.join(folder_name, "index.js"), "w") as f:
#         pass  # You can add content here

#     with open(os.path.join(folder_name, "style.css"), "w") as f:
#         pass  # You can add content here

# print("Folders and files created successfully!")

# import os

# for i in range(1, 21):
# <<<<<<< HEAD
#     old_folder_name = f"lec{i}"
#     new_folder_name = f"lecture{i}"
# =======
#     folder_name = f"lec{i}"
#     os.makedirs(folder_name)  # Create the folder
# >>>>>>> 8b6a5531948ede8c57c1d7faf4a385d2c15ace93

#     try:
#         # Attempt to rename the folder
#         os.rename(old_folder_name, new_folder_name)

#         # Update file paths only if the folder rename was successful
#         for filename in os.listdir(new_folder_name):
#             old_file_path = os.path.join(old_folder_name, filename)
#             new_file_path = os.path.join(new_folder_name, filename)
#             os.rename(old_file_path, new_file_path)

#     except FileNotFoundError:
#         print(f"Folder 'lec{i}' might not exist. Skipping...")

# <<<<<<< HEAD
# print("Folders and files renamed successfully (if they existed).")
# =======
# print("Folders and files created successfully!")
# >>>>>>> 8b6a5531948ede8c57c1d7faf4a385d2c15ace93
