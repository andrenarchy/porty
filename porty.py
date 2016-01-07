#!/usr/bin/env python

import argparse
import random
import socket


def bindToPort(minPort, maxPort):
    ports = range(minPort, maxPort)
    random.shuffle(ports)
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            return port, sock
        except socket.error:
            pass
    raise RuntimeError('could not bind to a port')


def main():
    parser = argparse.ArgumentParser(description='get a free port within a '
                                                 'range')
    parser.add_argument('--min', type=int, default=32768,
                        help='minimum port number')
    parser.add_argument('--max', type=int, default=61000,
                        help='maximum port number')
    args = parser.parse_args()

    # get a port
    port, sock = bindToPort(args.min, args.max)
    sock.close()

    print(port)


if __name__ == "__main__":
    main()
