from unittest import mock

# some 3rd party libs
OOGCompresionCodec = mock.Mock()
MPG4CompresionCodec = mock.Mock()
CodecFactory = mock.Mock()
BitrateReader = mock.Mock()
AudioMixer = mock.Mock()
File = mock.Mock()


class VideoFile(File):
    ...


# Facade
class VideoConverter:
    def convert(self, filename, format) -> File:
        file = VideoFile(filename)
        source_codec = CodecFactory().extract(file)
        if(format == "MP4"):
            dest_codec = MPG4CompresionCodec(file)
        else:
            dest_codec = OOGCompresionCodec(file)

        buffer = BitrateReader.read(file, source_codec)
        result = BitrateReader.convert(buffer, dest_codec)
        result = AudioMixer().fix(result)
        return File(result)
