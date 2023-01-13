from os import system as cmd
import requests
from bs4 import BeautifulSoup
from pick import pick
import yaml

def download_file(url):
    cmd(f'wget -c --retry-connrefused --tries=0 --timeout=5 {url}')

# amd64
def get_arch_amd64():
    URL = 'https://www.archlinux.org/download/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if 'agdsn.de' in link.text:
            file_dir = str(link.get('href'))
            break
    r = requests.get(file_dir)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso'):
            file = str(link.get('href'))
            break
    iso_urls['amd64']['arch'] = file_dir + file

def get_endevouros_amd64():
    URL = 'https://endeavouros.com/latest-release/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso'):
            file = str(link.get('href'))
    iso_urls['amd64']['endeavouros'] = URL + file

def get_fedora_amd64():
    URL = 'https://getfedora.org/en/server/download/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')):
            file = str(link.get('href'))
            break
    iso_urls['amd64']['fedora'] = file

def get_kali_amd64():
    URL = 'https://www.kali.org/get-kali/#kali-installer-images'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')) and 'amd64' in str(link.get('href')):
            file = str(link.get('href'))
            break
    iso_urls['amd64']['kali'] = file

def get_nixos_amd64():
    URL = 'https://nixos.org/download.html'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'gnome-x86' in str(link.get('href')):
            file = str(link.get('href'))
            break
    iso_urls['amd64']['nixos'] = file

def get_ubuntu_amd64():
    URL = 'https://ubuntu.com/download/server#architectures'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso'):
            file = str(link.get('href'))
            break
    iso_urls['amd64']['ubuntu'] = file

# arm64
def get_debian_arm64():
    URL = 'https://cdimage.debian.org/debian-cd/current/arm64/iso-cd/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso'): 
            file = str(link.get('href'))
            break
    iso_urls['arm64']['debian'] = URL + file

def get_fedora_arm64():
    URL = 'https://getfedora.org/en/server/download/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')) and 'aarch64' in str(link.get('href')):
            file = str(link.get('href'))
            break
    iso_urls['arm64']['fedora'] = file

def get_kali_arm64():
    URL = 'https://www.kali.org/get-kali/#kali-installer-images'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')) and 'arm64' in str(link.get('href')):
            file = str(link.get('href'))
            break
    iso_urls['arm64']['kali'] = file

def get_nixos_arm64():
    URL = 'https://nixos.org/download.html'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'gnome-aarch64' in str(link.get('href')):
            file = str(link.get('href'))
            break
    iso_urls['arm64']['nixos'] = file



iso_urls = {
    'amd64':{
        'arch': '',
        'debian': 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/weekly-builds/amd64/iso-cd/firmware-testing-amd64-netinst.iso',
        'endeavouros': '',
        'fedora': '',
        'kali': '',
        'nixos': ''
        },
    'arm64':{
        'debian': '',
        'fedora': '',
        'kali': '',
        'nixos': ''
        }
    }

title = 'Please choose your architecture: '
options = ['amd64', 'arm64']
option, index = pick(options, title)
if option == 'amd64':
    title = 'Please choose your OS: '
    options = list(iso_urls['amd64'].keys())
    selected = pick(options, title, multiselect=True, min_selection_count=1)
    items = [i[0] for i in selected]
    for i in items:
        if i == 'arch':
            get_arch_amd64()
            download_file(iso_urls[option]['arch'])
        elif i == 'debian':
            download_file(iso_urls[option]['debian'])
        elif i == 'fedora':
            get_fedora_amd64()
            download_file(iso_urls[option]['fedora'])
        elif i == 'kali':
            get_kali_amd64()
            download_file(iso_urls[option]['kali'])
        elif i == 'nixos':
            get_nixos_amd64()
            download_file(iso_urls[option]['nixos'])
            
elif option == 'arm64':
    title = 'Please choose your OS: '
    options = list(iso_urls['arm64'].keys())
    selected = pick(options, title, multiselect=True, min_selection_count=1)
    items = [i[0] for i in selected]
    for i in items:
        if i == 'debian':
            get_debian_arm64()
            download_file(iso_urls[option]['debian'])
        elif i == 'fedora':
            get_fedora_arm64()
            download_file(iso_urls[option]['fedora'])
        elif i == 'kali':
            get_kali_arm64()
            download_file(iso_urls[option]['kali'])
        elif i == 'nixos':
            get_nixos_arm64()
            download_file(iso_urls[option]['nixos'])
            
        print(items)