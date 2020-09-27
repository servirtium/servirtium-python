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
Date: Sun, 27 Sep 2020 15:08:07 GMT
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
Date: Sun, 27 Sep 2020 15:08:08 GMT
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
[{"uid":"94817d1d-a25f-49ee-bf4b-30088b27f2e6","title":"blah","order":523,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/94817d1d-a25f-49ee-bf4b-30088b27f2e6","url":"https://todo-backend-sinatra.herokuapp.com/todos/94817d1d-a25f-49ee-bf4b-30088b27f2e6"},{"uid":"3975a4cc-42df-4b35-8de0-f779c0c3c2b3","title":"blah","order":95,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/3975a4cc-42df-4b35-8de0-f779c0c3c2b3","url":"https://todo-backend-sinatra.herokuapp.com/todos/3975a4cc-42df-4b35-8de0-f779c0c3c2b3"},{"uid":"62416764-259d-4a2c-a4b6-f010688b3d35","title":"blah","order":95,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/62416764-259d-4a2c-a4b6-f010688b3d35","url":"https://todo-backend-sinatra.herokuapp.com/todos/62416764-259d-4a2c-a4b6-f010688b3d35"}]
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
b'{"title":"a todo"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:09 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/57593742-a643-4f21-8cad-f0a3804337c6
Content-Length: 270
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"a todo","uid":"57593742-a643-4f21-8cad-f0a3804337c6","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/57593742-a643-4f21-8cad-f0a3804337c6","url":"https://todo-backend-sinatra.herokuapp.com/todos/57593742-a643-4f21-8cad-f0a3804337c6"}
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
Date: Sun, 27 Sep 2020 15:08:09 GMT
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
Date: Sun, 27 Sep 2020 15:08:09 GMT
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
Date: Sun, 27 Sep 2020 15:08:09 GMT
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
Date: Sun, 27 Sep 2020 15:08:10 GMT
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
b'{"title":"walk the dog"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:11 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/13441c20-51af-4a85-a87b-be5c3200fedb
Content-Length: 276
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"walk the dog","uid":"13441c20-51af-4a85-a87b-be5c3200fedb","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/13441c20-51af-4a85-a87b-be5c3200fedb","url":"https://todo-backend-sinatra.herokuapp.com/todos/13441c20-51af-4a85-a87b-be5c3200fedb"}
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
Date: Sun, 27 Sep 2020 15:08:11 GMT
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
[{"uid":"13441c20-51af-4a85-a87b-be5c3200fedb","title":"walk the dog","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/13441c20-51af-4a85-a87b-be5c3200fedb","url":"https://todo-backend-sinatra.herokuapp.com/todos/13441c20-51af-4a85-a87b-be5c3200fedb"}]
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
Date: Sun, 27 Sep 2020 15:08:12 GMT
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
b'{"title":"blah"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:12 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/e7a8c861-25be-436e-a033-1fe61fd14954
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"blah","uid":"e7a8c861-25be-436e-a033-1fe61fd14954","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/e7a8c861-25be-436e-a033-1fe61fd14954","url":"https://todo-backend-sinatra.herokuapp.com/todos/e7a8c861-25be-436e-a033-1fe61fd14954"}
```

## Interaction 11: OPTIONS /todos

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
Date: Sun, 27 Sep 2020 15:08:13 GMT
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

## Interaction 12: GET /todos

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
Date: Sun, 27 Sep 2020 15:08:13 GMT
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
[{"uid":"e7a8c861-25be-436e-a033-1fe61fd14954","title":"blah","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/e7a8c861-25be-436e-a033-1fe61fd14954","url":"https://todo-backend-sinatra.herokuapp.com/todos/e7a8c861-25be-436e-a033-1fe61fd14954"}]
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
Date: Sun, 27 Sep 2020 15:08:14 GMT
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
b'{"title":"blah"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:14 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/f1a70b7b-41cd-44e1-a3d0-883fb8638960
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"blah","uid":"f1a70b7b-41cd-44e1-a3d0-883fb8638960","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/f1a70b7b-41cd-44e1-a3d0-883fb8638960","url":"https://todo-backend-sinatra.herokuapp.com/todos/f1a70b7b-41cd-44e1-a3d0-883fb8638960"}
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
Date: Sun, 27 Sep 2020 15:08:15 GMT
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
[{"uid":"f1a70b7b-41cd-44e1-a3d0-883fb8638960","title":"blah","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/f1a70b7b-41cd-44e1-a3d0-883fb8638960","url":"https://todo-backend-sinatra.herokuapp.com/todos/f1a70b7b-41cd-44e1-a3d0-883fb8638960"}]
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
Date: Sun, 27 Sep 2020 15:08:16 GMT
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
b'{"title":"my todo"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:16 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/db867920-b188-4c3e-9b15-eb2017d5c1aa
Content-Length: 271
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"my todo","uid":"db867920-b188-4c3e-9b15-eb2017d5c1aa","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/db867920-b188-4c3e-9b15-eb2017d5c1aa","url":"https://todo-backend-sinatra.herokuapp.com/todos/db867920-b188-4c3e-9b15-eb2017d5c1aa"}
```

