# standard library
import sys
import argparse
# third-party
pass
# local
import rsync_system_backup

if not len(sys.argv) > 1:
    print("WARNING: you didn't specify any arguments, therefore appending --help..")
    sys.argv.append("--help")

from rsync_system_backup.cli import *
main()