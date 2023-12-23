import os
import shutil
import scipy.io

# Load imagelabels.mat
mat_data = scipy.io.loadmat('imagelabels.mat')
labels = mat_data['labels'].flatten()  # Ensure labels is a 1D array

# Path to the directory containing unlabeled images
unlabeled_directory = r'E:\Camera Roll\jpg'  # Adjust the path to your images

# Assuming labels and image filenames are in the same order
for i, label in enumerate(labels):
    numerical_label = str(label)
    # Adjust the filename pattern based on your data
    image_filename = f'image_{i + 1:05d}.jpg'
    image_path = os.path.join(unlabeled_directory, image_filename)

    # Check if the image file exists before moving
    if os.path.exists(image_path):
        category_directory = os.path.join(unlabeled_directory, numerical_label)
        os.makedirs(category_directory, exist_ok=True)

        # Move the labeled image to the corresponding directory
        shutil.move(image_path, os.path.join(
            category_directory, image_filename))
