import sys
import psutil

def main():
    """Function revision"""
    sys.stdout.write("Hello, World!",)
    pass

def cpu_check():
    a = psutil.cpu_percent(1)
    print(a)

cpu_check()
main()