## Interaction 18: OPTIONS /todos/db867920-b188-4c3e-9b15-eb2017d5c1aa

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
Date: Sun, 27 Sep 2020 15:08:17 GMT
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

## Interaction 19: GET /todos/db867920-b188-4c3e-9b15-eb2017d5c1aa

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
Date: Sun, 27 Sep 2020 15:08:17 GMT
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
{"uid":"db867920-b188-4c3e-9b15-eb2017d5c1aa","title":"my todo","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/db867920-b188-4c3e-9b15-eb2017d5c1aa","url":"https://todo-backend-sinatra.herokuapp.com/todos/db867920-b188-4c3e-9b15-eb2017d5c1aa"}
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
Date: Sun, 27 Sep 2020 15:08:17 GMT
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
b'{"title":"todo the first"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:18 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/fac683eb-ac9b-4476-8ea7-88bbf656a878
Content-Length: 278
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"todo the first","uid":"fac683eb-ac9b-4476-8ea7-88bbf656a878","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/fac683eb-ac9b-4476-8ea7-88bbf656a878","url":"https://todo-backend-sinatra.herokuapp.com/todos/fac683eb-ac9b-4476-8ea7-88bbf656a878"}
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
b'{"title":"todo the second"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:18 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/469d9a66-180d-409c-b857-a788a875ac56
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"todo the second","uid":"469d9a66-180d-409c-b857-a788a875ac56","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/469d9a66-180d-409c-b857-a788a875ac56","url":"https://todo-backend-sinatra.herokuapp.com/todos/469d9a66-180d-409c-b857-a788a875ac56"}
```

## Interaction 23: OPTIONS /todos

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
Date: Sun, 27 Sep 2020 15:08:20 GMT
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

## Interaction 24: GET /todos

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
Date: Sun, 27 Sep 2020 15:08:20 GMT
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
[{"uid":"fac683eb-ac9b-4476-8ea7-88bbf656a878","title":"todo the first","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/fac683eb-ac9b-4476-8ea7-88bbf656a878","url":"https://todo-backend-sinatra.herokuapp.com/todos/fac683eb-ac9b-4476-8ea7-88bbf656a878"},{"uid":"469d9a66-180d-409c-b857-a788a875ac56","title":"todo the second","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/469d9a66-180d-409c-b857-a788a875ac56","url":"https://todo-backend-sinatra.herokuapp.com/todos/469d9a66-180d-409c-b857-a788a875ac56"}]
```

## Interaction 25: OPTIONS /todos/fac683eb-ac9b-4476-8ea7-88bbf656a878

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
Date: Sun, 27 Sep 2020 15:08:20 GMT
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

