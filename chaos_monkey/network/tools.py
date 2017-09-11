import socket
import select
import logging

DEFAULT_TIMEOUT = 1.5
BANNER_READ = 1024

LOG = logging.getLogger(__name__)


def check_port_tcp(ip, port, timeout=DEFAULT_TIMEOUT, get_banner=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((ip, port))
        banner = None
        if get_banner:
            read_ready, _, _ = select.select([sock], [], [], timeout)
            if len(read_ready) > 0:
                banner = sock.recv(BANNER_READ)
    except socket.timeout:
        return False, None
    except socket.error, exc:
        LOG.debug("Check port: %s:%s, Exception: %s", ip, port, exc)
        return False, None

    sock.close()
    return True, banner


def check_port_udp(ip, port, timeout=DEFAULT_TIMEOUT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)

    data = None
    is_open = False

    try:
        sock.sendto("-", (ip, port))
        data, _ = sock.recvfrom(BANNER_READ)
        is_open = True
        sock.close()
    except socket.error:
        pass

    return is_open, data
