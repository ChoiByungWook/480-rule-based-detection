import collections
import fileinput
import sys

def main():
    log_file = str(sys.argv[1])

    for line in fileinput.input(log_file):
        server_log_tuple = convert_line_to_server_log_tuple(line)

def convert_line_to_server_log_tuple(line):
    ServerLogTuple = collections.namedtuple('log_line', ['number', 'date', 'time', 'duration', 'protocol', 'src_port', 'destination_port', 'src_ip', 'destination_ip'])
    split_line = line.split(" ")

    number = split_line[0]
    date = split_line[1]
    time = split_line[2]
    duration = split_line[3]
    protocol = split_line[4]
    src_port = split_line[5]
    destination_port = split_line[6]
    src_ip = split_line[7]
    destination_ip = split_line[8]

    server_log_tuple = ServerLogTuple(number, date, time, duration, protocol, src_port, destination_port, src_ip, destination_ip)

    return server_log_tuple

if __name__ == '__main__':
    main()