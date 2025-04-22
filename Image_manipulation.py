import os
import sys
from PIL import Image, ImageFilter


def display_menu():
    print("Available Operations")
    print("1: GrayScale Conversion")
    print("2: Rotate Image")
    print("3: Crop Image")
    print("4: Resize Image")
    print("5: Make Thumbnail")
    print("0: Exit")

def grayscale_image(image):
    return image.convert("L")

def rotate_image(image,angel):
    return image.rotate(angel)

def crop_image(image, dimensions):
    left, upper, right, lower = map(int, dimensions)
    box = (left, upper, right, lower)
    return image.crop(box)

def resize_image(image, dimensions):
    width, height = map(int, dimensions)
    return image.resize((width, height))

def thumbnail_image(image, dimensions):
    width, height = map(int, dimensions)
    thumbnail_copy = image.copy()
    thumbnail_copy.thumbnail((width, height))
    return thumbnail_copy



if __name__ == "__main__":

    image_folder = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    while True:
        display_menu()
        choice = input("Enter Operation Number (0 to exit):")


        if choice == "1":
            image_name = input("Enter Image name:")
            image_path = os.path.join(image_folder,image_name)
            img = Image.open(image_path)
            modified_image = grayscale_image(img)
            output_path = os.path.join(output_folder,"grayscale " + image_name)
            modified_image.save(output_path)
            print("GrayScale Image Saved ",output_path)

        elif choice == "2":
            image_name = input("Enter Image name:")
            image_path = os.path.join(image_folder,image_name)
            img = Image.open(image_path)
            image_angel = int(input("Enter angel in degrees:"))
            modified_image = rotate_image(img,image_angel)
            output_image = 'resized_image' + image_name
            output_path = os.path.join(output_folder,output_image)
            modified_image.save(output_path)
            print(f"Image Rotated to {image_angel} Saved ",output_path)

        elif choice == "3":
            image_name = input("Enter image name:")
            image_path = os.path.join(image_folder,image_name)
            img = Image.open(image_path)

            image_dim = input("Enter Dimensions separated by comma:")
            image_dimensions = image_dim.split(',')
            modified_image = crop_image(img,image_dimensions)
            output_path = os.path.join(output_folder,'cropped'+ image_name)
            modified_image.save(output_path)
            print(f"Cropped Image Saved ", output_path)

        elif choice == "4":
            image_name = input("Enter image name:")
            image_path = os.path.join(image_folder,image_name)
            img = Image.open(image_path)

            image_dim = input("Enter Dimensions separated by comma:")
            image_dimensions = image_dim.split(',')
            modified_image = resize_image(img,image_dimensions)
            output_path = os.path.join(output_folder,'resized' + image_name)
            modified_image.save(output_path)
            print(f"Cropped Image Saved ", output_path)

        elif choice == "5":
            image_name = input("Enter image name:")
            image_path = os.path.join(image_folder,image_name)
            img = Image.open(image_path)

            image_dim = input("Enter Dimensions separated by comma:")
            image_dimensions = image_dim.split(',')
            modified_image = thumbnail_image(img,image_dimensions)
            output_path = os.path.join(output_folder,'thumbnail' + image_name)
            modified_image.save(output_path)
            print(f"Thumbnail Image Saved ", output_path)

        elif choice == "0":
            break
        
        else:
            print("Invalid choice. Please enter valid number.")


