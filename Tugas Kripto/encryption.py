from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def embed_text_in_image(image_path, text, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())
    
    binary_text = text_to_binary(text) + '1111111111111110'  
    
    if len(binary_text) > len(pixels) * 3:
        raise ValueError("Gambar terlalu kecil untuk menyimpan teks biner.")
    
    new_pixels = []
    idx = 0

    for pixel in pixels:
        r, g, b = pixel
        if idx < len(binary_text):
            r = (r & ~1) | int(binary_text[idx])  
            idx += 1
        if idx < len(binary_text):
            g = (g & ~1) | int(binary_text[idx])  
            idx += 1
        if idx < len(binary_text):
            b = (b & ~1) | int(binary_text[idx])  
            idx += 1
        new_pixels.append((r, g, b))

    new_pixels.extend(pixels[len(new_pixels):])
    
    img.putdata(new_pixels)
    img.save(output_path)
    print(f"Teks berhasil disembunyikan dalam gambar. Disimpan sebagai {output_path}")

input_image_path = r'D:\Kuliah\Semester 5\Kriptografi\Steganography\steganography.jpg'
output_image_path = r'D:\Kuliah\Semester 5\Kriptografi\Steganography\steganography_with_text.png'

embed_text_in_image(input_image_path, 'Dandadan', output_image_path)
