# -*- coding: utf-8 -*-

# open source code 
# get data users github by Dekura 
# source api : https://docs.github.com/en/rest/users
# report bug program nimetuber@gmail.com


import os,sys,json
import requests as req


# * Warna 

h = "\033[1;32m"
m = "\033[1;39m"
k = "\033[1;33m"
p = "\033[1;37m"

url='https://api.github.com/users/'
os.system('clear')
user=input(f'\n\n\n{p} ! masukan users github\n ? users: ')
try:
    response=req.get(url+user).json()
    nama=response['name']
except KeyError:
    print(f'\n{p} ! user tidak di temukan');exit()
print(f'\n{p} [ INFORMASI AKUN GITHUB PUBLIK ]')
print(f'\n{p} nama: {h}{nama}')
print(f'{p} company: {h}{response["company"]}')
print(f'{p} lokasi: {h}{response["location"]}')
print(f'{p} email: {h}{response["email"]}')
print(f'{p} bio: {h}{response["bio"]}')
print(f'{p} twitter: {h}{response["twitter_username"]}')
print(f'{p} repository: {h}{response["public_repos"]}')
print(f'{p} gists: {h}{response["public_gists"]}')
print(f'{p} pengikut: {h}{response["followers"]}')
print(f'{p} mengikuti: {h}{response["following"]}')
print(f'{p} di buat pada: {h}{response["created_at"].split("T")[0]}')
print(f'{p} di perbarui pada: {h}{response["updated_at"].split("T")[0]}{p}')


