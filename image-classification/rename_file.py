import os
import shutil

path = ["training", "testing"]
dist = "mnist"
i = 0
for dirc in path:
	for subdir in os.listdir(os.path.join(dirc)):
		for fls in os.listdir(os.path.join(dirc, subdir)):
			shutil.copyfile(os.path.join(dirc, subdir, fls),
			 				os.path.join(dist, subdir, str(i) + ".png"))
			i += 1
