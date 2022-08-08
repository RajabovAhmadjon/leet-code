import os 
import time

DAYS = 3        # Maximal age of file to stay, older will be deleted
FOLDERS = [
    "D:\Trash",
    "E:\Bin"
]

TOTAL_DELETED_SIZE = 0      # Total deleted size of all files in BYTES
TOTAL_DELETED_FILE = 0      # Total deleted files
TOTAL_DELETED_DIRS = 0      # Total deleted empty folders

now_time = time.time()      # Get current time in SECONDS
age_time = now_time - 60 * 60 * 24 * DAYS   # Minus DAYS in SECONDS sec*min*hours*days

#=============================== FUCNTIONS ====================================
def delete_old_files(folder):
    """Delete files older than X days"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE

    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)    # Get Full Path to file
            file_time = os.path.getmtime(file_name) # Get Modification time of file
            if file_time < age_time:
                file_size = os.path.getsize(file_name)
                TOTAL_DELETED_SIZE += file_size     # Count SUM of all deleted free space
                TOTAL_DELETED_FILE += 1             # Count number of deleted files
                os.remove(file_name)                # Delete file
                print("Deleting file: " + str(file_name))

def delete_empty_dir(folder):
    """Delete empty directories"""
    global TOTAL_DELETED_DIRS
    empty_folders_in_run = 0

    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1     # Count empty directories
            empty_folders_in_run += 1   # Count run of function to delete parent directory like recursive
            os.rmdir(path)              # Delete directory 
            print("Deleting empty directory: " + str(path))
    
    if empty_folders_in_run > 0:
        delete_empty_dir(folder)

#================================= MAIN =======================================
start_time = time.asctime() # Get formatted time

for folder in FOLDERS:
    delete_old_files(folder)    # Delete old files function
    delete_empty_dir(folder)    # Delete empty folders function

finish_time = time.asctime()

print("------------------------------------------------------------------------------------")
print("START TIME: "                    + str(start_time))
print("Total Deleted Size: "            + str(int(TOTAL_DELETED_SIZE / 1024 / 1024)) + " MB")
print("Total Deleted Files: "           + str(TOTAL_DELETED_FILE))
print("Total Deleted Empty Folders: "   + str(TOTAL_DELETED_DIRS))
print("FINISH TIME: "                   + str(finish_time))
print("-------------------------------------------------------------------------------------")
