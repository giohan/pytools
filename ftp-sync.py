from ftplib import FTP
from time import sleep
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-s', '--server',
                  dest="server")
parser.add_option('-u', '--username',
                  dest="username")
parser.add_option('-p', '--password',
                  dest="password")
parser.add_option('-d', '--directory',
                  dest="directory",
                  default='/')
parser.add_option('-i', '--interval',
                  dest="interval",
                  default=100)
(opts, args) = parser.parse_args()

if opts.server is None or opts.username is None or opts.password is None:
    print "Missing mandatory option\n"
    parser.print_help()
    exit(-1)

server = opts.server
username = opts.username
password = opts.password
directory = opts.directory
interval = opts.interval

ftp = FTP(server)
ftp.login(username, password)
ftp.cwd(directory)

old_files = []
try:
    while True:
        new_files = ftp.nlst()
        if len(old_files) != 0 and new_files != old_files:
            changes = [i for i in new_files if i not in old_files]
            print changes
        sleep(interval)
        old_files = list(new_files)
except KeyboardInterrupt:
    ftp.quit()

