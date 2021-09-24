import sys

from cffi import FFI


ffibuilder = FFI()

ffibuilder.set_source(
    "_golib",
    """ //passed to the real C compiler
        #include "golib.h"
    """,
    extra_objects=["build/golib.so"],
    include_dirs=["./build"]
)

is_64b = sys.maxsize > 2**32
if is_64b: ffibuilder.cdef("typedef long GoInt;\n")
else:      ffibuilder.cdef("typedef int GoInt;\n")

ffibuilder.cdef(
    """
    typedef struct {
        void* data;
        GoInt len;
        GoInt cap;
    } GoSlice;

    typedef struct {
        const char *p;
        GoInt n;
    } GoString;

    extern void Hello();
    extern int Greet(GoString name);
    extern GoInt Factorial(GoInt n);
    """
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
