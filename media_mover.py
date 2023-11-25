import os

# Get list of HEIF and HEIC files in directory
directory = '/mnt/user/Documents/test1'
files = [f for f in os.listdir(directory)]

# Convert each file to JPEG
for filename in files:
    print(f'Moving {filename}...', end='\r')
    os.rename(f'/mnt/user/Documents/test1/{filename}', f'/mnt/user/Documents/test2/{filename}')
    print(f'Moving {filename}... Moving Complete!')

print('All files moved!')