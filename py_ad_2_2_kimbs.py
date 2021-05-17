"""
Section 2
Parallelism with Multiprocessing - multiprocessing(1) - Join, is_alive

Keyword - multiprocessing, processing state

"""
from multiprocessing import Process
import time
import logging

# 프로세스 실행 함수
def proc_func(name):
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Sub-Process {}: starting".format(name))
    logging.info("Sub-Process {}: starting".format(name))
    time.sleep(3)
    logging.info("Sub-Process {}: finishing".format(name))
    logging.info("Sub-Process {}: ending".format(name))


def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    

    # 함수 인자 확인
    p = Process(target=proc_func, args=('First',))

    logging.info("Main-Process : before creating Process")
    # 프로세스 시작
    p.start()

    logging.info("Main-Process : During Process")

    # 프로세서 강제 종료 명령어
    logging.info("Main-Process : Terminated Process")
    p.terminate()

    logging.info("Main-Process : Joined Process")
    # p.join()

    # 프로세스 상태 확인
    logging.info(f'Process p is alive: {p.is_alive()}')

# 메인 시작
if __name__ == '__main__':
    main()