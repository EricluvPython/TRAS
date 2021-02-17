# 2020zion User's Guide

## How to Install the Program
NOTE: if you already satisfy some of the requirements, you do not have to redo the steps.
Operating system: ```MacOS```
Python version: ```Python 3.8```
Python packages: ```jieba```, ```wordcloud```, ```requests```, ```SpeechRecognition```, ```wxpython```, ```pyaudio```

1. Download ```Python 3.8```

Download and install python 3.8 from this link from the python official website: 
    https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg
(it's probably ok as long as you have python 3.0+)

2. Install ```git```

Go to the website https://sourceforge.net/projects/git-osx-installer/ and install ```git```

3. Install ```pip```

Go to terminal, copy paste and enter the following command to download and install ```pip```
```
sudo easy_install pip
```

4. Install ```homebrew```

Go to terminal, copy paste and enter the following command
```
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```
on the first input, enter ```1```

5. Install ```portaudio```

Go to terminal, copy paste and enter the following command
```
brew install portaudio
```

6. Change the default package download python version for ```pip``` from python2 to python3

Go to terminal, copy paste and enter the following command ```sudo pip3 install virtualenv```

Then enter the command ```which python3``` and copy the returned path

Then enter the command ```sudo virtualenv -p [PATH] py3env``` where ```[PATH]``` is obtained from last step

Then enter the command ```source py3env/bin/activate```

7. Download python packages

Go to terminal, copy paste and enter the following command
```
sudo pip install jieba wordcloud requests SpeechRecognition wxpython pyaudio
```

8. Go to terminal, copy paste and enter the following command to clone this repository
```
git clone https://github.com/EricluvPython/2020zion.git
```

NOW, you have downloaded and installed this!

## How to Use the program?
the procedures are still finished in terminal
First, copy paste and enter the following commands
```
cd
cd 2020zion
```
After that, you can execute our python files using the command
```
python3 [FILENAME]
```
where [FILENAME] can be one of the following three: ```reset.py```, ```recognition.py```, or ```summary.py```.

```reset.py``` clears all history data in the folders ```record``` and ```results```.

```recognition.py``` starts recording your voice, recognize it using Baiducloud API (means needs internet connection), and show you the results on the screen. The results are temporarily saved to ```history.txt``` in ```record``` folder. The ```history.txt``` file is cleared everytime you run this program.

```summary.py``` does an Natural Language Processing (NLP) on the ```history.txt```, and provide you with a wordcloud image that you could use to remind yourself of the content of the class, and a ```YYMMDD_HHMMSS.txt``` file in folder ```results``` named based on the time you run the program. In this file, there will be the top 8 key words of your class, and the content of the speech heard.

A suggested sequence of using the three files are: before you start a meeting, run ```reset.py```. Then, run ```recognition.py```. When your meeting ends, stop ```recognition.py``` by pressing ```ctrl+c``` in terminal. If you want to obtain a summary of the class, run ```summary.py``` and save the image that shows on your screen or go to results folder and find the record for the class.

## But I Need Help!
If you have any problems regarding the program, you are welcomed to email me at 2025066613@QQ.com!
