scanless
========

Command-line utility for using websites that can perform port scans on your behalf. Useful for early stages of a penetration test or if you'd like to run a port scan on a host and have it not come from your IP address.

`scanless <http://www.urbandictionary.com/define.php?term=scanless>`_ (adj): lacking respectable morals. *That girl is scanless!*

Supported Online Port Scanners
------------------------------

- `yougetsignal <http://www.yougetsignal.com/tools/open-ports/>`_
- `viewdns <http://viewdns.info/>`_
- `hackertarget <https://hackertarget.com/nmap-online-port-scanner/>`_
- `ipfingerprints <http://www.ipfingerprints.com/portscan.php>`_
- `pingeu <http://ping.eu/port-chk/>`_
- `spiderip <https://spiderip.com/online-port-scan.php>`_
- `portcheckers <http://www.portcheckers.com/>`_
- `t1shopper <http://www.t1shopper.com/tools/port-scan/>`_

Install & Usage
---------------

To install, simply run: ``pip install scanless``

.. code-block::
    $ scanless --help
    usage: scanless.py [-h] [-t TARGET] [-s SCANNER] [-l] [-a]

    scanless, public port scan scrapper

    optional arguments:
      -h, --help            show this help message and exit
      -t TARGET, --target TARGET
                            ip or domain to scan
      -s SCANNER, --scanner SCANNER
                            scanner to use (default: yougetsignal)
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
    portcheckers   | http://www.portcheckers.com
    t1shopper      | http://www.t1shopper.com

    $ scanless -s viewdns -t scanme.nmap.org
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
    Device type: general purpose
    Running: Linux 3.X
    OS CPE: cpe:/o:linux:linux_kernel:3
    OS details: Linux 3.11 - 3.14
    Network Distance: 10 hops
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

    -------- portcheckers --------
    PORT     STATE  SERVICE
    21/tcp   closed ftp
    22/tcp   open   ssh
    23/tcp   closed telnet
    25/tcp   closed smtp
    80/tcp   open   http
    110/tcp  closed pop3
    115/tcp  closed sftp
    143/tcp  closed imap
    443/tcp  closed https
    1433/tcp closed ms-sql-s
    3306/tcp closed mysql
    3389/tcp closed ms-wbt-server
    5900/tcp closed rfb
    8080/tcp closed webcache
    -----------------------------

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