## Interaction 26: GET /todos/fac683eb-ac9b-4476-8ea7-88bbf656a878

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
Date: Sun, 27 Sep 2020 15:08:21 GMT
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
{"uid":"fac683eb-ac9b-4476-8ea7-88bbf656a878","title":"todo the first","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/fac683eb-ac9b-4476-8ea7-88bbf656a878","url":"https://todo-backend-sinatra.herokuapp.com/todos/fac683eb-ac9b-4476-8ea7-88bbf656a878"}
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
Date: Sun, 27 Sep 2020 15:08:22 GMT
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
b'{"title":"initial title"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:22 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/93f01ae1-d42d-4b97-a37d-f40269e4caf1
Content-Length: 277
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"initial title","uid":"93f01ae1-d42d-4b97-a37d-f40269e4caf1","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/93f01ae1-d42d-4b97-a37d-f40269e4caf1","url":"https://todo-backend-sinatra.herokuapp.com/todos/93f01ae1-d42d-4b97-a37d-f40269e4caf1"}
```

## Interaction 29: OPTIONS /todos/93f01ae1-d42d-4b97-a37d-f40269e4caf1

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
Date: Sun, 27 Sep 2020 15:08:22 GMT
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

## Interaction 30: PATCH /todos/93f01ae1-d42d-4b97-a37d-f40269e4caf1

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
b'{"title":"bathe the cat"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:23 GMT
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
{"uid":"93f01ae1-d42d-4b97-a37d-f40269e4caf1","title":"bathe the cat","order":0,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/93f01ae1-d42d-4b97-a37d-f40269e4caf1","url":"https://todo-backend-sinatra.herokuapp.com/todos/93f01ae1-d42d-4b97-a37d-f40269e4caf1"}
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
Date: Sun, 27 Sep 2020 15:08:23 GMT
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
b'{"title":"blah"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:24 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/7f00b9b9-e4ab-4c6a-8c01-8cf084f37190
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"blah","uid":"7f00b9b9-e4ab-4c6a-8c01-8cf084f37190","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/7f00b9b9-e4ab-4c6a-8c01-8cf084f37190","url":"https://todo-backend-sinatra.herokuapp.com/todos/7f00b9b9-e4ab-4c6a-8c01-8cf084f37190"}
```

## Interaction 33: OPTIONS /todos/7f00b9b9-e4ab-4c6a-8c01-8cf084f37190

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
Date: Sun, 27 Sep 2020 15:08:25 GMT
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

## Interaction 34: PATCH /todos/7f00b9b9-e4ab-4c6a-8c01-8cf084f37190

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
b'{"completed":true}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:25 GMT
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
{"uid":"7f00b9b9-e4ab-4c6a-8c01-8cf084f37190","title":"blah","order":0,"completed":true,"href":"https://todo-backend-sinatra.herokuapp.com/todos/7f00b9b9-e4ab-4c6a-8c01-8cf084f37190","url":"https://todo-backend-sinatra.herokuapp.com/todos/7f00b9b9-e4ab-4c6a-8c01-8cf084f37190"}
```

## Interaction 35: OPTIONS /todos

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
Date: Sun, 27 Sep 2020 15:08:26 GMT
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

## Interaction 36: DELETE /todos

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
Date: Sun, 27 Sep 2020 15:08:27 GMT
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

## Interaction 37: POST /todos

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
b'{"title":"blah"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:27 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"blah","uid":"8ecc0749-9f99-486e-b99e-fee695abe8cb","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb","url":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb"}
```

## Interaction 38: OPTIONS /todos/8ecc0749-9f99-486e-b99e-fee695abe8cb

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
Date: Sun, 27 Sep 2020 15:08:28 GMT
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

