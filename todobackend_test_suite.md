## Interaction 0: OPTIONS /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: GET
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:01:57 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,HEAD,POST,DELETE,OPTIONS,PUT
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 1: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos the pre-requisites the api root responds to a GET (i.e. the server is up and accessible, CORS headers are set up)
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:01:57 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 842
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[
  {
    "uid": "447b52f3-4989-43a9-acd2-e3c030888da5",
    "title": "blah",
    "order": 523,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/447b52f3-4989-43a9-acd2-e3c030888da5",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/447b52f3-4989-43a9-acd2-e3c030888da5"
  },
  {
    "uid": "120218fc-9067-46d4-aa7b-678ff1d7d097",
    "title": "blah",
    "order": 95,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/120218fc-9067-46d4-aa7b-678ff1d7d097",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/120218fc-9067-46d4-aa7b-678ff1d7d097"
  },
  {
    "uid": "57524d1f-093f-431c-8cb5-addd8182c95d",
    "title": "blah",
    "order": 95,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/57524d1f-093f-431c-8cb5-addd8182c95d",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/57524d1f-093f-431c-8cb5-addd8182c95d"
  }
]
```
## Interaction 2: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 18
fullTitle: Todo-Backend API residing at http://localhost:61417/todos the pre-requisites the api root responds to a POST with the todo which was posted to it
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "a todo"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:01:58 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/10926974-3321-4a39-b514-d80d2fc0cca1
Content-Length: 270
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "a todo",
  "uid": "10926974-3321-4a39-b514-d80d2fc0cca1",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/10926974-3321-4a39-b514-d80d2fc0cca1",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/10926974-3321-4a39-b514-d80d2fc0cca1"
}
```
## Interaction 3: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos the pre-requisites the api root responds successfully to a DELETE
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:01:58 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 4: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos the pre-requisites after a DELETE the api root responds to a GET with a JSON representation of an empty array
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:00 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 5: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos the pre-requisites after a DELETE the api root responds to a GET with a JSON representation of an empty array
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:01:59 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 2
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[]
```
## Interaction 6: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos the pre-requisites after a DELETE the api root responds to a GET with a JSON representation of an empty array
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:00 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 7: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 24
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url adds a new todo to the list of todos at the root url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "walk the dog"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:00 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/551e6a53-32c3-4804-a84b-3bcd8a7abe22
Content-Length: 276
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "walk the dog",
  "uid": "551e6a53-32c3-4804-a84b-3bcd8a7abe22",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/551e6a53-32c3-4804-a84b-3bcd8a7abe22",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/551e6a53-32c3-4804-a84b-3bcd8a7abe22"
}
```
## Interaction 8: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url adds a new todo to the list of todos at the root url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:01 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 288
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[
  {
    "uid": "551e6a53-32c3-4804-a84b-3bcd8a7abe22",
    "title": "walk the dog",
    "order": 0,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/551e6a53-32c3-4804-a84b-3bcd8a7abe22",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/551e6a53-32c3-4804-a84b-3bcd8a7abe22"
  }
]
```
## Interaction 9: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url adds a new todo to the list of todos at the root url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:01 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 10: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 16
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url sets up a new todo as initially not completed
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "blah"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:02 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/db2db966-21ea-4e80-89af-8ccc2fd22358
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "blah",
  "uid": "db2db966-21ea-4e80-89af-8ccc2fd22358",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/db2db966-21ea-4e80-89af-8ccc2fd22358",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/db2db966-21ea-4e80-89af-8ccc2fd22358"
}
```
## Interaction 11: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url sets up a new todo as initially not completed
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:03 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 280
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[
  {
    "uid": "db2db966-21ea-4e80-89af-8ccc2fd22358",
    "title": "blah",
    "order": 0,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/db2db966-21ea-4e80-89af-8ccc2fd22358",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/db2db966-21ea-4e80-89af-8ccc2fd22358"
  }
]
```
## Interaction 12: OPTIONS /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:02 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,HEAD,POST,DELETE,OPTIONS,PUT
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 13: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url sets up a new todo as initially not completed
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:03 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 14: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 16
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url each new todo has a url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "blah"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:04 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/9c77d1fd-4dba-495f-97c2-de15015bd165
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "blah",
  "uid": "9c77d1fd-4dba-495f-97c2-de15015bd165",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/9c77d1fd-4dba-495f-97c2-de15015bd165",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/9c77d1fd-4dba-495f-97c2-de15015bd165"
}
```
## Interaction 15: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url each new todo has a url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:04 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 280
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[
  {
    "uid": "9c77d1fd-4dba-495f-97c2-de15015bd165",
    "title": "blah",
    "order": 0,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/9c77d1fd-4dba-495f-97c2-de15015bd165",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/9c77d1fd-4dba-495f-97c2-de15015bd165"
  }
]
```
## Interaction 16: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url each new todo has a url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:04 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 17: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 19
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url each new todo has a url, which returns a todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "my todo"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:05 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/e38f40e7-74c2-4840-be87-50cca4e02dce
Content-Length: 271
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "my todo",
  "uid": "e38f40e7-74c2-4840-be87-50cca4e02dce",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/e38f40e7-74c2-4840-be87-50cca4e02dce",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/e38f40e7-74c2-4840-be87-50cca4e02dce"
}
```
## Interaction 18: OPTIONS /todos/e38f40e7-74c2-4840-be87-50cca4e02dce

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: GET
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:06 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 19: GET /todos/e38f40e7-74c2-4840-be87-50cca4e02dce

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url each new todo has a url, which returns a todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:06 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 281
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "e38f40e7-74c2-4840-be87-50cca4e02dce",
  "title": "my todo",
  "order": 0,
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/e38f40e7-74c2-4840-be87-50cca4e02dce",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/e38f40e7-74c2-4840-be87-50cca4e02dce"
}
```
## Interaction 20: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos storing new todos by posting to the root url each new todo has a url, which returns a todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:07 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 21: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 26
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can navigate from a list of todos to an individual todo via urls
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "todo the first"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:07 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/76d0bc2b-f212-45d4-acdf-c6a9271564af
Content-Length: 278
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "todo the first",
  "uid": "76d0bc2b-f212-45d4-acdf-c6a9271564af",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/76d0bc2b-f212-45d4-acdf-c6a9271564af",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/76d0bc2b-f212-45d4-acdf-c6a9271564af"
}
```
## Interaction 22: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 27
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can navigate from a list of todos to an individual todo via urls
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "todo the second"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:08 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/2f59fc3d-1716-476c-802f-cc981f21a77d
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "todo the second",
  "uid": "2f59fc3d-1716-476c-802f-cc981f21a77d",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/2f59fc3d-1716-476c-802f-cc981f21a77d",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/2f59fc3d-1716-476c-802f-cc981f21a77d"
}
```
## Interaction 23: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can navigate from a list of todos to an individual todo via urls
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:08 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 580
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[
  {
    "uid": "76d0bc2b-f212-45d4-acdf-c6a9271564af",
    "title": "todo the first",
    "order": 0,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/76d0bc2b-f212-45d4-acdf-c6a9271564af",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/76d0bc2b-f212-45d4-acdf-c6a9271564af"
  },
  {
    "uid": "2f59fc3d-1716-476c-802f-cc981f21a77d",
    "title": "todo the second",
    "order": 0,
    "completed": false,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/2f59fc3d-1716-476c-802f-cc981f21a77d",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/2f59fc3d-1716-476c-802f-cc981f21a77d"
  }
]
```
## Interaction 24: OPTIONS /todos/76d0bc2b-f212-45d4-acdf-c6a9271564af

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: GET
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:08 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 25: GET /todos/76d0bc2b-f212-45d4-acdf-c6a9271564af

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can navigate from a list of todos to an individual todo via urls
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:09 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 288
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "76d0bc2b-f212-45d4-acdf-c6a9271564af",
  "title": "todo the first",
  "order": 0,
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/76d0bc2b-f212-45d4-acdf-c6a9271564af",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/76d0bc2b-f212-45d4-acdf-c6a9271564af"
}
```
## Interaction 26: OPTIONS /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:09 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,HEAD,POST,DELETE,OPTIONS,PUT
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 27: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can navigate from a list of todos to an individual todo via urls
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:10 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 28: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 25
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can change the todo's title by PATCHing to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "initial title"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:10 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/c2cc8d3d-74e3-47d3-9745-5c1afd13de3d
Content-Length: 277
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "initial title",
  "uid": "c2cc8d3d-74e3-47d3-9745-5c1afd13de3d",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/c2cc8d3d-74e3-47d3-9745-5c1afd13de3d",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/c2cc8d3d-74e3-47d3-9745-5c1afd13de3d"
}
```
## Interaction 29: OPTIONS /todos/c2cc8d3d-74e3-47d3-9745-5c1afd13de3d

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: PATCH
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:11 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 30: PATCH /todos/c2cc8d3d-74e3-47d3-9745-5c1afd13de3d

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 25
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can change the todo's title by PATCHing to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "bathe the cat"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:12 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 287
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "c2cc8d3d-74e3-47d3-9745-5c1afd13de3d",
  "title": "bathe the cat",
  "order": 0,
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/c2cc8d3d-74e3-47d3-9745-5c1afd13de3d",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/c2cc8d3d-74e3-47d3-9745-5c1afd13de3d"
}
```
## Interaction 31: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can change the todo's title by PATCHing to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:12 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 32: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 16
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can change the todo's completedness by PATCHing to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "blah"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:12 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/0282ab35-ae44-4f11-994c-2083a1b75c28
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "blah",
  "uid": "0282ab35-ae44-4f11-994c-2083a1b75c28",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/0282ab35-ae44-4f11-994c-2083a1b75c28",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/0282ab35-ae44-4f11-994c-2083a1b75c28"
}
```
## Interaction 33: OPTIONS /todos/0282ab35-ae44-4f11-994c-2083a1b75c28

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: PATCH
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:13 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 34: PATCH /todos/0282ab35-ae44-4f11-994c-2083a1b75c28

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 18
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can change the todo's completedness by PATCHing to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "completed": true
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:13 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 277
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "0282ab35-ae44-4f11-994c-2083a1b75c28",
  "title": "blah",
  "order": 0,
  "completed": true,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/0282ab35-ae44-4f11-994c-2083a1b75c28",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/0282ab35-ae44-4f11-994c-2083a1b75c28"
}
```
## Interaction 35: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can change the todo's completedness by PATCHing to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:14 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 36: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 16
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo changes to a todo are persisted and show up when re-fetching the todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "blah"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:15 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "blah",
  "uid": "a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04"
}
```
## Interaction 37: OPTIONS /todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: PATCH
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:14 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 38: PATCH /todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 42
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo changes to a todo are persisted and show up when re-fetching the todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "changed title",
  "completed": true
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:15 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 286
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
  "title": "changed title",
  "order": 0,
  "completed": true,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04"
}
```
## Interaction 39: GET /todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo changes to a todo are persisted and show up when re-fetching the todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:16 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 286
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
  "title": "changed title",
  "order": 0,
  "completed": true,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04"
}
```
## Interaction 40: OPTIONS /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: GET
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:16 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,HEAD,POST,DELETE,OPTIONS,PUT
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 41: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo changes to a todo are persisted and show up when re-fetching the todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:17 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 288
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[
  {
    "uid": "a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
    "title": "changed title",
    "order": 0,
    "completed": true,
    "href": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04",
    "url": "https://todo-backend-sinatra.herokuapp.com/todos/a0d38b65-1366-4fbd-bf85-0cc8e4e27b04"
  }
]
```
## Interaction 42: DELETE /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo changes to a todo are persisted and show up when re-fetching the todo
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:17 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 43: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 16
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can delete a todo making a DELETE request to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "blah"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:17 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/52c7e68d-927a-4a31-96ee-c8da778acb3a
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "blah",
  "uid": "52c7e68d-927a-4a31-96ee-c8da778acb3a",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/52c7e68d-927a-4a31-96ee-c8da778acb3a",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/52c7e68d-927a-4a31-96ee-c8da778acb3a"
}
```
## Interaction 44: OPTIONS /todos/52c7e68d-927a-4a31-96ee-c8da778acb3a

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:18 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 45: DELETE /todos/52c7e68d-927a-4a31-96ee-c8da778acb3a

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can delete a todo making a DELETE request to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:19 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (204: ):

