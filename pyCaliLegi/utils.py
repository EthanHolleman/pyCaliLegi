import time

def press_submit(submitable, wait=1):
    time.sleep(wait)
    submitable.submit()
    time.sleep(wait)