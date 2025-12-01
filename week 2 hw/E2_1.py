import numpy as np
import torch
from PIL import Image
import urllib.request
import os

# Step 1: Load an image with PIL.Image
print("=" * 60)
print("Task 1.1: Numpy to PyTorch and back")
print("=" * 60)

# Check if we have an image, if not download a sample image
image_path = "../data/sample_image.jpg"
if not os.path.exists(image_path):
    print("No image found, downloading a sample image...")
    os.makedirs("../data", exist_ok=True)
    # Download a sample image from PIL
    url = "https://raw.githubusercontent.com/pytorch/vision/main/gallery/assets/dog2.jpg"
    try:
        urllib.request.urlretrieve(url, image_path)
        print(f"Downloaded sample image to {image_path}")
    except Exception as e:
        print(f"Could not download image: {e}")
        print("Please provide an image in the data folder")
        exit(1)

# Load the image
pil_image = Image.open(image_path)
print(f"\n1. Loaded PIL.Image object: {type(pil_image)}")
print(f"   Image size: {pil_image.size} (width x height)")
print(f"   Image mode: {pil_image.mode}")

# Step 2: Convert to numpy array
numpy_array = np.array(pil_image)
print(f"\n2. Converted to numpy array")

# Step 3: Print the shape
print(f"   Shape: {numpy_array.shape}")

# Step 4: Print the dtype (should be uint8)
print(f"   Dtype: {numpy_array.dtype}")

# Step 5: Convert numpy array to PyTorch Tensor
pytorch_tensor = torch.from_numpy(numpy_array)
print(f"\n3. Converted to PyTorch Tensor")
print(f"   Tensor shape: {pytorch_tensor.shape}")
print(f"   Tensor dtype: {pytorch_tensor.dtype}")

# Step 6: Change dtype to float32
pytorch_tensor_float = pytorch_tensor.float()  # or .to(torch.float32)
print(f"\n4. Changed dtype to float32")
print(f"   New dtype: {pytorch_tensor_float.dtype}")

# Step 7: Calculate mean and standard deviation for R, G, B channels separately
# Image is in HWC format (Height, Width, Channels), need to work with channels
print(f"\n5. Calculating mean and std for each channel:")

# Method 1: Using indexing
r_channel = pytorch_tensor_float[:, :, 0]
g_channel = pytorch_tensor_float[:, :, 1]
b_channel = pytorch_tensor_float[:, :, 2]

r_mean = torch.mean(r_channel)
r_std = torch.std(r_channel)
g_mean = torch.mean(g_channel)
g_std = torch.std(g_channel)
b_mean = torch.mean(b_channel)
b_std = torch.std(b_channel)

print(f"   Red channel   - Mean: {r_mean:.4f}, Std: {r_std:.4f}")
print(f"   Green channel - Mean: {g_mean:.4f}, Std: {g_std:.4f}")
print(f"   Blue channel  - Mean: {b_mean:.4f}, Std: {b_std:.4f}")

# Alternative method: Permute to CHW format and calculate along dimensions
pytorch_tensor_chw = pytorch_tensor_float.permute(2, 0, 1)  # Change to CHW format
means = torch.mean(pytorch_tensor_chw, dim=[1, 2])
stds = torch.std(pytorch_tensor_chw, dim=[1, 2])

print(f"\n   Using permute method (CHW format):")
print(f"   Means (R, G, B): {means}")
print(f"   Stds (R, G, B):  {stds}")

# Bonus: Check for GPU and move tensor to GPU
print(f"\n6. BONUS - GPU Operations:")
if torch.cuda.is_available():
    print(f"   GPU is available: {torch.cuda.get_device_name(0)}")

    # Move tensor to GPU
    pytorch_tensor_gpu = pytorch_tensor_float.to('cuda')
    print(f"   Tensor moved to GPU")
    print(f"   Tensor device: {pytorch_tensor_gpu.device}")

    # Check GPU memory usage
    allocated_memory = torch.cuda.memory_allocated() / 1024**2  # Convert to MB
    reserved_memory = torch.cuda.memory_reserved() / 1024**2    # Convert to MB
    max_memory = torch.cuda.max_memory_allocated() / 1024**2    # Convert to MB

    print(f"\n   GPU Memory Usage:")
    print(f"   - Allocated: {allocated_memory:.2f} MB")
    print(f"   - Reserved:  {reserved_memory:.2f} MB")
    print(f"   - Max allocated: {max_memory:.2f} MB")

    # Calculate mean and std on GPU
    pytorch_tensor_chw_gpu = pytorch_tensor_gpu.permute(2, 0, 1)
    means_gpu = torch.mean(pytorch_tensor_chw_gpu, dim=[1, 2])
    stds_gpu = torch.std(pytorch_tensor_chw_gpu, dim=[1, 2])

    print(f"\n   Calculated on GPU:")
    print(f"   Means (R, G, B): {means_gpu}")
    print(f"   Stds (R, G, B):  {stds_gpu}")

    # Note: For image normalization, values are often divided by 255 first
    pytorch_tensor_normalized = pytorch_tensor_gpu / 255.0
    pytorch_tensor_chw_norm = pytorch_tensor_normalized.permute(2, 0, 1)
    means_norm = torch.mean(pytorch_tensor_chw_norm, dim=[1, 2])
    stds_norm = torch.std(pytorch_tensor_chw_norm, dim=[1, 2])

    print(f"\n   Normalized to [0,1] range:")
    print(f"   Means (R, G, B): {means_norm}")
    print(f"   Stds (R, G, B):  {stds_norm}")
else:
    print(f"   GPU is not available")
    print(f"   Tensor device: {pytorch_tensor_float.device}")
    print(f"   Running on CPU")

    # Note: For image normalization, values are often divided by 255 first
    pytorch_tensor_normalized = pytorch_tensor_float / 255.0
    pytorch_tensor_chw_norm = pytorch_tensor_normalized.permute(2, 0, 1)
    means_norm = torch.mean(pytorch_tensor_chw_norm, dim=[1, 2])
    stds_norm = torch.std(pytorch_tensor_chw_norm, dim=[1, 2])

    print(f"\n   Normalized to [0,1] range (CPU):")
    print(f"   Means (R, G, B): {means_norm}")
    print(f"   Stds (R, G, B):  {stds_norm}")

print("\n" + "=" * 60)
print("Task 1.1 completed!")
print("=" * 60)
