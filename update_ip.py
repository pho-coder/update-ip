#!/usr/bin/env python3
import os
from urllib import request
import sys


def get_ip():
    url = "http://members.3322.org/dyndns/getip"
    req = request.urlopen(url)
    return req.read().decode().split("\n")[0]


if __name__ == '__main__':
    remote = sys.argv[1]
    ip = get_ip()
    ip_file = "/home/phoenix/ip"
    with open(ip_file, "w") as f:
        f.write(ip)
    os.system("scp " + ip_file + " " + remote + ":~/")
