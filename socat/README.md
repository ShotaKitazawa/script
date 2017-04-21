# socat - Multipurpose relay

## Abstract

what: "netcat++" (extended design, new implementation)
OS:   AIX, BSD, HP-UX, Linux, Solaris e.a. (UNIX)
lic:  GPL2
inst: tar x...; ./configure; make; make install
doc:  README; socat.html, socat.1; xio.help
ui:   command line
exa:  socat TCP6-LISTEN:8080,reuseaddr,fork PROXY:proxy:www.domain.com:80
keyw: tcp, udp, ipv6, raw ip, unix-socket, pty, pipe, listen, socks4, socks4a,
      proxy-connect, ssl-client, filedescriptor, readline, stdio,
      exec, system, file, open, tail -f, termios, setsockopt, chroot,
      fork, perm, owner, trace, dump, dgram, ext3, resolver, datagram,
      multicast, broadcast, interface, socket, sctp, generic, ioctl

