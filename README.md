# Use Go methods in Python

1. Export methods in the Go file
2. Wrap all exposed methods in `builder.py` to make them availble after building
3. Wrap all exposed methods in `test_py_go/__init__.py` to make them available in Python
4. Run `./install` to build the Go module and install the library as Python module
5. Run example scripts in the `examples/` folder
