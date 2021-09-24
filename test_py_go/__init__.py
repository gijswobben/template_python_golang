from _golib import ffi, lib


def GoString(data: bytes):
    x = ffi.new("char[]", data)
    msg = ffi.new("GoString*", {"p": x, "n": len(data)})
    return msg[0]


def hello():
    return lib.Hello()


def greet(data: bytes) -> int:
    return lib.Greet(GoString(data))


def factorial(n: int) -> int:
    return lib.Factorial(n)


__all__ = [
    "hello",
    "greet",
    "factorial",
]
