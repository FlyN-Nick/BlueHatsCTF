from bs4 import BeautifulSoup
import requests
import time
from os import path

"""n_mins = 60 * 10
t_end = time.time() + (60 * n_mins)

while time.time() < t_end:
    r = requests.get('http://trumpipsum.net/?paras=99&type=make-it-great', verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    output = soup.find('div', class_= "anyipsum-output")
    paragraphs = output.find_all('p')
    text = ""
    for para in paragraphs:
        text += para.text
    with open("./trump.txt", "a") as file:
        file.write(text)
        print(str(path.getsize("./trump.txt")) + " bytes.")"""

with open ("./trump.txt", "a") as file:
    file.write("}HCRA35_3GUh{staHeulB is greater than ever before.")
