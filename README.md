---
# Youtube Video Downloader

This Python software provides a simple way to download YouTube videos in either video or audio format by pasting the YouTube link.
It allows the user to choose where to save the file, either in a specified path or by default in the same directory as the Python program. 
The user has the freedom to choose between downloading either the video with its audio or only the audio file. The software also presents a list of available formats for the selected video and audio, allowing the user to choose their preferred option. 
Upon completion, the software automatically opens the downloaded file to ensure the download was successful.

![image](https://user-images.githubusercontent.com/115204665/227081312-edcaaaf5-94c7-4cf5-888e-719f9ea56f5b.png)

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
To use this program, run the yt_downloader.py file. A simple interface will be displayed where you can enter the YouTube link and choose the format of the downloaded file. You can choose to download both video and audio, or only audio. You can also choose to save the file in a specific location or in the same directory as the Python program.

After you click the "Download" button, the program will start downloading the file. Once the download is complete, the file will automatically open so you can confirm that it downloaded correctly.

### Credits
This program uses the following libraries:

* pytube - Used to download the video from YouTube
* moviepy - Used to play the file after it has been downloaded
* tkinter - Used to provide a simple interface for the user
