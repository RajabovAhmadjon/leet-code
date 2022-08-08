#!/bin/python3 

from fileinput import filename
import shutil   # For copy file
import os       # For getting file size and chacking if file exists
import sys      # For CLI arguments

# purge_log.py <log_file_name>  <max_size_of_log> <extra_files_number>
# purge_log.py mylog.txt 10 5

if(len(sys.argv) < 4):
    print("Missing arguments! Usage is script.py log.txt 10 5")
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
log_number = int(sys.argv[3])

if(os.path.isfile(file_name) == True):          # Check if MAIN logfile exists
    logfile_size = os.stat(file_name).st_size   # Get Filesize in BYTES
    logfile_size = logfile_size / 1024          # Convert from BYTES to KILOBYTES

    if(logfile_size >= limit_size):
        if(log_number > 0):
            for current_file_number in range(log_number, 1, -1):
                src = file_name + "_" + str(current_file_number - 1)        # log.txt_4
                dst = file_name + "_" + str(current_file_number)            # log.txt_5
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)                               # log.txt_4 to log.txt_5
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + filename + " to " + file_name + "_1")
        base_file = open(file_name, 'w')        # To clear initial log file
        base_file.close()
else:
    print("Such file {} doesn't exsists!".format(file_name))            
