import os
import sys
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
import servirtium.recorder as MockRecorder
import servirtium.playback as MockPlaybacker

ruby_process = None
todoSuiteUrl = "https://servirtium.github.io/compatibility-suite/index.html"

if len(sys.argv) > 1:
   if sys.argv[1] == "record":

       # TODO check that ruby process is already started.
       url = "http://localhost:61417"
       MockRecorder.set_mocks_dir(os.getcwd())
       MockRecorder.pretty_print_json_or_xml()
       MockRecorder.set_markdown_filename("todobackend_test_suite")
       MockRecorder.set_real_service("https://todo-backend-sinatra.herokuapp.com")
       servirtium_daemon = threading.Thread(target=MockRecorder.start, daemon=True)
       servirtium_daemon.start()
   elif sys.argv[1] == "playback":

       url = "http://localhost:61417"
       MockRecorder.set_mocks_dir(os.getcwd())
       MockPlaybacker.set_markdown_filename("todobackend_test_suite")
       servirtium_daemon = threading.Thread(target=MockPlaybacker.start, daemon=True)
       servirtium_daemon.start()
   elif sys.argv[1] == "direct":
       print("showing reference Sinatra app online without Servirtium in the middle")
       todoSuiteUrl = "https://www.todobackend.com/specs/index.html"
       url = "https://todo-backend-sinatra.herokuapp.com"
   else:
       print("Second arg should be record, playback or direct")
       exit(10)
else:
   print("record/playback/direct argument needed")
   exit(10)

if len(sys.argv) > 2:
   if sys.argv[2] == "local":
       # Running via 'python -m SimpleHTTPServer 8000' in a different shell
       todoSuiteUrl = "http://localhost:8000/index.html"

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

time.sleep(5) # for old workstations

driver.get(todoSuiteUrl + "?" + url + "/todos")
try:
    element = WebDriverWait(driver, 300).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "passes"), "16")
    )
    print("Compatibility suite: all 16 tests passed")

except TimeoutException as ex:
    print("Compatibility suite: did not finish with 16 passes. See open browser frame.")

# TODO warn that node process was not started.

print("mode: " + sys.argv[1])

print("Closing Selenium")
driver.quit()
print("All done.")
