import os
import sys
import threading

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