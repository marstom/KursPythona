from youtube import ThirdPartyYouTubeLib, CachedYouTubeClass, ThirdPartyYouTubeClass


def test_youtube_orig():
    yt_service = ThirdPartyYouTubeClass()

    print(yt_service.list_videos())
    print(yt_service.list_videos())
    print(yt_service.list_videos())
    yt_service.download_video('my')
    yt_service.download_video('my')
    yt_service.download_video('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')

def test_youtube_proxy():
    orig_yt_service = ThirdPartyYouTubeClass()
    yt_service = CachedYouTubeClass(orig_yt_service)

    print(yt_service.list_videos())
    print(yt_service.list_videos())
    print(yt_service.list_videos())
    yt_service.download_video('my')
    yt_service.download_video('my')
    yt_service.download_video('my')
    yt_service.download_video('my')
    yt_service.download_video('my')
    yt_service.download_video('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')
    yt_service.get_video_info('my')
