import subprocess as sub
import os
import shutil
import glob
import random
import signal
import threading
import argparse
from time import sleep

exit_event = threading.Event()

def bg_thread(set):
    for percent in set:
        for agregado in range(0,5):
            print(percent, agregado)
            sleep(20)

        if exit_event.is_set():
            break

    i = 100
    print(f'{i} iterations completed before exiting.')


def signal_handler(signum, frame):
    exit_event.set()


def main():

    parser = argparse.ArgumentParser(usage=__doc__)

    # Definicao dos percentuais de varredura (geracao dos arquivos)

    parser.add_argument(
        "--p0", type=float, default=0.10, help="percentual inicial de agregados"
    )
    parser.add_argument(
        "--pf", type=float, default=0.50, help="percentual final de agregados"
    )
    parser.add_argument(
        "--step", type=int, default=2, help="variacao de cada percentual"
    )

    args = parser.parse_args()

    p0 = int(args.p0 * 100)

    pf = int(args.pf * 100)

    step_percent = args.step

    set = (x * 0.01 for x in range(p0, pf, step_percent))

    signal.signal(signal.SIGINT, signal_handler)
    th = threading.Thread(target=bg_thread(set))
    th.start()
    th.join()

if __name__ == "__main__":
    main()
