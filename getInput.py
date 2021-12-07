import sys
import time
import requests
import configparser
from termcolor import colored
print(colored('tips:', 'green'), 'passing year and day to fetch specify input')
#print ('Number of arguments:', len(sys.argv), 'arguments.')
if len(sys.argv)>2:
    print('year: ' + sys.argv[1], 'day:' + sys.argv[2])
    year,day = sys.argv[1],sys.argv[2]
year = year if 'year' in locals() else time.localtime().tm_year
day = day if 'day' in locals() else time.localtime().tm_mday
print(f'fetching input of Year: {year}, Day: {day}')
url = f'https://adventofcode.com/{year}/day/{day}/input'
config = configparser.ConfigParser()
config.read('./config.ini')
cookie = config.get('login', 'cookie')
hd = {'User-Agent': 'Mozilla', 'cookie':cookie}
r = requests.get(url, headers=hd)
r.raise_for_status()
print(r.text)
with open(f'./{year}/{day}.in', 'w') as file:
    file.write(r.text) 