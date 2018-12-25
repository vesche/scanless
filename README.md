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
```shell
$ pip install scanless --user
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
