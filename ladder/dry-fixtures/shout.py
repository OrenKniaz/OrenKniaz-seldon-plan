import argparse
import sys

argparse.ArgumentParser().parse_args()
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sys.stdout.write(sys.stdin.read().upper())
