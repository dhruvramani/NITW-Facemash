from urllib.request import urlretrieve

def main():
    for i in range(100000, 1000000):
        try :
            print("=> Dowloading Roll Number {} :=> ".format(i), end = "")
            urlretrieve("https://wsdc.nitw.ac.in/student/assets/upload/thumbs/{}.jpg".format(i), "{}.jpg".format(i))
            print("Done")
        except :
            print("=> Roll Number {} doesn't exist.".format(i))

if __name__ == '__main__':
    main()