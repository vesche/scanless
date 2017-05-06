# scanless

Command-line utility for using websites that can perform port scans on your behalf. Useful for early stages of a penetration test or if you'd like to run a port scan on a host and have it not come from your IP address.

[**scanless**](http://www.urbandictionary.com/define.php?term=scanless) (adj): lacking respectable morals. _That girl is scanless!_

## Public Port Scanners
* [viewdns.info](http://viewdns.info/)
* [hackertarget.com](https://hackertarget.com/nmap-online-port-scanner/)
* [www.t1shopper.com](http://www.t1shopper.com/tools/port-scan/) (not yet implemented)
* [www.yougetsignal.com](http://www.yougetsignal.com/) (not yet implemented)

## Usage
Requires the `requests` and `bs4` libraries to run, install with pip.
```
$ python scanless.py --help
usage: scanless.py [-h] [-t TARGET] [-s SCANNER] [-l] [-a]

scanless, public port scan scrapper

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        ip or domain to scan
  -s SCANNER, --scanner SCANNER
                        scanner to use (default: viewdns)
  -l, --list            list scanners
  -a, --all             use all the scanners

$ python scanless.py --list
Scanner Name | Website
-------------|--------------------------
viewdns      | http://viewdns.info/
hackertarget | https://hackertarget.com/

$ python scanless.py -a -t scanme.nmap.org
Running scanless...

------- viewdns -------
PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
23/tcp   closed telnet
25/tcp   closed smtp
53/tcp   closed dns
80/tcp   open   http
110/tcp  closed pop3
139/tcp  closed netbios
143/tcp  closed imap
443/tcp  closed https
445/tcp  closed smb
1433/tcp closed mssql
1521/tcp closed oracle
3306/tcp closed mysql
3389/tcp closed rdp
-----------------------

------- hackertarget -------
tarting Nmap 7.01 ( https://nmap.org ) at 2017-05-06 02:31 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.065s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
PORT     STATE  SERVICE       VERSION
21/tcp   closed ftp
22/tcp   open   ssh           OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
23/tcp   closed telnet
25/tcp   closed smtp
80/tcp   open   http          Apache httpd 2.4.7 ((Ubuntu))
110/tcp  closed pop3
143/tcp  closed imap
443/tcp  closed https
445/tcp  closed microsoft-ds
3389/tcp closed ms-wbt-server
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.05 second
----------------------------
```
