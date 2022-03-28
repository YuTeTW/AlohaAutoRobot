import time

from function import driver, url, click_by_id, By

def start():
    driver.get(url)
    driver.execute_script("document.body.style.zoom='0.5'")

    time_end = time.time() + 5
    while True:
        try:
            click_by_id("actionLine_create")
        except Exception as e:
            break
        # if time_end < time.time():
        #     break
