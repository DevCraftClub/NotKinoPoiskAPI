#!/usr/bin/env python3
import NotKinoPoiskAPI

import pdoc

if __name__ == "__main__":
    doc = pdoc.doc.Module(NotKinoPoiskAPI)

    out = pdoc.render.html_module(module=doc, all_modules={"NotKinoPoiskAPI": doc})

    with open("index.html", "w") as f:
        f.write(out)
