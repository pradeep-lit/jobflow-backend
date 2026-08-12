Request and response
Request is a way to ask a server to do some work or to ask something with your question (query). Response is the answer or data sends back upon a request when done 
HTTP method

There different types of HTTP methods and they have their purpose, Like GET to get the response (data) of the query, POST to set something to the server or db, PUT to change the something changable, and DELETE to delete the data or record
URL
Uniform resource locator is the unique address used to find a webpage, file or resource from the internet/local
Headers
HTTP Headers are very important to provide some authorization for APIs, Headers are like User Agents (for device fingerprinting), Referrer (to check which domain/url redirected to the current API or page), etc. Header pretty much tells the device identity, where it came from, what data the requester (client) expecting.
Path parameters
These parameter are like filesystem in an os, Suppose we have to have to access a specific resource under a folder. Its written as https://leetcode.com/u/pradeep-lit here pradeep-lit is a path paramter.

Query parameters

Query parameters is a different way to specify a parameter. Here we use `?` and `&` to specify parameter. These are written in key=value pair. Example: ?u=8&query=Who%20Am%20I, The value should URL-encoded.
Request body
Request body are generally used to request apis, body are written in json which could specify parameter, so that server does the operation on those. 
Status codes
response Status codes tells the status of the query we made in request was successfully completed. Like 429 Means rate-limited for a certain duration, 200 Means Everything was OK, 401 Means Unauthorized, 403 Means Forbidden, Responses are grouped in five classes:

Informational responses (100 – 199)
Successful responses (200 – 299)
Redirection messages (300 – 399)
Client error responses (400 – 499)
Server error responses (500 – 599)
Statelessness

An API with no context of the user stored in API Server. It ideally works with Authorization header, like some cryptography like jwt.
Idempotency
Idempotent means we get the same result after doing a task multiple times as we did it once. In APIs there much idempotency HTTP methods like GET, DELETE, PUT. POST and PATCH can be non-idempotent

In /jobs/42?include_company=true, which value is a path parameter and which is a query parameter?
42 is the path value and true is the query value
When should an API return 201 Created instead of 200 OK?
201 comes in POST ig, which tells us creation was sucessfull
Why is GET expected to be safe and idempotent?
Because, It doesnt modify any data and idempotent because wont effect anything on the server, and result would be same until something is changed in server
What is the difference between 401 Unauthorized and 403 Forbidden?
Unauthorized mean that we are not allowed to do the operation with the current credential, token, or session. Forbidden comes usually when something is geo-blocked or user-blocked
What does it mean when an HTTP API is stateless?
When API server doesnt save the context or session. Works by mathematical computation.