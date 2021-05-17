"""
Section 2
Parallelism with Multiprocessing - multiprocessing(1) - Join, is_alive

Keyword - multiprocessing, processing state

"""
import time
import logging
from multiprocessing import Process


def proc_func(name):
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info('Sub-process : {} starting'.format(name))
    time.sleep(3)
    logging.info('Sub-process : {} ending'.format(name))


def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 함수 인자 확인
    p = Process(target=proc_func, args=('First', ))

    logging.info('Main-process : before creating Process')
    # 프로세스 시작
    p.start()

    logging.info('Main-process : During Process')

    # 프로레스 강제 종료 명령어
    # logging.info('Main-process : Terminated Process')
    # p.terminate()

    logging.info('Main-process : Joined Process')
    p.join()

    # 프로세스 상태 확인
    logging.info(f"Process P is alive: {p.is_alive()}")



if __name__=='__main__':
    main()