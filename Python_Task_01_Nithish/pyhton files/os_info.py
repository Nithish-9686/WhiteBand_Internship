import os
import platform
import sys

print("=" * 40)
print("        OS INFORMATION")
print("=" * 40)
print(f"Operating System : {platform.system()} {platform.release()}")
print(f"Current Username : {os.getlogin()}")
print(f"Working Directory: {os.getcwd()}")
print(f"Python Version   : {sys.version}")
print("=" * 40)