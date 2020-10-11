from subprocess import Popen
import os


# use Popen from subprocess to execute a child program in a new process
# if args is a string, the string is interpreted as the name or path of the program to execute

# list for the links to download
rmpt_list = ["rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-08-27.mp4",
            "rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-08-28.mp4",
            "rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-08-29.mp4",
            "rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-09-03.mp4",
            "rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-09-04.mp4",
            'rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-09-05.mp4',
            "rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-09-10.mp4",
            "rtmp://streaming.noroff.no:1935/vod/UC2OOP101_2018-09-11.mp4"
]


def download_videos(path, video_list):
    """Download rmtp videos to designated path.

    Args:
        path ([string]): path to where to download
        video_list ([type]): list of the links
    """

    # VLC has the following app path on mac:
    # Popen(f"/Applications/VLC.app/Contents/MacOS/VLC")

    # change directory of where to download
    os.chdir(path)

    # loop through the list of links and download them, saving with the name of the file
    for fname in rmpt_list:
        split = fname.split("/")
        final_name = split[4]
        Popen(["/Applications/VLC.app/Contents/MacOS/VLC", "-v", f"{fname}",
        "--sout", f"file/ts:{final_name}"])

if __name__ == "__main__":
    download_videos("/Volumes/T7 Touch/NOROFF/Downloaded from Moodle/Year2/Object Oriented Programming/Videos/",
    rmpt_list)
