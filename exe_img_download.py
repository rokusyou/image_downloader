import csv
import time
import urllib.error
import urllib.request

OUT_DIR = './download_images/'
INTERVAL = 1
def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

with open('./items_image_urls.csv') as f:
  reader = csv.reader(f)
  num = 1
  for row in reader:
    jan = row[0]
    url = row[1]
    num_str = str(num).zfill(4)
    print( num_str + ":" + jan + " : " + url)
    download_file(url, OUT_DIR + "img_" + num_str + ".jpg")
    num += 1
    time.sleep(INTERVAL)
