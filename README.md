# Youtube Video Downloader

### About
This Python software provides a simple way to download YouTube videos in either video or audio format by pasting the YouTube link.
It allows the user to choose where to save the file, either in a specified path or by default in the same directory as the Python program. 
The user can choose between downloading either the video with its audio or only the audio file. 

The user is also presented with a list of available formats for the selected video and audio, allowing the them to choose their preferred option. 
Upon completion, the downloaded file is automatically opened if possible to ensure the download was successful.

![ezgif-4-9ec23466fb](https://user-images.githubusercontent.com/115204665/227121394-70fe0e35-3552-4eba-bed5-57d94c2a6273.gif)


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

### Important Notice
PyTube does not fully function at the moment, and if run directly the program with give you an **ERROR** stating that 'NoneType' object has no attribute 'span'.

This requires a quick fix (found thanks to @dark9ive [in this thread](https://github.com/pytube/pytube/issues/1498#issuecomment-1472963944)) that can be patched by modifying **{home}/.local/lib/python3.7/site-packages/pytube/cipher.py** -- **Line 411** -- from
```
transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)
```
to
```
transform_plan_raw = js
```

### Usage
To use this program, run the yt_downloader.py file. A simple interface will be displayed where you can enter the YouTube link and choose the format of the downloaded file. You can choose to download both video and audio, or only audio. You can also choose to save the file in a specific location or in the same directory as the Python program.

After you click the "Download" button, the program will start downloading the file. Once the download is complete, the file will automatically open so you can confirm that it downloaded correctly.

### Credits 
This program uses the following libraries:

* pytube - Used to download the video from YouTube
* moviepy - Used to play the file after it has been downloaded
* tkinter - Used to provide a simple interface for the user
