# JoVision AI Tasks

## Task 1: Text Extraction from Image

### Description
Write a Python script that extracts text from an image. The script should prompt the user to enter the path to an image, then process the image to extract and display the text contained within it.

## Task 2: Convert Image to Grayscale Manually

### Description
Write a Python function that converts an image to grayscale manually, without using built-in grayscale functions from image processing libraries.

## Task 3: Finger Pressure Detection and Data Saving

### Description
Write a Python program that detects which fingers are holding an object from the provided images. Determine whether there is pressure on each finger based on image brightness and save the data to an Excel sheet.

## Task 4: Chess Piece Detection Using YOLOv5

### Description
Build a deep learning model using YOLOv5 to detect chess pieces in images. The model should classify the pieces into the following categories: 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'.

### Steps
1. **Data Preparation**: Load and preprocess the dataset.
2. **Model Training**: Train the YOLOv5 model on the dataset.
3. **Evaluation**: Evaluate the model's performance.

## Task 5: Data Augmentation and Model Re-Training

### Description
To address overfitting in the chess piece detection model, augment the dataset by flipping, rotating, and altering images. Retrain the model with the augmented dataset and compare its accuracy with the original model.

### Steps
1. **Data Augmentation**: Apply various augmentation techniques to the dataset.
2. **Retrain the Model**: Train the YOLOv5 model on the augmented dataset.
3. **Compare Accuracy**: Evaluate and compare the performance of the retrained model.

## Task 6: Image Classification Model Training and Testing

### Description
Train a classification model using the provided labeled data and test it with random images to evaluate its performance.

### Steps
1. **Data Preparation**: Load and preprocess the labeled data.
2. **Model Training**: Train a classification model on the labeled data.
3. **Testing**: Evaluate the model using the random images.
