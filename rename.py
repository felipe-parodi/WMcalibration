'''
logic: 
- set of folders, each containing videos
- go in each folder and rename using folder name
- iterate per folder
'''

#=====TODO
# insert check for .mp4 extension


import os, time, argparse 

#============== ARGUMENTS =======================
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to frames")
ap.add_argument("-n", "--indx", required=True, help="index to use of file name")
args = vars(ap.parse_args())
#================================================
tic = time.perf_counter()

path = str(args["path"])
nums = int(args["indx"])
agg = path[-nums:] # change to -5 if working with >9 cameras
# if first element isn't c, then remove it
# if agg[0] != 'c':
#    agg = agg[1:]

for count, filename in enumerate(os.listdir(path)): 
   dst =agg + '_' + str(count) + ".mp4"
   src = path + '/' + filename
   dst = path + '/' + dst
   os.rename(src, dst)

# how to add a loop to iterate over folders in broader directory?
# for root, dirs, files in enumerate(os.listdir(path)):
#    for name in files:
#       if(name.endswith('.mp4')):
#          dst =agg + '_' + str(count) + ".mp4"
#          src = path + '/' + filename
#          dst = path + '/' + dst
#          os.rename(src, dst)

toc = time.perf_counter()
print(f'Files renamed in {toc - tic:0.4f} seconds!')