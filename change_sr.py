import subprocess
import glob
from params import sample_rate
import sys
import tqdm
import shutil


def change_sr(filename, sr):
    subprocess.run(["ffmpeg", "-y", "-i", filename, "-ar", f"{sr}", f"{filename.replace('.wav', '1.wav')}"])
    shutil.move(filename.replace('.wav', '1.wav'), filename)


if __name__ == '__main__':
    for filename in tqdm.tqdm(glob.glob(f"{sys.argv[1]}/*.wav")):
        print(filename)
        change_sr(filename, sr=sample_rate)
