import sys
import subprocess
import pkg_resources

required  = {'pytube', 'gdown', 'spleeter','sffmpeg'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

import spleeter
import IPython.display as ipd
from IPython.display import Audio, display
from IPython.display import HTML

import tqdm
from pytube import YouTube
import os
from pathlib import Path


def youtube2mp3 (url,outdir,fname):
    # url input from user
    yt = YouTube(url)

    ##@ Extract audio with 160kbps quality from video
    video = yt.streams.filter(only_audio=True,abr='160kbps').last()

    ##@ Downloadthe file
    out_file = video.download(output_path=outdir,filename=fname)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    ##@ Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
        fname="/content/audio/"+"/"+fname+'/'+fname+'.mp3'
        !spleeter separate $fname -p spleeter:5stems -c mp3 -o /content/audio/
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')
    

def audiodl(id):
  id=str.split(id)
  print(id)
  for i in range(0,len(id)):
    url='www.youtube.com/watch?v='+id[i]
    youtube2mp3(url,'/content/audio/'+str(id[i])+"",id[i])

audiodl(input())
