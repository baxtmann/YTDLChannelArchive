#!/usr/bin/env python3

import os

# the custom command to be executed with every URL, the URL is substituted inside the {}
command = r'.\youtube-dl.exe -f best -ciw -o "%(uploader)s/%(title)s.%(ext)s" -v {}'

# channels list file
channels_file = 'channels.txt' # file in the same folder

# Program entry point
if __name__ == "__main__":

    # open the file
    try:
        f = open(channels_file)    
    except: 
        print("There was a problem opening the file {}, please check the file and try again".format(channels_file))
        exit()
    
    # read the URLs
    try:
        channels_list = f.readlines()
        print("Read {} files".format(len(channels_list)))
    except: 
        print("There was a problem reading the file {}, please check the file and try again".format(channels_file))

    # Execute the custom command for every URL
    for i, c in enumerate(channels_list):
        print("Downloading {} of {}".format(i+1, len(channels_list)))
        os.system(command.format(c))
    

