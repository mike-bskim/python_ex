"""
Section 2
Parallelism with Multiprocessing - Multiprocessing(3) - ProcessPoolExecutor

Keyword - ProcessPoolExecutor, as_completed, futures, timeout, dict

"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URLS
URLS =  [
        'https://www.daum.net/',
        'http://www.cnn.com/',
        'https://naver.com/',
        'http://www.bbc.co.uk/',
        'http://ruliweb.com'
        ]
# URLS = ['https://www.daum.net/',
#         'http://www.cnn.com/',
#         'http://europe.wsj.com/',
#         'http://www.bbc.co.uk/',
#         'http://some-made-up-domain.com/']

# 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    # 프로세스풀 context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

    print(future_to_url)

    # 실행
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('{} generated an exception: {}'.format(url, exec))
        else:
            print('{} page is {} bytes'.format(url, len(data)))


if __name__ == '__main__':
    main()    