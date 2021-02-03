import urllib.request
import time
import re
import subprocess

from Tools.scripts.treesync import raw_input

url = input("输入电影的的地址：")
dizhi = "https://660e.com/?url=" + url

print("确认地址:" + dizhi)
time.sleep(0.7)

print("")

print("以下为网页解析的网页代码，请自行找出m3u8地址")

response = urllib.request.urlopen(dizhi)

html = response.read().decode('utf-8')
print(html)

url = re.search(r"""url=(.*.m3u8)""", html).group(1)
print(url)

command = "ffmpeg -i " + url + "  -vcodec copy -acodec copy  1.mp4"

print(subprocess.call(command)
      )
raw_input("Press <enter>")