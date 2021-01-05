import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.srce$sel31_v?choice=1&fcode=NG&fcourt=20&ftype=2'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ui_body_container')
# print(results.prettify())

elems = results.find_all('tr')
elem_arr = []
for elem in elems:
    # print(elem.text, end='\n'*2)
    elem_arr.append(elem.text)

timeslot_arr = []
for i in range(1, len(elem_arr)-20, 20):
    tmp = []
    for c in range(20):
        tmp.append(elem_arr[c+i])
    timeslot_arr.append(tmp)

# print(timeslot_arr[1])
slot_dict = {}


for i in range(len(timeslot_arr)):
    ind_dict = {}
    time1 = timeslot_arr[i]
    # print(time1)
    for slot in range(len(time1)):
        slot1 = time1[slot].split('/n')
        # print(slot)
        # print(slot1)
        if slot == 0:
            ma = slot1[0].split('\n')[3]
        else:
            ma = slot1[0].split('\n')[2]
        # print("ma", ma)
        ind_dict[slot+1] = ma
    slot_dict[time1[0].split('\n')[1]] = ind_dict



for key, value in slot_dict.items():
    for slot in value.values():
        if slot == "Avail":
            print("Slot available at time: ", key)

