import fnmatch
import os
import glob
import zipfile
import shutil
import argparse


def find_mp4(root_directory, pattern='*.mp4'):
    matched = []

    for root, dirs, files in os.walk(root_directory):
        for filename in fnmatch.filter(files, pattern):
            matched.append(os.path.join(root, filename))

    return matched


def create_videos(base_dir = '.'):
    os.chdir(base_dir)

    for file in glob.glob("*.maff"):
        new_dir = file.replace(' ', '', 1).rsplit('.', 1)[0]
        print "Done {}".format(file)

        zip_file = zipfile.ZipFile(file, 'r')
        zip_file.extractall(new_dir)

        video_dir = os.path.join(new_dir, 'videos')
        try:
            os.stat(video_dir)
        except:
            os.mkdir(video_dir)

        for mp4 in find_mp4(new_dir):
            os.rename(mp4, os.path.join(video_dir, mp4.split('/')[-1]))

        for subdir in os.listdir(new_dir):
            if subdir != 'videos':
                shutil.rmtree(os.path.join(new_dir, subdir))


def main():
    parser = argparse.ArgumentParser(description='Convert and extract all mp4 '
                                                 'files from maff archives.')
    parser.add_argument('--base-dir', default='.',
                        help='Root directory to start the search')

    args = parser.parse_args()
    create_videos(base_dir=args.base_dir)


if __name__ == "__main__":
    main()
