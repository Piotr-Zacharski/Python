import urllib.request

def img_dnl(url, file_path, file_name):
    full_path = file_path + file_name +'.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter img URL: ')
file_name = input('Enter file name to save as: ')

img_dnl(url, 'images/', file_name)
