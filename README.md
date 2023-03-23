# scanless

This is a Python command-line utility and library for using websites that can perform port scans on your behalf.

## Supported Online Port Scanners

* [ipfingerprints](http://www.ipfingerprints.com/portscan.php)
* [spiderip](https://spiderip.com/online-port-scan.php)
* [standingtech](https://portscanner.standingtech.com/)
* [viewdns](http://viewdns.info/)
* [yougetsignal](http://www.yougetsignal.com/tools/open-ports/)

## Install

Do it up:
```
$ pip install scanless --user
```

## CLI Usage

```
$ scanless --help
usage: scanless [-h] [-v] [-t TARGET] [-s SCANNER] [-r] [-l] [-a] [-d]

scanless, an online port scan scraper.

options:
  -h, --help            show this help message and exit
  -v, --version         display the current version
  -t TARGET, --target TARGET
                        ip or domain to scan
  -s SCANNER, --scanner SCANNER
                        scanner to use (default: yougetsignal)
  -r, --random          use a random scanner
  -l, --list            list scanners
  -a, --all             use all the scanners
  -d, --debug           debug mode (cli mode off & show network errors)

$ scanless --list
+----------------+--------------------------------------+
| Scanner Name   | Website                              |
+----------------+--------------------------------------+
| ipfingerprints | https://www.ipfingerprints.com       |
| spiderip       | https://spiderip.com                 |
| standingtech   | https://portscanner.standingtech.com |
| viewdns        | https://viewdns.info                 |
| yougetsignal   | https://www.yougetsignal.com         |
+----------------+--------------------------------------+

$ scanless -t scanme.nmap.org -s spiderip
Running scanless v2.2.1 ...

spiderip:
PORT      STATE  SERVICE
21/tcp    closed ftp
22/tcp    open   ssh
25/tcp    closed smtp
80/tcp    open   http
110/tcp   closed pop3
143/tcp   closed imap
443/tcp   closed https
465/tcp   closed smtps
993/tcp   closed imaps
995/tcp   closed pop3s
1433/tcp  closed ms-sql-s
3306/tcp  closed mysql
3389/tcp  closed ms-wbt-server
5900/tcp  closed vnc
8080/tcp  closed http-proxy
8443/tcp  closed https-alt
```

## Library Usage

```
>>> import scanless
>>> sl = scanless.Scanless()
>>> output = sl.scan('scanme.nmap.org', scanner='yougetsignal')
>>> print(output['raw'])
PORT      STATE  SERVICE
21/tcp    closed ftp
22/tcp    open   ssh
23/tcp    closed telnet
25/tcp    closed smtp
53/tcp    closed domain
80/tcp    open   http
110/tcp   closed pop3
115/tcp   closed sftp
135/tcp   closed msrpc
139/tcp   closed netbios-ssn
143/tcp   closed imap
194/tcp   closed irc
443/tcp   closed https
445/tcp   closed microsoft-ds
1433/tcp  closed ms-sql-s
3306/tcp  closed mysql
3389/tcp  closed ms-wbt-server
5632/tcp  closed pcanywherestat
5900/tcp  closed vnc
6112/tcp  closed dtspc
>>> import json
>>> print(json.dumps(output['parsed'], indent=2))
[
  {
    "port": "21",
    "state": "closed",
    "service": "ftp",
    "protocol": "tcp"
  },
  {
    "port": "22",
    "state": "open",
    "service": "ssh",
    "protocol": "tcp"
  },
  {
    "port": "23",
    "state": "closed",
    "service": "telnet",
    "protocol": "tcp"
  },
  {
    "port": "25",
    "state": "closed",
    "service": "smtp",
    "protocol": "tcp"
  },
  {
    "port": "53",
    "state": "closed",
    "service": "domain",
    "protocol": "tcp"
  },
  {
    "port": "80",
    "state": "open",
    "service": "http",
    "protocol": "tcp"
  },
  ...
]
```
