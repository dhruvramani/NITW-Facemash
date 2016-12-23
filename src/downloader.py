import requests

def main():
    for i in range(100000, 1000000):
        try :
            r = requests.get("https://wsdc.nitw.ac.in/student/assets/upload/thumbs/{}.jpg".format(i))
            if 'html' in r.headers['content-type'] :
                raise Exception('Roll Number Doesn\'t exist')
            print("=> Dowloading Roll Number {} :=> ".format(i), end = "")
            with open("../images/{}.jpg".format(i), "wb") as img :
                img.write(r.content)
            print("Done")
        except :
            print("=> Roll Number {} doesn't exist.".format(i))

if __name__ == '__main__':
    main()