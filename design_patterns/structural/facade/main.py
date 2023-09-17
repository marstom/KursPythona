from video_converter import VideoConverter

if __name__ == '__main__':
    vid = VideoConverter()
    converted = vid.convert('my.raw', 'MP4')
    print(converted)
