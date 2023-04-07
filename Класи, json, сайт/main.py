import os
import requests
import json

file_Men = 'Men'
file_Inoplun = 'Inoplun'
file_Komaxu = 'Komaxu'

class VSI():
    def __init__(self, men, Inoplun, Komaxu):
        self.men = men
        self.Inoplun = Inoplun
        self.Komaxu = Komaxu

    def poshyk(self):
        for i in range(30):
            response = requests.get(f"https://rickandmortyapi.com/api/character/{i + 1}").json()
            if response["species"] == "Human":
                vsi_Men.append(response)

            if response["species"] == "Alien":
                vsi_Inoplun.append(response)

            if response["species"] == "Humanoid":
                vsi_Komaxu.append(response)


def loading_toJSON(value, directory):
    try:
        with open(f'{directory}.json', 'w') as write_file:
            json.dump(value, write_file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Error: {str(e)}')

vsi = []
vsi_Inoplun = []
vsi_Komaxu = []
vsi_Men = []
for i in range(30):
    response = requests.get(f"https://rickandmortyapi.com/api/character/{i+1}").json()
    if response["species"] == "Human":
        vsi_Men.append(response)


    if response["species"] == "Alien":
        vsi_Inoplun.append(response)

    if response["species"] == "Humanoid":
        vsi_Komaxu.append(response)




loading_toJSON(vsi_Men, file_Men)
loading_toJSON(vsi_Inoplun, file_Inoplun)
loading_toJSON(vsi_Komaxu, file_Komaxu)










