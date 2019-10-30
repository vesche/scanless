# scanless

Command-line utility and library for using websites that can perform port scans on your behalf.

[**scanless**](http://www.urbandictionary.com/define.php?term=scanless) (adj): lacking respectable morals. _That girl is scanless!_

## Supported Online Port Scanners

* [hackertarget](https://hackertarget.com/nmap-online-port-scanner/)
* [ipfingerprints](http://www.ipfingerprints.com/portscan.php)
* [pingeu](http://ping.eu/port-chk/)
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

$ scanless --list
+----------------+--------------------------------------+
| Scanner Name   | Website                              |
+----------------|--------------------------------------+
| hackertarget   | https://hackertarget.com             |
| ipfingerprints | https://www.ipfingerprints.com       |
| pingeu         | https://ping.eu                      |
| spiderip       | https://spiderip.com                 |
| standingtech   | https://portscanner.standingtech.com |
| t1shopper      | http://www.t1shopper.com             |
| viewdns        | https://viewdns.info                 |
| yougetsignal   | https://www.yougetsignal.com         |
+----------------+--------------------------------------+

$ scanless -t scanme.nmap.org -s ipfingerprints
Running scanless v2.0.0...
Host is up (0.15s latency).
Not shown: 484 closed ports
PORT    STATE    SERVICE
22/tcp  open     ssh
80/tcp  open     http
111/tcp filtered rpcbind
135/tcp filtered msrpc
136/tcp filtered profile
137/tcp filtered netbios-ns
138/tcp filtered netbios-dgm
139/tcp filtered netbios-ssn
445/tcp filtered microsoft-ds
Aggressive OS guesses: Linux 2.6.32 - 3.13 (95%), Linux 2.6.22 - 2.6.36 (94%), Linux 3.10
(94%), Linux 3.10 - 4.2 (94%), Linux 2.6.32 (93%), Linux 3.2 - 4.6 (93%), Linux 2.6.32 - 3.10
(92%), Linux 2.6.18 (92%), Linux 3.16 - 4.6 (92%), HP P2000 G3 NAS device (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 7 hops
```

## Library Usage

```python
>>> import scanless
>>> sl = scanless.Scanless()
>>> list(sl.scanners.keys())
['hackertarget', 'ipfingerprints', 'pingeu', 'spiderip', 'standingtech', 't1shopper', 'viewdns', 'yougetsignal']
>>> output = sl.scan('scanme.nmap.org', scanner='hackertarget')
>>> print(output)
Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-30 00:21 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.065s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
23/tcp   closed telnet
80/tcp   open   http
110/tcp  closed pop3
143/tcp  closed imap
443/tcp  closed https
3389/tcp closed ms-wbt-server

Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
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

If that long command is too troublesome, you can make an alias like so: `alias scanless="docker run --rm -it scanless"` and then run `scanless` as you would normally:
```shell
$ scanless --help
$ scanless -l
$ scanless -t scanme.nmap.org -s yougetsignal
```
