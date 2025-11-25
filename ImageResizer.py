import os
from PIL import Image
import argparse

class ImageResizer:
    def __init__(self, input_folder, output_folder, new_size=(800, 600), output_format='JPEG'):
        """
        Initialize the Image Resizer
        
        Args:
            input_folder (str): Path to folder containing input images
            output_folder (str): Path to folder where resized images will be saved
            new_size (tuple): Target size as (width, height)
            output_format (str): Output format ('JPEG', 'PNG', etc.)
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.new_size = new_size
        self.output_format = output_format
        
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    
    def get_supported_formats(self):
        """Return list of supported image formats"""
        return ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    
    def resize_single_image(self, image_path, output_path):
        """
        Resize a single image and save it
        
        Args:
            image_path (str): Path to input image
            output_path (str): Path for output image
        """
        try:
            # Open the image
            with Image.open(image_path) as img:
                # Resize the image
                resized_img = img.resize(self.new_size, Image.Resampling.LANCZOS)
                
                # Convert to RGB if saving as JPEG (JPEG doesn't support transparency)
                if self.output_format.upper() == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
                    resized_img = resized_img.convert('RGB')
                
                # Save the resized image
                resized_img.save(output_path, self.output_format)
                print(f"✓ Resized: {os.path.basename(image_path)} -> {os.path.basename(output_path)}")
                
        except Exception as e:
            print(f"✗ Error processing {image_path}: {str(e)}")
    
    def batch_resize_images(self):
        """
        Resize all images in the input folder and save to output folder
        """
        supported_formats = self.get_supported_formats()
        processed_count = 0
        
        print(f"Starting batch image resizing...")
        print(f"Input folder: {self.input_folder}")
        print(f"Output folder: {self.output_folder}")
        print(f"Target size: {self.new_size}")
        print(f"Output format: {self.output_format}")
        print("-" * 50)
        
        # Iterate through all files in input folder
        for filename in os.listdir(self.input_folder):
            # Check if file is a supported image format
            if any(filename.lower().endswith(fmt) for fmt in supported_formats):
                input_path = os.path.join(self.input_folder, filename)
                
                # Create output filename with new format
                name_without_ext = os.path.splitext(filename)[0]
                output_filename = f"{name_without_ext}.{self.output_format.lower()}"
                output_path = os.path.join(self.output_folder, output_filename)
                
                # Resize the image
                self.resize_single_image(input_path, output_path)
                processed_count += 1
        
        print("-" * 50)
        print(f"Batch processing completed! Processed {processed_count} images.")
    
    def get_image_info(self, image_path):
        """
        Get basic information about an image
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            dict: Image information
        """
        try:
            with Image.open(image_path) as img:
                return {
                    'filename': os.path.basename(image_path),
                    'format': img.format,
                    'size': img.size,
                    'mode': img.mode
                }
        except Exception as e:
            return {'error': str(e)}

def main():
    """Main function to run the image resizer"""
    parser = argparse.ArgumentParser(description='Batch Image Resizer Tool')
    parser.add_argument('--input', '-i', default='input_images', 
                       help='Input folder containing images (default: input_images)')
    parser.add_argument('--output', '-o', default='output_images', 
                       help='Output folder for resized images (default: output_images)')
    parser.add_argument('--width', '-w', type=int, default=800, 
                       help='Target width (default: 800)')
    parser.add_argument('--height', '-ht', type=int, default=600, 
                       help='Target height (default: 600)')
    parser.add_argument('--format', '-f', default='JPEG', 
                       choices=['JPEG', 'PNG', 'BMP', 'GIF'], 
                       help='Output format (default: JPEG)')
    
    args = parser.parse_args()
    
    # Create resizer instance
    resizer = ImageResizer(
        input_folder=args.input,
        output_folder=args.output,
        new_size=(args.width, args.height),
        output_format=args.format
    )
    
    # Perform batch resizing
    resizer.batch_resize_images()

# Example usage without command line arguments
def simple_example():
    """Simple example without command line arguments"""
    resizer = ImageResizer(
        input_folder='input_images',
        output_folder='output_images',
        new_size=(800, 600),
        output_format='JPEG'
    )
    resizer.batch_resize_images()

if __name__ == "__main__":
    # Check if command line arguments are provided
    import sys
    if len(sys.argv) > 1:
        main()
    else:
        print("No command line arguments provided. Using default settings...")
        simple_example()