import os
import subprocess
import sys

if not os.path.exists('output'):
    os.mkdir('output')

print(subprocess.call(['sh','topictiling.sh','-ri','5','-tmd','topic-model','-tmn','model-final','-fp',sys.argv[1]+'.txt','-fd','files_to_segment','-out','output/output.xml', '-dn']))