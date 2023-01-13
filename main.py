from os import system as cmd
import requests
from bs4 import BeautifulSoup
from pick import pick
import yaml

cmd('rm -fr main.py')
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
            iso_urls['amd64']['arch'] = file_dir + str(link.get('href'))
            break

def get_debian_amd64():
    URL = 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/weekly-builds/amd64/iso-cd/firmware-testing-amd64-netinst.iso'
    iso_urls['amd64']['debian'] = URL

def get_endeavouros_amd64():
    URL = 'https://endeavouros.com/latest-release/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso'):
            iso_urls['amd64']['endeavouros'] = URL + str(link.get('href'))
 
def get_fedora_amd64():
    URL = 'https://getfedora.org/en/server/download/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')):
            iso_urls['amd64']['fedora'] = str(link.get('href'))
            break

def get_kali_amd64():
    URL = 'https://www.kali.org/get-kali/#kali-installer-images'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')) and 'amd64' in str(link.get('href')):
            iso_urls['amd64']['kali'] = str(link.get('href'))
            break

def get_nixos_amd64():
    URL = 'https://nixos.org/download.html'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'gnome-x86' in str(link.get('href')):
            iso_urls['amd64']['nixos'] = str(link.get('href'))
            break

def get_ubuntu_amd64():
    URL = 'https://ubuntu.com/download/server#architectures'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso'):
            iso_urls['amd64']['ubuntu'] = str(link.get('href'))
            break

# arm64
def get_debian_arm64():
    URL = 'https://cdimage.debian.org/debian-cd/current/arm64/iso-cd/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso'): 
            iso_urls['arm64']['debian'] = URL + str(link.get('href'))
            break

def get_fedora_arm64():
    URL = 'https://getfedora.org/en/server/download/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')) and 'aarch64' in str(link.get('href')):
            iso_urls['arm64']['fedora'] = str(link.get('href'))
            break

def get_kali_arm64():
    URL = 'https://www.kali.org/get-kali/#kali-installer-images'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'netinst' in str(link.get('href')) and 'arm64' in str(link.get('href')):
            iso_urls['arm64']['kali'] = str(link.get('href'))
            break

def get_nixos_arm64():
    URL = 'https://nixos.org/download.html'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).endswith('.iso') and 'gnome-aarch64' in str(link.get('href')):
            iso_urls['arm64']['nixos'] = str(link.get('href'))
            break

iso_urls = {
    'amd64':{
        'arch': '',
        'debian': '',
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
elif option == 'arm64':
    title = 'Please choose your OS: '
    options = list(iso_urls['arm64'].keys())
    selected = pick(options, title, multiselect=True, min_selection_count=1)

for i in [i[0] for i in selected]:
    exec(f'get_{i}_{option}()')
for url in [url for url in list(iso_urls['amd64'].values()) + list(iso_urls['arm64'].values()) if url != '']:
    download_file(url)