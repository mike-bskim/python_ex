"""
Section 1
Multithreading - Thread(5) - Prod and Cons Using Queue
Keyword - 생산자 소비자 패턴(Producer/Consumer Pattern)

"""
"""

Producer-Consumer Pattern
(1).멀티스레드 디자인 패턴의 정석
(2).서버측 프로그래밍의 핵심
(3).주로 허리역할 중요

Python Event 객체
(1). Flag 초기값(0)
(2). Set() -> 1, Clear() -> 0, Wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래그 상태

"""

import concurrent.futures
import logging
import queue
import random
import threading
import time

# 생산자
def producer(queue, event):
    '''
    네트워크 대기 상태라 가정(서버)
    '''
    while not event.is_set():
        message = random.randint(1,101)
        logging.info('Producer got message: {}'.format(message))
        queue.put(message)

    logging.info('Producer received event Exiting')


# 소비자
def consumer(queue, event):
    '''
    응답 받고 소비하는 것으로 가정 or DB 저장
    '''
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            'Consumer storing message: {}, (size={})'.format( message, queue.qsize())
        )
    logging.info('Consumer received enent Exiting')


if __name__=='__main__':
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 사이즈 중요
    pipeline = queue.Queue(maxsize=100)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    # With context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event) # (self, fn, *args, **kwargs): 함수, 데이터공유(큐), 이벤트
        # 기존에는 메소드1개, 각 스레드에서 메소드를 코드 영역에서 공유함.
        # 지금은 스레드(생산자), 스레드(소비자), 각각 실행, 통신은 큐를 이용해서 통신함.
        executor.submit(consumer, pipeline, event) # (self, fn, *args, **kwargs): 함수, 데이터공유(큐), 이벤트

        # 실행 시간 조정
        time.sleep(0.1)

        logging.info('Main : about to set event')

        #프로그램 종료
        print('before set():', event.is_set())
        event.set()
        print('after set():', event.is_set())







