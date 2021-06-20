#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

import socket
import argparse
import time
import os
from argparse import RawTextHelpFormatter

def printLogo():
    print(r""" 
  ____            _                             
 / ___| _   _ ___| | ___   __ _                 
 \___ \| | | / __| |/ _ \ / _` |                
  ___) | |_| \__ | | (_) | (_| |                
 |____/ \__, |___|_|\___/ \__, |                
  ____  |___/             |___/   _             
 / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __ 
 \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
  ___) | | | | | | | |_| | | (_| | || (_) | |   
 |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   v1.0 
                @enesilhaydin                                                

                                                                                                                                                                                                                     
""")
    time.sleep(3)
    print(" ===Tanimli Kaynak Listesi=== \n")
    list=""
    for path, dirs, files in os.walk('logs'):
        for f in files:
            parca=path.split('\\')
            #print(len(parca)> 2)
            if(len(parca)>2):
                print("-- "+str(parca[1])+"\\"+parca[2]+"\\"+f)
                time.sleep(0.2)
                #print(path.s
            if(len(parca)==2):
                print("-- "+str(parca[1]) + "\\" + f)
                time.sleep(0.2)

    print("\n ================================")
def syslog(data, host, port=514, proto='udp'):

    if isinstance(port, str):
        port = int(port)

    try:
        s = False
        if proto.lower() == 'tcp':
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        elif proto.lower() == 'udp':
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        s.connect((host,port))
        s.send(data)
        s.close()
        return True
    except Exception as e:
        print("TCP portunun acik oldugundan veya baglantinin sorunsuz oldugundan emin olunuz...")

def logReader(path):
    with open('logs/'+path, "rb") as f:
        lines = f.readlines()
    return lines


parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)


parser.add_argument('-d', "--delay",
                    help="Her satir için bekleme süresini belirleyiniz..",
                    dest="delay",
                    default="0.5",
                    type=str)

parser.add_argument('-r', "--rotate",
                      type=int,
                      default=1,
                      help='Kaç kez gonderilecegini belirleyiniz.')

parser.add_argument('-s', '--server',
                      dest = "syslog_server",
                      action = "append",
                      default=[],
                      required = True,
                      help='Syslog alicilar\'i giriniz.')

parser.add_argument('-p', '--port',
                      dest = "syslog_port",
                      action = "store",
                      default="514",
                      help='Syslog gonderim portunu belirleyiniz.')

parser.add_argument('-P', '--protocol',
                      dest = "syslog_protocol",
                      action = "store",
                      default="udp",
                      help='Protokol\'u belirleyiniz.')


args = parser.parse_args()



def main():
    printLogo()
    kaynak = input("> Lutfen kaynagi giriniz = ")
    sayac = 1

    mesaj = logReader(kaynak)

    while True:
        if float(args.rotate) >= sayac:
            if float(args.rotate) == 10:
                for syslog_server in sorted(args.syslog_server):
                    for msg in mesaj:
                        syslog(msg, str(syslog_server), int(args.syslog_port), str(args.syslog_protocol))
                        time.sleep(float(args.delay))
                        print(msg)
                continue

            else:
                for syslog_server in sorted(args.syslog_server):
                    for msg in mesaj:
                        syslog(msg, str(syslog_server), int(args.syslog_port), str(args.syslog_protocol))
                        time.sleep(float(args.delay))
                        print(msg)
                    sayac = sayac + 1
        else:
            break


main()



