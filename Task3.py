from PIL import Image  # type: ignore
import numpy as np
import pandas as pd
from Functions.GUIrequest import open_image_file

def Detect_Finger_Pressure(image_path):
    # Load and process the image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Error while opening image: ",e)    

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
        width, height = image.size
        
        img_data_porttion = image.crop((width//2, 0, width, height))
        # Crop (left, top, right, bottom)
        fingers = [img_data_porttion.crop((0, 0, width//2, height//10)),
                   img_data_porttion.crop((0,height//5.5,width//2,height//3.6)),
                   img_data_porttion.crop((0,height//3.3,width//2,height//2.5)),
                   img_data_porttion.crop((0,height//2.2,width//2,height//1.8)),
                   img_data_porttion.crop((0,height//1.8,width//2,height//1.03))]
        
        pressure = []
        
        for finger in fingers:
            pixels = finger.load()
            height, width = finger.size
            arr_mean = []
            for x in range(height):
                for y in range(width):
                    r,g,b = pixels[x,y]
                    if r >= 10 and g >= 125 and b >= 240:
                        arr_mean.append(1)
                    else:
                        arr_mean.append(0)
            finger_pressure = round(float(np.mean(arr_mean)),4)
            if finger_pressure >= 0.004:
                pressure.append(1)
            else:
                pressure.append(0)

        return pressure
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
