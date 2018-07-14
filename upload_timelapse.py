import os
path="/home/pi/motion/"


def upload_files():
	if not os.path.exists(path):
		return
	for files in os.listdir("."):
		if files.endswith("timelapse.mpg"):
			cmd = "/home/pi/dropbox_uploader.sh upload " + path + files
			os.system(cmd)


if __name__ == "_main_":
	upload_files()
