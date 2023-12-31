import os
import re
import json
import time
from modules import logger

#read in json config file
with open("json_config/config.json") as config_file:
    config_dirs = json.load(config_file)

# Establish initial variables
movie_directory = config_dirs['movie_dir']
tv_directory = config_dirs['tv_dir']
handbrake_directory = config_dirs['handbrake_dir']
encoded_files = [f for f in os.listdir(handbrake_directory) if os.path.isfile(os.path.join(handbrake_directory, f))]

if len(encoded_files) > 0:
    #loop through all encoded files in the handbrake directory
    for file in encoded_files:
        file_match = file.lower().replace(' ', '').replace('.mkv', '')
        #check to see if current file is a movie or tv show - all tv shows will have a -sXXeXX format
        if re.search(r'-s\d{2}e\d{2}', file_match):
            #TV File
            tv_files = [f.name for f in os.scandir(tv_directory)]
            tv_files_match = [f.lower().replace(' ', '') for f in tv_files]
            new_tv_dir = f"{tv_directory}/{file.split('-')[0]}"
            new_tv_season = file.replace('.mkv', '').split('-')[1].split('e')[0].split('s')[1]
            new_tv_dir_season = f"{tv_directory}/{file.split('-')[0]}/Season {new_tv_season}"
            src_tv = f"{handbrake_directory}/{file}"
            
            #check to see if current tv show exists in tv shows directory
            if file_match.split('-')[0] in tv_files_match:
                #TV Show already exists in directory
                tv_seasons = [f.name for f in os.scandir(f"{tv_directory}/{file.split('-')[0]}")]
                
                #check to see if current season exists for this show
                if f"Season {new_tv_season}" in tv_seasons:
                    os.replace(src_tv, f"{new_tv_dir_season}/{file}")
                else:
                    os.mkdir(new_tv_dir_season)
                    os.replace(src_tv, f"{new_tv_dir_season}/{file}")

            else:
                #TV Show does not exist in directory
                os.mkdir(new_tv_dir)
                os.mkdir(new_tv_dir_season)
                os.replace(src_tv, f"{new_tv_dir_season}/{file}")
        else:
            #Movie file
            movie_files = [f.name for f in os.scandir(movie_directory)]
            movie_files_match = [f.lower().replace(' ', '') for f in movie_files]
            new_movie_dir = f"{movie_directory}/{file.split('.')[0]}"
            src_movie_file = f"{handbrake_directory}/{file}"

            if file_match in movie_files_match:
                os.replace(src_movie_file, f"{new_movie_dir}/{file}")
            else:
                os.mkdir(new_movie_dir)
                os.replace(src_movie_file, f"{new_movie_dir}/{file}")
