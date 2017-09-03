# InstaPicDownloader
Download the high quality version of a picture from Instagram. Tested on Ubuntu 16.04.3
Code is written in python3.

<img src="https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16110655_1661631840796839_4755495280277716992_n.jpg" alt="wolfiecindysmile" style="width:304px;height:228px;">

## how to run: 
1. ```git clone https://github.com/tai-euler/InstaPicDownloader.git```
2. ```cd InstaPicDownloader/```
3. ```python3 instaPicDownloader.py your_url```

## example: 
1. ```python3 instaPicDownloader.py 'https://www.instagram.com/p/BPXMlaKj88u/?taken-by=wolfiecindy'```

output:
2. ```Downloading from URL: https://www.instagram.com/p/BPXMlaKj88u/?taken-by=wolfiecindy```
3. ```High quality image downloaded from URL and saved as https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16110655_1661631840796839_4755495280277716992_n.jpg```



## troubleshooting: 
1. ```pip3 install bs4```
2. ```pip3 install requests```