## Interaction 39: PATCH /todos/8ecc0749-9f99-486e-b99e-fee695abe8cb

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
b'{"title":"changed title","completed":true}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:29 GMT
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
{"uid":"8ecc0749-9f99-486e-b99e-fee695abe8cb","title":"changed title","order":0,"completed":true,"href":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb","url":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb"}
```

## Interaction 40: GET /todos/8ecc0749-9f99-486e-b99e-fee695abe8cb

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
Date: Sun, 27 Sep 2020 15:08:30 GMT
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
{"uid":"8ecc0749-9f99-486e-b99e-fee695abe8cb","title":"changed title","order":0,"completed":true,"href":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb","url":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb"}
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
Date: Sun, 27 Sep 2020 15:08:30 GMT
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
[{"uid":"8ecc0749-9f99-486e-b99e-fee695abe8cb","title":"changed title","order":0,"completed":true,"href":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb","url":"https://todo-backend-sinatra.herokuapp.com/todos/8ecc0749-9f99-486e-b99e-fee695abe8cb"}]
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
Date: Sun, 27 Sep 2020 15:08:31 GMT
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

## Interaction 43: OPTIONS /todos

### Request headers recorded for playback:

```
Host: todo-backend-sinatra.herokuapp.com
Connection: keep-alive
Accept: */*
Access-Control-Request-Method: POST
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
Date: Sun, 27 Sep 2020 15:08:32 GMT
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

## Interaction 44: POST /todos

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
b'{"title":"blah"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:33 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/449aeee7-0233-4515-84e4-43a921134d90
Content-Length: 268
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"blah","uid":"449aeee7-0233-4515-84e4-43a921134d90","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/449aeee7-0233-4515-84e4-43a921134d90","url":"https://todo-backend-sinatra.herokuapp.com/todos/449aeee7-0233-4515-84e4-43a921134d90"}
```

## Interaction 45: OPTIONS /todos/449aeee7-0233-4515-84e4-43a921134d90

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
Date: Sun, 27 Sep 2020 15:08:33 GMT
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

## Interaction 46: DELETE /todos/449aeee7-0233-4515-84e4-43a921134d90

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
Date: Sun, 27 Sep 2020 15:08:34 GMT
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

## Interaction 47: GET /todos

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
Date: Sun, 27 Sep 2020 15:08:35 GMT
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

## Interaction 48: POST /todos

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
b'{"title":"blah","order":523}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:35 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/6b7aea57-8b69-4cbf-b87b-ae5455677cca
Content-Length: 280
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"title":"blah","order":523,"uid":"6b7aea57-8b69-4cbf-b87b-ae5455677cca","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/6b7aea57-8b69-4cbf-b87b-ae5455677cca","url":"https://todo-backend-sinatra.herokuapp.com/todos/6b7aea57-8b69-4cbf-b87b-ae5455677cca"}
```

## Interaction 49: POST /todos

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
b'{"order":10,"title":"blah"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:36 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/4df6a23d-56b4-486f-bf0f-e112cdf1cf1d
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"order":10,"title":"blah","uid":"4df6a23d-56b4-486f-bf0f-e112cdf1cf1d","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/4df6a23d-56b4-486f-bf0f-e112cdf1cf1d","url":"https://todo-backend-sinatra.herokuapp.com/todos/4df6a23d-56b4-486f-bf0f-e112cdf1cf1d"}
```

## Interaction 50: OPTIONS /todos/4df6a23d-56b4-486f-bf0f-e112cdf1cf1d

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
Date: Sun, 27 Sep 2020 15:08:36 GMT
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

## Interaction 51: PATCH /todos/4df6a23d-56b4-486f-bf0f-e112cdf1cf1d

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
b'{"order":95}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:37 GMT
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
{"uid":"4df6a23d-56b4-486f-bf0f-e112cdf1cf1d","title":"blah","order":95,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/4df6a23d-56b4-486f-bf0f-e112cdf1cf1d","url":"https://todo-backend-sinatra.herokuapp.com/todos/4df6a23d-56b4-486f-bf0f-e112cdf1cf1d"}
```

## Interaction 52: POST /todos

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
b'{"order":10,"title":"blah"}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:38 GMT
Connection: keep-alive
Content-Type: text/html;charset=utf-8
Access-Control-Allow-Origin: *
Location: https://todo-backend-sinatra.herokuapp.com/todos/1341a52c-6777-4c00-a864-5a53d1a89876
Content-Length: 279
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Server: thin 1.6.2 codename Doc Brown
Via: 1.1 vegur
```

### Response body recorded for playback (201: text/html;charset=utf-8):

```
{"order":10,"title":"blah","uid":"1341a52c-6777-4c00-a864-5a53d1a89876","completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/1341a52c-6777-4c00-a864-5a53d1a89876","url":"https://todo-backend-sinatra.herokuapp.com/todos/1341a52c-6777-4c00-a864-5a53d1a89876"}
```

## Interaction 53: OPTIONS /todos/1341a52c-6777-4c00-a864-5a53d1a89876

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
Date: Sun, 27 Sep 2020 15:08:38 GMT
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

## Interaction 54: PATCH /todos/1341a52c-6777-4c00-a864-5a53d1a89876

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
b'{"order":95}'
```

### Response headers recorded for playback:

```
Date: Sun, 27 Sep 2020 15:08:38 GMT
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
{"uid":"1341a52c-6777-4c00-a864-5a53d1a89876","title":"blah","order":95,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/1341a52c-6777-4c00-a864-5a53d1a89876","url":"https://todo-backend-sinatra.herokuapp.com/todos/1341a52c-6777-4c00-a864-5a53d1a89876"}
```

## Interaction 55: GET /todos/1341a52c-6777-4c00-a864-5a53d1a89876

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
Date: Sun, 27 Sep 2020 15:08:39 GMT
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
{"uid":"1341a52c-6777-4c00-a864-5a53d1a89876","title":"blah","order":95,"completed":false,"href":"https://todo-backend-sinatra.herokuapp.com/todos/1341a52c-6777-4c00-a864-5a53d1a89876","url":"https://todo-backend-sinatra.herokuapp.com/todos/1341a52c-6777-4c00-a864-5a53d1a89876"}
```
