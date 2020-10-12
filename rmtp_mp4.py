from subprocess import Popen
import os


# use Popen from subprocess to execute a child program in a new process
# if args is a string, the string is interpreted as the name or path of the program to execute


ads_extra = [
    "rtmp://streaming.noroff.no:1935/vod/ADS101_TweetProcess1.mp4",
    "rtmp://streaming.noroff.no:1935/vod/ADS101_TagToGML.mp4"
]

# list for the links to download
rmpt_list = [ # list of "links" separated by , ]


def download_videos(path, video_list):
    """Download rmtp videos to designated path.

    Args:
        path (string): path to where to download
        video_list (list): list of the links
    """

    # VLC has the following app path on mac:
    # Popen(f"/Applications/VLC.app/Contents/MacOS/VLC")

    # change directory of where to download
    os.chdir(path)

    # loop through the list of links and download them, saving with the name of the file
    # use file/mp4 as per the documentation here https://www.videolan.org/streaming-features.html since ts doesn't work with quicktime
    for fname in rmpt_list:
        split = fname.split("/")[4]
        final_name = split.replace(".mp4", "",)
        print("Working on ", fname)
        Popen(["/Applications/VLC.app/Contents/MacOS/VLC", "-I", "rc", f"{fname}", "--sout", f"file/mp4:{final_name}.mp4"])

if __name__ == "__main__":
    download_videos("/Volumes/T7 Touch/NOROFF/Downloaded from Moodle/Year2/Algorithms and Data Structures/Videos/",rmpt_list)
