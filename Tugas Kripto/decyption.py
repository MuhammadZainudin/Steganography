from PIL import Image
def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def extract_text_from_image(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())
    
    binary_data = ''
    
    for pixel in pixels:
        for color in pixel[:3]:  
            binary_data += str(color & 1)
            if binary_data.endswith('1111111111111110'):
                binary_data = binary_data[:-16]  
                return binary_to_text(binary_data)
    
    return binary_to_text(binary_data)

hidden_image_path = r'D:\Kuliah\Semester 5\Kriptografi\Steganography\steganography_with_text.png'

hidden_text = extract_text_from_image(hidden_image_path)
print(f"Teks tersembunyi: {hidden_text}")
