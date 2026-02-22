#!/usr/bin/python3
if __name__ == "__main__":
    import marshal
    import os

    pyc_path = os.path.join(os.path.dirname(__file__), "__pycache__", "hidden_4.cpython-38.pyc")

    with open(pyc_path, "rb") as f:
        f.read(16)
        code = marshal.load(f)

    names = [n for n in code.co_names if not n.startswith("__")]

    for n in sorted(names):
        print(n)
