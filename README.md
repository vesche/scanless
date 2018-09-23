# scanless

Command-line utility for using websites that can perform port scans on your behalf.

[**scanless**](http://www.urbandictionary.com/define.php?term=scanless) (adj): lacking respectable morals. _That girl is scanless!_

## Supported Online Port Scanners
* [yougetsignal](http://www.yougetsignal.com/tools/open-ports/)
* [viewdns](http://viewdns.info/)
* [hackertarget](https://hackertarget.com/nmap-online-port-scanner/)
* [ipfingerprints](http://www.ipfingerprints.com/portscan.php)
* [pingeu](http://ping.eu/port-chk/)
* [spiderip](https://spiderip.com/online-port-scan.php)
* [t1shopper](http://www.t1shopper.com/tools/port-scan/)
* [standingtech](https://portscanner.standingtech.com/)

## Install

To install, simply run:
```
$ sudo pip install scanless
```

## Usage

```
$ scanless --help  
usage: scanless [-h] [-v] [-t TARGET] [-s SCANNER] [-r] [-l] [-a]

scanless, public port scan scrapper

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         display the current version
  -t TARGET, --target TARGET
                        ip or domain to scan
  -s SCANNER, --scanner SCANNER
                        scanner to use (default: hackertarget)
  -r, --random          use a random scanner
  -l, --list            list scanners
  -a, --all             use all the scanners

$ scanless --list
Scanner Name   | Website
---------------|------------------------------
yougetsignal   | http://www.yougetsignal.com
viewdns        | http://viewdns.info
hackertarget   | https://hackertarget.com
ipfingerprints | http://www.ipfingerprints.com
pingeu         | http://ping.eu
spiderip       | https://spiderip.com
t1shopper      | http://www.t1shopper.com
standingtech   | https://portscanner.standingtech.com

$ scanless -t scanme.nmap.org -s ipfingerprints
Running scanless...

------- ipfingerprints -------
Host is up (0.16s latency).
Not shown: 491 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.6
Network Distance: 7 hops
------------------------------

$ scanless -a -t scanme.nmap.org
Running scanless...

------- yougetsignal -------
PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
23/tcp   closed telnet
25/tcp   closed smtp
53/tcp   closed dns
80/tcp   open   http
110/tcp  closed pop3
115/tcp  closed sftp
135/tcp  closed msrpc
139/tcp  closed netbios
143/tcp  closed imap
194/tcp  closed irc
443/tcp  closed https
445/tcp  closed smb
1433/tcp closed mssql
3306/tcp closed mysql
3389/tcp closed rdp
5632/tcp closed pcanywhere
5900/tcp closed vnc
6112/tcp closed wc3
----------------------------

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
Starting Nmap 7.01 ( https://nmap.org ) at 2017-05-14 16:46 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.066s latency).
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
Nmap done: 1 IP address (1 host up) scanned in 6.94 seconds
----------------------------

------- ipfingerprints -------
Host is up (0.16s latency).
Not shown: 491 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.6
Network Distance: 7 hops
------------------------------

------- pingeu -------
PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
23/tcp   closed telnet
25/tcp   closed smtp
53/tcp   closed dns
80/tcp   open   http
139/tcp  closed netbios
443/tcp  closed https
445/tcp  closed smb
3389/tcp closed rdp
----------------------

------- spiderip -------
PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
25/tcp   closed smtp
80/tcp   open   http
110/tcp  closed pop3
143/tcp  closed imap
443/tcp  closed https
465/tcp  closed smtps
993/tcp  closed imaps
995/tcp  closed pop3s
1433/tcp closed mssql
3306/tcp closed mysql
3389/tcp closed rdp
5900/tcp closed vnc
8080/tcp closed http-alt
8443/tcp closed https-alt
------------------------

------- t1shopper -------
PORT     STATE  SERVICE
21/tcp   closed ftp
23/tcp   closed telnet
25/tcp   closed smtp
80/tcp   open   http
110/tcp  closed pop3
139/tcp  closed netbios
445/tcp  closed smb
1433/tcp closed mssql
1521/tcp closed oracle
1723/tcp closed pptp
3306/tcp closed mysql
3389/tcp closed rdp
5900/tcp closed vnc
8080/tcp closed http-alt
-------------------------

------- standingtech -------
PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
23/tcp   closed telnet
25/tcp   closed smtp
80/tcp   open   http
110/tcp  closed pop3
139/tcp  closed netbios
143/tcp  closed imap
443/tcp  closed https
445/tcp  closed smb
1433/tcp closed mssql
3306/tcp closed mysql
3389/tcp closed rdp
5900/tcp closed vnc
----------------------------
```

## Docker

### Build

To build the docker image, run:

```shell
$ docker build -t scanless .
```

### Usage

To use the docker image previously created, run the following with whichever options you want like `--help`:

```shell
$ docker run --rm -it scanless --help
```

If the that long command it's too troublesome, you can make an alias with this: `alias scanless="docker run --rm -it scanless"` and you can make use of the `scanless` alias like before:

```shell
$ scanless --help
$ scanless -l
$ scanless -t somedomain.com -s yougetsignal
```
