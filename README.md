# scanless

This is a Python 3 command-line utility and library for using websites that can perform port scans on your behalf.

## Supported Online Port Scanners

* [hackertarget](https://hackertarget.com/nmap-online-port-scanner/)
* [ipfingerprints](http://www.ipfingerprints.com/portscan.php)
* [spiderip](https://spiderip.com/online-port-scan.php)
* [standingtech](https://portscanner.standingtech.com/)
* [t1shopper](http://www.t1shopper.com/tools/port-scan/)
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
usage: scanless [-h] [-v] [-t TARGET] [-s SCANNER] [-r] [-l] [-a]

scanless, an online port scan scraper.

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
  -d, --debug           debug mode (cli mode off & show network errors)

$ scanless --list
+----------------+--------------------------------------+
| Scanner Name   | Website                              |
+----------------+--------------------------------------+
| hackertarget   | https://hackertarget.com             |
| ipfingerprints | https://www.ipfingerprints.com       |
| spiderip       | https://spiderip.com                 |
| standingtech   | https://portscanner.standingtech.com |
| t1shopper      | http://www.t1shopper.com             |
| viewdns        | https://viewdns.info                 |
| yougetsignal   | https://www.yougetsignal.com         |
+----------------+--------------------------------------+

$ scanless -t scanme.nmap.org -s spiderip
Running scanless v2.1.3...

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
>>> output = sl.scan('scanme.nmap.org', scanner='hackertarget')
>>> print(output['raw'])
Starting Nmap 7.70 ( https://nmap.org ) at 2020-05-12 21:39 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.065s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

PORT    STATE  SERVICE
21/tcp  closed ftp
22/tcp  open   ssh
80/tcp  open   http
443/tcp closed https

Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
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
    "port": "80",
    "state": "open",
    "service": "http",
    "protocol": "tcp"
  },
  {
    "port": "443",
    "state": "closed",
    "service": "https",
    "protocol": "tcp"
  }
]
```

## Docker

**Note from the repo author:** I did not create, nor do I maintain Docker support or the Dockerfile for scanless. It was a nice community addition. If it's broken please open an issue or submit a pull request and I'll take a look. Thank you!

### Build

To build the Docker image, run:
```shell
$ docker build -t scanless .
```

### Usage

To use the Docker image previously created, run the following with whichever options you want like `--help`:
```
$ docker run --rm -it scanless --help
```

If that long command is too troublesome, you can make an alias like so: `alias scanless="docker run --rm -it scanless"` and then run `scanless` as you would normally:
```
$ scanless --help
$ scanless -l
$ scanless -t scanme.nmap.org -s yougetsignal
```
