import sys
import os
import subprocess
def generate(song, name, ext):
    count = 1
    cmd = ['convert']
    while os.path.isfile("/tmp/t2vimage-"+ str(count) + ".png"):
            cmd.append("-delay")
            cmd.append("200")
            cmd.append("/tmp/t2vimage-"+ str(count) + ".png")
            count += 1
    cmd.append("/tmp/tv2.mp4")
    subprocess.call(cmd)
    cmd = ["ffmpeg",  "-i", "/tmp/t2v.mp4", "-i", song, "-codec", "copy", "-shortest", "/tmp/" + str(name) + ".mp4"]
    subprocess.call(cmd)
