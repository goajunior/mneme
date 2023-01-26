import subprocess as sub
import os
import shutil
import glob
import signal
import threading
import argparse
from time import sleep

exit_event = threading.Event()


def bg_thread(set, curva_gan):
    """funcao que gera a thread que pode ser abortada com control-c

    Args:
        set (lista): lista dos percentuais a serem passados para o script gen_2d
        curva_gan (inteiro): curva granulometrica de inicio
    """
    argument_head = '--percent '
    argument_tail = ' --agreg '

    check_event = True

    while check_event:
        for percent in set:
            percent_str = str(percent)
            for agregado in range(curva_gan, 5):
                command = 'python3 scripts/gen_2d.py '
                print(percent, agregado)
                agregado_str = str(agregado)
                command = command + argument_head + percent_str + argument_tail + agregado_str
                print(command)
                sleep(1)
                sub.run([command], shell=True)
        if exit_event.is_set():
            check_event = False  # ao abortar, uma nova porcentagem em set eh selecionada


def gera_script(script_file):
    """Gera os scripts termico e mecanico

    Args:
        script_file (): tipo de script a ser gerado
    """
    for file in glob.glob('pre-termico/*.dgibi'):
        dir_target = 'termico-mecanico/' + file[25:27] + '.' + file[21]

        if os.path.exists(dir_target) is False:
            os.makedirs(dir_target)

        command = 'python3 scripts/' + script_file + '.py ' + '--file ' + file
        sub.run([command], shell=True)

        if os.path.exists('termico.py'):
            shutil.move('termico.py', dir_target)
        elif os.path.exists('mecanico.py'):
            shutil.move('mecanico.py', dir_target)


def signal_handler(signum, frame):
    exit_event.set()


def main():

    parser = argparse.ArgumentParser(usage=__doc__)

    # Definicao dos percentuais de varredura (geracao dos arquivos)

    parser.add_argument(
        "--p0", type=float, default=0.10, help="percentual inicial de agregados (<1)"
    )
    parser.add_argument(
        "--pf", type=float, default=0.50, help="percentual final de agregados (<1)"
    )
    parser.add_argument(
        "--step", type=int, default=2, help="variacao de cada percentual"
    )
    parser.add_argument(
        "--gran", type=int, default=0, help="curva granulometrica de inicio"
    )
    parser.add_argument(
        "--term", action="store_true", help="pos processamento termico"
    )
    parser.add_argument(
        "--mec", action="store_true", help="pos processamento mecanico"
    )

    args = parser.parse_args()

    if (not args.term) and (not args.mec):
        if args.p0 < 1:
            p0 = int(args.p0 * 100)
        else:
            p0 = int(args.p0)

        if args.pf < 1:
            pf = int(args.pf * 100)
        else:
            pf = int(args.pf)

        step_percent = args.step

        curva_gan = args.gran

        set = (x * 0.01 for x in range(p0, pf, step_percent))

        signal.signal(signal.SIGINT, signal_handler)
        th = threading.Thread(target=bg_thread(set, curva_gan))
        th.start()
        th.join()

        if os.path.exists('termico-mecanico'):
            shutil.rmtree('termico-mecanico')

        gera_script('geraScriptTermico')
        gera_script('geraScriptMec')

    elif args.term:
        print("termico")


if __name__ == "__main__":
    main()
