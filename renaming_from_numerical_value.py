import os
import json

# Load modelling.json
with open('mapping.json', 'r') as f:
    modelling_data = json.load(f)

# Path to the directory containing unlabeled images
unlabeled_directory = r'E:\Camera Roll\jpg'  # Adjust the path to your images

# Rename folders based on modelling.json
for folder_name, numerical_label in modelling_data.items():
    numerical_label_str = str(numerical_label)
    old_folder_path = os.path.join(unlabeled_directory, numerical_label_str)
    
    if os.path.exists(old_folder_path):
        new_folder_path = os.path.join(unlabeled_directory, folder_name)
        os.rename(old_folder_path, new_folder_path)
