# Python 3 code to demonstrate
# SHA hash algorithms.

import hashlib

hash = "b8e46064c5cb98321ab378f546d2641881b43563"

words = ["walle", "WALLE", "Wall-e", "wall-e", "WALL-E", "logitech", "walle is having fun", "wally with hands up", "nopasswordrequired",
         "wallewithlasmanosarriba", "walleWithLasManosArriba"]
for str2 in words:
    for str in str2.split():
        result = hashlib.sha1(str.encode())
        hashres = result.hexdigest()
        if hashres == hash:
            print("FOUND!!!!!")
        #print(hashres)