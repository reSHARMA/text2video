import sys  
import os
import sel
import utils
import emotion
import nlp
import image
import music
import video

def main(filepath):  
        emotions = []
	if not os.path.isfile(filepath):
            print("File path does not exist. Exiting...".format(filepath))
	    sys.exit()
        # make it txt
	with open(filepath) as fp:
            ln_count = 0;
            blob = ""
            for line in fp:
                ln_count += 1
                if ln_count // 10 == 0:
                    emotions.append(emotion.get(blob))
                else:
                    blob += line
		input = nlp.preprocess(line)
		input = utils.unique(input)
                print(input)
                sel.getImage(' '.join(input))
                image.join(line, ln_count)
        mood = emotion.process(emotions)
        song = music.getSong(mood)
        video.generate(song, "Awesomevideo", "mp4")
