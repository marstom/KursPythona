from hashlib import md5

from typing_extensions import Protocol


class ThirdPartyYouTubeLib(Protocol):
    def list_videos(self) -> dict[str, str]:
        ...

    def get_video_info(self, id: str) -> dict:
        ...

    def download_video(self, id: str) -> bytes:
        ...


class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, s: ThirdPartyYouTubeLib):
        self._service = s
        self._list_cache = ""
        self._video_cache = ""
        self._downloads = dict()
        self.need_reset = False

    def list_videos(self) -> dict[str, str]:
        if not self._list_cache or self.need_reset:
            print("Caching list result....")
            self._list_cache = self._service.list_videos()
        return self._list_cache

    def get_video_info(self, id: str) -> dict:
        if not self._video_cache or self.need_reset:
            print("Caching video info result....")
            self._video_cache = self._service.get_video_info(id)
        return self._video_cache

    def download_video(self, id: str) -> bytes:
        raw_data = self._service.download_video(id)
        hashed = md5(raw_data).hexdigest()
        if not self.__download_exitst(raw_data) or self.need_reset:
            print("Caching download data....")
            self._downloads[hashed] = raw_data
        return self._downloads[hashed]

    def __download_exitst(self, data):
        hash = md5(data).hexdigest()
        # self._downloads[hash] = data
        return hash in self._downloads.keys()

class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def list_videos(self) -> dict[str, str]:
        # do request
        return {'my': 'my.mp4', 'cats': 'cats.mp4', 'python_tutorial': 'tut.mp4'}

    def get_video_info(self, id: str) -> dict:
        print(f"video info for {id}")
        return {"my", "my.mp4"}

    def download_video(self, id: str) -> bytes:
        print(f"Download vid {id}")
        return b"video stream bytes......"
