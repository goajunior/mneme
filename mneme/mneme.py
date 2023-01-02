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


def bg_thread(set, curva_gan):

    command = 'python3 scripts/gen_2d.py '
    argument_head = '--percent '
    argument_tail = ' --agreg '

    check_event = True

    while check_event:
        for percent in set:
            argument_head = '--percent '
            percent_str = str(percent)
            for agregado in range(curva_gan, 5):
                command = 'python3 scripts/gen_2d.py '
                print(percent, agregado)
                agregado_str = str(agregado)
                command = command + argument_head + percent_str + argument_tail + agregado_str
                print(command)
                sleep(2)
                sub.run([command], shell=True)
        if exit_event.is_set():
            check_event = False


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
    parser.add_argument(
        "--gran", type=int, default=0, help="curva granulometrica de inicio"
    )

    args = parser.parse_args()

    p0 = int(args.p0 * 100)

    pf = int(args.pf * 100)

    step_percent = args.step

    curva_gan = args.gran

    set = (x * 0.01 for x in range(p0, pf, step_percent))

    signal.signal(signal.SIGINT, signal_handler)
    th = threading.Thread(target=bg_thread(set, curva_gan))
    th.start()
    th.join()

if __name__ == "__main__":
    main()
