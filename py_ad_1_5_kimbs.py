"""
Section 1
Multithreading - Thread(3) - ThreadPoolExecutor
Keyword - Many Threads, concurrent.futures, (xxx)PoolExcutor
"""

"""
그룹스레드
(1).Python 3.2 이상 표준 라이브러리 사용
(2).concurrent.futures
(3).with사용으로 생성, 소멸 라이프사이클 관리 용이
(4).디버깅하기가 난해함(단점)
(5).대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화(캡슐화)
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name, n):
    logging.info('***Sub-Thread %s: starting', name)

    result = 0
    for i in range(n):
        result += i

    logging.info('***Sub-Thread %s: finished result: %d', name, result)

    return result


def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info('Main-Thread : before creating and running thread')

    # # 실행방법1
    # # amx_workers : 작업의 개수가 넘어가면 직접 설정이 유리
    # excutor = ThreadPoolExecutor(max_workers=3)
    # task1 = excutor.submit(task, ('First',))
    # task2 = excutor.submit(task, ('Second',))
    # # task3 = excutor.submit(task, ('Third',))

    # # 결과값이 있을 경우
    # print('task1:', task1.result())
    # print('task2:', task2.result())

    '''
    executor.map(func, args)에서 
    func의 인자(arguments)가 2개 이상일때에는 다음과 같이 구성하면 결과값 추출이 가능합니다.
    args  = (('first', 10001), ('second', 10001))
    for result in executor.map(lambda args : func(*args), args):
        print(result)
    '''
    # 실행방법2
    args  = (('first', 10001), ('second', 10001), ('third', 10001))
    with ThreadPoolExecutor(max_workers=3) as executor:
        # tasks = executor.map(task, ['First',Second,'Third']) # 인자가 1개일 경우
        tasks = executor.map(lambda args : task(*args), args) # 인자가 2개 이상일 경우
        # 결과확인
        print(list(tasks))

    
    logging.info('Main-Thread : main is done')


if __name__=='__main__':
    main()