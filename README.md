# Automatically scrape images from reddit and generate short 10 second videos for YouTube
**Demo**: https://www.youtube.com/@dailymemeshq 

This project takes two images from a subreddit of your liking and generates a short 10 second video ready to be uploaded to YouTube. You can customize the background, the audio and you can choose from where and what images to use.
In the example channel above i am using memes from the [dankmemes](https://www.reddit.com/r/dankmemes/) subreddit.

## Requirements

Except from all the Python modules you will aslo need [ffmpeg](https://ffmpeg.org/download.html) to add audio to the video (make sure ffmpeg is added to path) and you will also need [wand](https://docs.wand-py.org/en/0.6.7/guide/install.html) wich is required to build together the images. 

## Usage

Change line 28 in main.py to choose what subreddit to use.

Run the following command but change `{index}` to the index of the image you want i.e if you want the first two images use index 0 and 1.
```
python main.py {index} {index}
```


 
