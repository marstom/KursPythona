import zlib
from typing_extensions import Protocol
import codecs


class DataSource(Protocol):
    def write_data(self, data: bytes):
        ...

    def read_data(self) -> bytes:
        ...


class FileDataSource(DataSource):
    def __init__(self, filename: str):
        self._filename = filename

    def write_data(self, data: bytes):
        with open(self._filename, 'w') as f:
            f.write(data)

    def read_data(self) -> bytes:
        with open(self._filename, 'r') as f:
            content = f.read()
        return content


class DataSourceDecorator(DataSource):
    def __init__(self, s: DataSource):
        self._wrapee = s

    def write_data(self, data: bytes):
        self._wrapee.write_data(data)

    def read_data(self) -> bytes:
        return self._wrapee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def _enc(self, data):
        enc = codecs.encode(data, 'rot_13')
        return enc

    def _dec(self, data):
        # Create a binary codec for ROT13
        rot13_codec = codecs.getdecoder("rot_13")

        # Decode the binary data using ROT13
        decoded_data, _ = rot13_codec(data)

        return decoded_data

    def write_data(self, data: bytes):
        super().write_data(self._enc(data))

    def read_data(self) -> bytes:
        decoded = self._dec(super().read_data())
        return decoded


class ZipDecorator(DataSourceDecorator):
    def _zip(self, data):
        # Convert the input string to bytes
        input_bytes = data.encode('utf-8')

        # Compress the bytes using zlib
        compressed_bytes = zlib.compress(input_bytes, level=zlib.Z_BEST_COMPRESSION)

        # Encode the compressed bytes as base64 for safe storage
        compressed_base64 = compressed_bytes.hex()

        return compressed_base64

    def _unzip(self, data):
        # Decode the compressed base64 string to bytes
        compressed_bytes = bytes.fromhex(data)

        # Decompress the bytes using zlib
        decompressed_bytes = zlib.decompress(compressed_bytes)

        # Convert the decompressed bytes back to a string
        decompressed_string = decompressed_bytes.decode('utf-8')

        return decompressed_string

    def write_data(self, data: bytes):
        super().write_data(self._zip(data))

    def read_data(self) -> bytes:
        decoded = self._unzip(super().read_data())
        return decoded
