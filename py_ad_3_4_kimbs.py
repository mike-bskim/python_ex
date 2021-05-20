"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(1) - Synchronous

Keyword - I/O Bound, requests

"""
# I/O-Bound Sync 예제(https://realpython.com/python-concurrency/#synchronous-version)

# pip install requests
import requests
import time

# function1 (download)
def request_site(url, session):
    # checking session
    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        print(f"[Read contents: {len(response.content)}, Status code: {response.status_code} from {url}")


# function2
def request_all_site(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)


def main():

    # URLS for test
    urls = [
            "https://www.jython.org",
            "https://www.naver.com",
            "https://realpython.com/"
    ] * 3

    start_time = time.time()

    request_all_site(urls)

    duration = time.time() - start_time

    print()

    print(f"Download {len(urls)} sites in {duration} seconds")



if __name__=='__main__':
    main()