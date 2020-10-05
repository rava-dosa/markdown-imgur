import re
import os
import sys
from imgurpython import ImgurClient

r=re.compile('\!\[.*\]\(.*\)')
r1=re.compile('\((.*)\)')
r2=re.compile('(^http://|^https://)')
client = None

def init_client():
    client_id = os.getenv("imgur_id")
    client_secret = os.getenv("imgur_secret")
    global client
    client = ImgurClient(client_id, client_secret)

def upload_image(image_path):
    global client
    if(client is None):
        init_client()
    image = client.upload_from_path(image_path)
    print(image)
    return image["link"]

def write_in_file(filepath,all):
    f=open(filepath,"w")
    for x in all:
        f.write(x)
    f.close()

def checklocal(path):
    temp=r2.findall(path)
    if(temp is None):
        return True
    else:
        return False

def update_file(filepath):
    f=open(filepath)
    all=f.readlines()
    for x in range(0,len(all)):
        temp=r.findall(all[x])
        for y in temp:
            temp1=r1.search(y)
            temp_path=temp1.group(1)
            if(checklocal(temp_path)):
                url=upload_image(temp_path)
                print("uploaded {} to {}".format(temp_path,url))
                all[x]=all[x].replace(temp_path,url)
            else:
                continue
    f.close()
    write_in_file(filepath,all)

if __name__ == "__main__":
    init_client()
    for x in range(1,len(sys.argv)):
        update_file(sys.argv[x])
        
