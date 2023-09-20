class It:
    def __init__(self):
        self.ll = [11, 22, 33]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.ll) == 0:
            raise StopIteration()
        return self.ll.pop()


if __name__ == '__main__':
    it = It()
    for a in it:
        print(a)
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
