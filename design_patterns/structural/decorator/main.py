from data_source import FileDataSource, EncryptionDecorator, ZipDecorator

if __name__ == '__main__':
    """ Multiple zipped and encrypted rot13 file! """
    ff = EncryptionDecorator(ZipDecorator(
        ZipDecorator(
            EncryptionDecorator(
                FileDataSource('./file.txt')
            )
        )
    )
    )
    ff.write_data("Mam na imie tomek.")

    print(ff.read_data())
