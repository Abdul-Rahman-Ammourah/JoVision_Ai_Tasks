from PIL import Image  # type: ignore
import numpy as np
import pandas as pd
from Functions.GUIrequest import open_image_file

def Detect_Finger_Pressure(image_path):
    # Load and process the image
    image = Image.open(image_path)

    if image.mode != "RGB":
        image = image.convert("RGB")

    # Convert the image to a NumPy array
    img_array = np.array(image)

    # Green color for pressure detected 
    green_color = np.array([0, 255, 0])  
    
    # Create the bottom region of the image
    bottom_region = img_array[-1, :, :] 

    # Check if the green color is detected in the bottom region
    if np.mean(bottom_region == green_color) > 0.5:
        
        # Get the dimensions of the image
        height, width, _ = img_array.shape
        # Define the finger regions
        finger_regions = [
            (0, pressure_data.shape[1] // 5),
            (pressure_data.shape[1] // 5, 2 * pressure_data.shape[1] // 5),
            (2 * pressure_data.shape[1] // 5, 3 * pressure_data.shape[1] // 5),
            (3 * pressure_data.shape[1] // 5, 4 * pressure_data.shape[1] // 5),
            (4 * pressure_data.shape[1] // 5, pressure_data.shape[1])
        ]

        # Define the region where pressure data is located (right half of the image)
        pressure_data = img_array[:, width // 2:, :]
        finger_pressure = []
        
            

    else:
        return [0] * 5
    
def Save_To_Excel(data, file_name='finger_pressure_data'):
    file_name = file_name + '.xlsx'
    # Convert data to a DataFrame
    df = pd.DataFrame(data, columns=['Finger 1', 'Finger 2', 'Finger 3', 'Finger 4', 'Finger 5'])
    
    # Save to an Excel file
    df.to_excel(file_name, index=False)
    print(f"Data saved to {file_name}")

def main():
    try:
        # Open the image file
        image_path = open_image_file()
        if image_path:
            # Detect finger pressure
            finger_data = Detect_Finger_Pressure(image_path)
            print("Finger Pressure Data: ", finger_data)
            
            # Save the data to an Excel file
            Save_To_Excel([finger_data])
        else:
            print("Error: No image file selected.")
    
    except Exception as e:
        print("Error while processing image: ", e)

if __name__ == "__main__":
    main()
