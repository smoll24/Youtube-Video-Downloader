---
# Youtube Video Downloader

This Python program allows you to easily download YouTube videos, either in video or audio format, with only a YouTube link. It gives you the option to enter a path, or, left blank, it will save the video directly in the same directory as the Python program. You can choose if you want video and audio or only audio, and it will give you the list of formats available and you can choose which format you want. After you download it, it opens the file automatically so you are sure it downloaded correctly.

### Installation
To use this program, you will need to install the following libraries:

* pytube
* moviepy
* tkinter
* os

You can install these libraries using pip with the following command:
```
pip install pytube moviepy tkinter os
```
### Usage
To use this program, simply run the yt_downloader.py file. A simple interface will be displayed where you can enter the YouTube link and choose the format of the downloaded file. You can choose to download both video and audio, or only audio. You can also choose to save the file in a specific location or in the same directory as the Python program.

After you click the "Download" button, the program will start downloading the file. Once the download is complete, the file will automatically open so you can confirm that it downloaded correctly.

### Credits
This program uses the following libraries:

* pytube - Used to download the video from YouTube
* moviepy - Used to play the file after it has been downloaded
* tkinter - Used to provide a simple interface for the user.
