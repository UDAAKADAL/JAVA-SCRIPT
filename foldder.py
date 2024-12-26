import os

for i in range(3, 21):
    folder_name = f"lec{i}"
    os.makedirs(folder_name)  # Create the folder

    # Create files in the folder
    with open(os.path.join(folder_name, "index.html"), "w") as f:
        pass  # You can add content here

    with open(os.path.join(folder_name, "index.js"), "w") as f:
        pass  # You can add content here

    with open(os.path.join(folder_name, "style.css"), "w") as f:
        pass  # You can add content here

print("Folders and files created successfully!")