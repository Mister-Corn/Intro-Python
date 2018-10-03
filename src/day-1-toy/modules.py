import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print(str(sys.argv))

for arg in sys.argv:
    print(f"{arg}")

# Print out the platform from sys:
print(f"Platform: {sys.platform}\n")

# Print out the Python version from sys:
print(f"Python Version: {sys.version_info}\n")



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f"Current Process ID: {os.getpid()}\n")

# Print the current working directory (cwd):
print(f"Current Working Directory: {os.getcwd()}\n")

# Print your login name
"""
Per Docs:
> For most purposes, it is more useful to use getpass.getuser() since the latter
> checks the environment variables LOGNAME or USERNAME to find out who the user is,
> and falls back to pwd.getpwuid(os.getuid())[0] to get the login name of the current
> real user id.
"""
from getpass import getuser
print(f"Current Login: {getuser()}\n")

