import re

from config import Config

def read_subdomains():
    lines = [] 
    with open(Config.SUBDOMAIN_FILE, 'r+') as f:
        lines = f.readlines()
    if lines is None:
        print('none')
    return lines

def write_subdomains(lines):
    with open(Config.SUBDOMAIN_FILE, 'w+') as f:
        f.writelines(lines)

def add_subdomain(subdomain):
    lines = read_subdomains()
    lines.append(subdomain + "-CREATED\n")
    write_subdomains(lines)

def get_status(subdomain):
    lines = read_subdomains()
    for l in lines:
        if re.match("{}-.*".format(subdomain), l):
            info = l.split("-")
            return info[1]
    return None

def get_subdomains():
    lines = read_subdomains()
    subdomains = []
    for l in lines:
        info = l.split("-")
        subdomains.append({
            'name': info[0],
            'status': info[1]
            })
    return subdomains 
    

