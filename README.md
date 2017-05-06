# scanless

Command-line utility for using websites that can perform port scans on your behalf. Useful for early stages of a penetration test or if you'd like to run a port scan on a host so that it won't come from your IP.

[**scanless**](http://www.urbandictionary.com/define.php?term=scanless) (adj): lacking respectable morals. _That girl is scanless!_

## Public Port Scanners
* [viewdns.info](http://viewdns.info/)
* [hackertarget.com](https://hackertarget.com/nmap-online-port-scanner/)
* [www.t1shopper.com](http://www.t1shopper.com/tools/port-scan/)
* [www.yougetsignal.com](http://www.yougetsignal.com/)

## Usage
```
$ python scanless.py --help
usage: scanless.py [-h] -t TARGET

scanless, public port scan scrapper

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        ip or domain to scan

$ python scanless.py -t scanme.nmap.org
Running scanless...

PORT     STATE  SERVICE
  21/tcp closed     ftp
  22/tcp   open     ssh
  23/tcp closed  telnet
  25/tcp closed    smtp
  53/tcp closed     dns
  80/tcp   open    http
 110/tcp closed    pop3
 139/tcp closed netbios
 143/tcp closed    imap
 443/tcp closed   https
 445/tcp closed     smb
1433/tcp closed   mssql
1521/tcp closed  oracle
3306/tcp closed   mysql
3389/tcp closed     rdp
```
