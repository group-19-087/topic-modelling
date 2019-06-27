import glob
import os
import subprocess
import shutil
import sys


def lda(no_of_topics):
    print (subprocess.call(['sudo','java','-Xmx2048m','-cp','bin:lib/args4j-2.0.6.jar','jgibblda.LDA','-est','-beta', str(0.05),'-ntopics', str(no_of_topics),'-twords',str(5),'-dir','.','-dfile','data.dat']))
    folder_name = 'topic-model'
    os.mkdir(folder_name)
    files = glob.glob('model-*')
    for j in files:
        shutil.move(j, folder_name)
    shutil.move('wordmap.txt',folder_name)
    print("Completed model with topics: "+str(no_of_topics))

if __name__== "__main__":
    lda(sys.argv[1])