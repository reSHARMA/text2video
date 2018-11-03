import subprocess
import os
def join(text, line_no):
    # image.png + text = image-line_no.png
    out = subprocess.Popen(['identify', '-format', '%w', '/tmp/image.png'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    width = int(stdout)
    subprocess.call(['convert', '/tmp/image.png', '-resize', '480x480!', '/tmp/image-t.png' ])
#   TODO font size
    output = "/tmp/t2vimage-" + str(line_no) + ".png"
    cmd = "convert -background '#0008' -fill white -gravity center -size " + str(int(width) * 30) + " caption:\"" + str(text) + "\" /tmp/image-t.png +swap -gravity center -composite " + output 
    os.system(cmd)