```

```
## Interaction 46: GET /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos working with an existing todo can delete a todo making a DELETE request to the todo's url
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:19 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 2
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
[]
```
## Interaction 47: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 28
fullTitle: Todo-Backend API residing at http://localhost:61417/todos tracking todo order can create a todo with an order field
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "title": "blah",
  "order": 523
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:19 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/7792550a-a089-45f2-a7ec-407abe3c4010
Content-Length: 280
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "title": "blah",
  "order": 523,
  "uid": "7792550a-a089-45f2-a7ec-407abe3c4010",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/7792550a-a089-45f2-a7ec-407abe3c4010",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/7792550a-a089-45f2-a7ec-407abe3c4010"
}
```
## Interaction 48: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 27
fullTitle: Todo-Backend API residing at http://localhost:61417/todos tracking todo order can PATCH a todo to change its order
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "order": 10,
  "title": "blah"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:20 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/0854800c-9cbc-45a6-9284-bb2be08c8d2e
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "order": 10,
  "title": "blah",
  "uid": "0854800c-9cbc-45a6-9284-bb2be08c8d2e",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/0854800c-9cbc-45a6-9284-bb2be08c8d2e",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/0854800c-9cbc-45a6-9284-bb2be08c8d2e"
}
```
## Interaction 49: OPTIONS /todos/0854800c-9cbc-45a6-9284-bb2be08c8d2e

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: PATCH
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:20 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 50: PATCH /todos/0854800c-9cbc-45a6-9284-bb2be08c8d2e

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 12
fullTitle: Todo-Backend API residing at http://localhost:61417/todos tracking todo order can PATCH a todo to change its order
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "order": 95
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:21 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "0854800c-9cbc-45a6-9284-bb2be08c8d2e",
  "title": "blah",
  "order": 95,
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/0854800c-9cbc-45a6-9284-bb2be08c8d2e",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/0854800c-9cbc-45a6-9284-bb2be08c8d2e"
}
```
## Interaction 51: POST /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 27
fullTitle: Todo-Backend API residing at http://localhost:61417/todos tracking todo order remembers changes to a todo's order
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "order": 10,
  "title": "blah"
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:21 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/7f3b8da5-ad50-4957-b724-0bbd12315561
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{
  "order": 10,
  "title": "blah",
  "uid": "7f3b8da5-ad50-4957-b724-0bbd12315561",
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/7f3b8da5-ad50-4957-b724-0bbd12315561",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/7f3b8da5-ad50-4957-b724-0bbd12315561"
}
```
## Interaction 52: OPTIONS /todos/7f3b8da5-ad50-4957-b724-0bbd12315561

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: PATCH
Access-Control-Request-Headers: content-type,fulltitle
Origin: https://servirtium.github.io
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:22 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: content-type,fulltitle
Access-Control-Allow-Methods: GET,PATCH,HEAD,DELETE,OPTIONS
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
Content-Typeaccess-control-allow-originaccess-control-allow-headersaccess-control-allow-methodsX-XSS-ProtectionX-Content-Type-OptionsX-Frame-Options
```
## Interaction 53: PATCH /todos/7f3b8da5-ad50-4957-b724-0bbd12315561

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Content-Length: 12
fullTitle: Todo-Backend API residing at http://localhost:61417/todos tracking todo order remembers changes to a todo's order
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```
{
  "order": 95
}
```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:23 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "7f3b8da5-ad50-4957-b724-0bbd12315561",
  "title": "blah",
  "order": 95,
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/7f3b8da5-ad50-4957-b724-0bbd12315561",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/7f3b8da5-ad50-4957-b724-0bbd12315561"
}
```
## Interaction 54: GET /todos/7f3b8da5-ad50-4957-b724-0bbd12315561

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
fullTitle: Todo-Backend API residing at http://localhost:61417/todos tracking todo order remembers changes to a todo's order
Accept: text/plain, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Content-Type: application/json
Origin: https://servirtium.github.io
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Thu, 01 Oct 2020 17:02:23 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (200: text/html;charset=utf-8):

```
{
  "uid": "7f3b8da5-ad50-4957-b724-0bbd12315561",
  "title": "blah",
  "order": 95,
  "completed": false,
  "href": "https://todo-backend-sinatra.herokuapp.com/todos/7f3b8da5-ad50-4957-b724-0bbd12315561",
  "url": "https://todo-backend-sinatra.herokuapp.com/todos/7f3b8da5-ad50-4957-b724-0bbd12315561"
}
```
