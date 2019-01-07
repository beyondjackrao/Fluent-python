def aa():
    print ('aa')


def bb():
    return aa()
if __name__ == '__main__':
    print(bb())