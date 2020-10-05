Typora provide a way to add local image to your markdown. I have written a simple script to upload the image to imgur.

## How to use ?

1. python imgur.py filepath1 filepath2

## How to setup ?

1. Create a virtual environment
2. pip install -r requirements.txt
3. create a imgur app [here](https://api.imgur.com/oauth2/addclient)
4. After you do that you will get client id and secret. So set environment variable as 

```
export imgur_id="{id}"
export imgur_secret="{secret}"
```
5. Put it in bashrc for more permanent use. Source it.
