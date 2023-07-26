import contextlib

@contextlib.contextmanager
def funkcja(handler):
    handler.append('start....')
    yield handler
    print(".....clean up")
    handler.append('....end')

handler = []
with funkcja(handler) as ff:
    print(ff)
    handler.append('moja')
    print("Hello")

print(handler)
