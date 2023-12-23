# 102_oxford_flower_prediction
This Image Classification model helps you to recognized 102 kinds of flowers that are provided my Oxford University. I am using famous 102 oxford flower dataset. 

# Steps of Building this Image Classification Model

1. Selecting Dataset
2. Data Pre-processing
3. Model Traning & Trialing
4. Deploying

## Selecting Dataset
To get the actual raw dataset, go to this site: https://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html
After thet, download Dataset image zip file that contains 8k+ images for 102 categories of flowers. But, the thing is, the entire dataset is unlabeled & we need to label it through algorithmic techniques. With the help of imagelabels.mat file, we have to do the entire process. 

## Data Pre-processing 

This is the most challenging part in entire project. We have imagelabels.mat file that contains image mapping sequntially. But the problem is no name is given there. So, based on the sequence, I have to manually set the name by the taking help of this link: https://www.robots.ox.ac.uk/~vgg/data/flowers/102/categories.html

After that I have to create a json file containing flower names & sequence for 102 categories of flowers named mapping.json. 

In the 3rd step, I have written Pthon script to labelling these flowers dataset based on imagelabels.mat file data. 

After labelling, I have written another 2nd script to rename from numerical value to their actual name. 

Finally, the dataset is ready to model training stage. 

The dataset is available on google drive: https://drive.google.com/drive/folders/1DHTzI-2UQg1nwjLd9iY6GjveezmDy2cG?usp=sharing 


## Model Training & Trialing 

After that, dataset is being used at training stage with Resnet 50. You can check Flower_Model_Data_preprocessing.ipynb file for more details. After trail & training, the model has achieved 96% valid accuracy. 

The trained model on Resnet50: https://drive.google.com/file/d/1-J3MplpNWdhGo5NZVc5N9SW7N_sLdWgC/view?usp=sharing

## Deploying

Model is deployed at huggingface: https://huggingface.co/spaces/tdnathmlenthusiast/flower_classifier
