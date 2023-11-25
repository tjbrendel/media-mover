import os

# Establish initial variables
movie_directory = '/mnt/user/Media/Movies'
tv_directory = '/mnt/user/Media/TV Shows'
movie_files = [f for f in os.walk(movie_directory)]
tv_files = [f for f in os.walk(tv_directory)]

# Convert each file to JPEG
for filename in movie_files:
    print(f'{filename}')
    #os.rename(f'/mnt/user/Documents/test1/{filename}', f'/mnt/user/Documents/test2/{filename}')
    #print(f'Moving {filename}... Moving Complete!')

print('')

for filename in tv_files:
    print(f'{filename}')