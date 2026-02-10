"""
RGB til YCrCb-fargeområdet
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load the image
image = mpimg.imread('minions.jpg')

print(f"Shape: {image.shape}")
print(f"Data type: {image.dtype}")
w = image.shape[1]
h = image.shape[0]

# Lager tre tomme arrayer med 32-bit presisjon for tallene.
Y = np.zeros((h,w),dtype=np.float32)
Cr = np.zeros((h,w),dtype=np.float32)
Cb = np.zeros((h,w),dtype=np.float32)
image_back = np.zeros((h,w,3),dtype=np.float32)


def rgb_til_yuv_manuell():
    for y in range(h):
        for x in range(w):
            # Forward conversion
            Y[y][x] = image[y][x][0] * 0.299 + image[y][x][1] * 0.587 + image[y][x][2] * 0.114
            Cb[y][x] = 128 - 0.169*image[y][x][0] - 0.331*image[y][x][1] + 0.5*image[y][x][2]
            Cr[y][x] = 128 + 0.5*image[y][x][0] - 0.419*image[y][x][1] - 0.081*image[y][x][2]
            
            # Inverse conversion
            image_back[y][x][0] = Y[y][x] + 1.403*(Cr[y][x]-128)
            image_back[y][x][1] = Y[y][x] - 0.344*(Cb[y][x]-128) - 0.714*(Cr[y][x]-128)
            image_back[y][x][2] = Y[y][x] + 1.773*(Cb[y][x]-128)

    # Begrens alle verdiene til 0-255 og sett dem til datatype uint-8 (8-bits positive heltall).
    Y = np.clip(Y, 0, 255).astype(np.uint8)
    Cb = np.clip(Cb, 0, 255).astype(np.uint8)
    Cr = np.clip(Cr, 0, 255).astype(np.uint8)
    image_back = np.clip(image_back, 0, 255).astype(np.uint8)

"""
Rask metode for å beregne YUV-fargene benytter matriseregning. MYE raskere.
Må først gjøre om arrayene til en annen fasong for å utføre beregningene.
# Original image shape: (2, 3, 3) - 2x3 image with RGB channels
original = np.array([
    [[R1,G1,B1], [R2,G2,B2], [R3,G3,B3]],  # First row of pixels
    [[R4,G4,B4], [R5,G5,B5], [R6,G6,B6]]   # Second row of pixels
])

# After reshape(-1, 3): (6, 3) - 6 pixels, each with 3 values
reshaped = np.array([
    [R1, G1, B1],  # Pixel 1
    [R2, G2, B2],  # Pixel 2
    [R3, G3, B3],  # Pixel 3
    [R4, G4, B4],  # Pixel 4
    [R5, G5, B5],  # Pixel 5
    [R6, G6, B6]   # Pixel 6
])
"""
# RGB to YUV transformation matrix
RGB_to_YUV = np.array([
    [ 0.299,     0.587,     0.114   ],  # Y
    [-0.168736, -0.331264,  0.5     ],  # U (Cb)
    [ 0.5,      -0.418688, -0.081312]   # V (Cr)
], dtype=np.float32)

# YUV to RGB transformation matrix (inverse of above)
YUV_to_RGB = np.array([
    [1.0,  0.0,      1.402   ],  # R
    [1.0, -0.344136, -0.714136],  # G  
    [1.0,  1.772,    0.0     ]   # B
], dtype=np.float32)

# Offset values for U and V channels (128 for 8-bit)
UV_OFFSET = 128.0

def rgb_to_yuv(rgb_image):
    """Convert RGB to YUV using the exact same method as OpenCV"""
    # Ensure input is float32
    rgb_float = rgb_image.astype(np.float32)
    
    # Reshape for matrix multiplication: (H*W, 3)
    # -1 betyr "calculate this dimension automatically": reshape(-1, 3) becomes (240*320, 3) = (76800, 3)
    h, w, c = rgb_float.shape
    rgb_reshaped = rgb_float.reshape(-1, 3)
    
    # Tar prikkprodukt mellom konverteringsmatrisen og arrayet vårt med RGB-verdier.
    yuv_reshaped = np.dot(rgb_reshaped, RGB_to_YUV.T)
    
    # Legger til eller trekker fra offset pga YUV er fra -127-127 i pixelverdier.
    yuv_reshaped[:, 1] += UV_OFFSET  # U channel
    yuv_reshaped[:, 2] += UV_OFFSET  # V channel
    
    # Reshape back to original image shape
    yuv_image = yuv_reshaped.reshape(h, w, c)
    
    # Clip values to valid range [0, 255]
    yuv_image = np.clip(yuv_image, 0, 255)
    
    return yuv_image.astype(np.uint8)

def yuv_to_rgb(yuv_image):
    """Convert YUV to RGB using the exact same method as OpenCV"""
    # Ensure input is float32
    yuv_float = yuv_image.astype(np.float32)
    
    # Subtract offset from U and V channels
    yuv_float[:, :, 1] -= UV_OFFSET  # U channel
    yuv_float[:, :, 2] -= UV_OFFSET  # V channel
    
    # Reshape for matrix multiplication: (H*W, 3)
    h, w, c = yuv_float.shape
    yuv_reshaped = yuv_float.reshape(-1, 3)
    
    # Apply transformation matrix
    rgb_reshaped = np.dot(yuv_reshaped, YUV_to_RGB.T)
    
    # Reshape back to original image shape
    rgb_image = rgb_reshaped.reshape(h, w, c)
    
    # Clip values to valid range [0, 255]
    rgb_image = np.clip(rgb_image, 0, 255)
    
    return rgb_image.astype(np.uint8)

image_yuv = rgb_to_yuv(image)
image_back = yuv_to_rgb(image_yuv)


# Display the image
plt.imshow(image_back)
plt.title("image back")
plt.axis('off')
plt.show()