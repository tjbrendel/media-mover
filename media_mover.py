import os
import re

# Establish initial variables
movie_directory = r'S:\test_dir\Movies' #'/mnt/user/Media/Movies'
tv_directory = r'S:\test_dir\TV Shows' #'/mnt/user/Media/TV Shows'
handbrake_directory = r'S:\test_dir\encoded'

movie_files = [f.name for f in os.scandir(movie_directory)]
tv_files = [f.name for f in os.scandir(tv_directory)]
encoded_files = [f for f in os.listdir(handbrake_directory) if os.path.isfile(os.path.join(handbrake_directory, f))]

if len(encoded_files) > 0:
    #loop through all encoded files in the handbrake directory
    for file in encoded_files:

        #check to see if current file is a movie or tv show - all tv shows will have a -sXXeXX format
        if re.search(r'-s\d{2}e\d{2}', file):
            #TV File
            new_tv_dir = f"{tv_directory}\{file.split('-')[0]}"
            new_tv_season = file.replace('.mkv', '').split('-')[1].split('e')[0].split('s')[1]
            new_tv_dir_season = f"{tv_directory}\{file.split('-')[0]}\Season {new_tv_season}"
            src_tv = f"{handbrake_directory}\{file}"
            
            #check to see if current tv show exists in tv shows directory
            if file.split('-')[0] in tv_files:
                #TV Show already exists in directory
                tv_seasons = [f.name for f in os.scandir(f"{tv_directory}\{file.split('-')[0]}")]
                
                #check to see if current season exists for this show
                if f"Season {new_tv_season}" in tv_seasons:
                    os.replace(src_tv, f"{new_tv_dir_season}\{file}")
                else:
                    os.mkdir(new_tv_dir_season)
                    os.replace(src_tv, f"{new_tv_dir_season}\{file}")

            else:
                #TV Show does not exist in directory
                os.mkdir(new_tv_dir)
                os.mkdir(new_tv_dir_season)
                os.replace(src_tv, f"{new_tv_dir_season}\{file}")
        else:
            #Movie file
            new_movie_dir = f"{movie_directory}\{file.split('.')[0]}"
            src_movie_file = f"{handbrake_directory}\{file}"

            if file.replace('.mkv', '') in movie_files:
                os.replace(src_movie_file, f"{new_movie_dir}\{file}")
            else:
                os.mkdir(new_movie_dir)
                os.replace(src_movie_file, f"{new_movie_dir}\{file}")