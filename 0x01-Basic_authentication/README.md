# Basic Authentication 
Basic authentication in Python is a simple and common method of implementing authentication for web APIs.

## Description
It involves including the username and password in the "Authorization" header of an HTTP request, encoded in a simple way using Base64. The requests package in Python provides an easy way to use basic authentication with the auth keyword argument. While it is a simple and common authentication method for web APIs, it's important to consider the security implications and explore more secure authentication mechanisms for production systems. Here's an example of how to use basic authentication with the requests package:

```python
import requests

username = "your_username"
password = "your_password"
response = requests.get("http://api.example.com/data", auth=(username, password))
```

## Features
* **Standard Authentication Mechanism:** Basic authentication is a standard authentication mechanism implemented by HTTP servers, clients, and web browsers
* **Authorization Header:** A request made using Basic Authentication includes an "Authorization" header that contains the API key. The value of the Authorization header is in the form: Basic base64Encode(username:password)
* **Security Considerations:** Basic Authentication is a simple method, but the authentication credentials are transferred as encoded plain text, making it susceptible to interception. It is recommended to use Basic Authentication only in conjunction with a secure transport layer such as SSL
* **Implementation in Python:** In Python, basic authentication can be implemented using the requests library, which provides built-in support for Basic Authentication. The HTTPBasicAuth class from the requests.auth module can be used to include basic authentication in the requests
* **Ease of Use:** Basic authentication is relatively easy to implement and is suitable for smaller APIs. It can be enabled by setting a flag in the API Definition object or by using the HTTPBasic class in Python frameworks such as FastAPI
* **Security Enhancements:** In Python, it is important to handle basic authentication securely by using techniques such as comparing passwords using secrets.compare_digest() to mitigate timing attacks

## Simple API
Simple HTTP API for playing with `User` model.

## Files
### `models/`
- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`
- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

## Setup
```
$ pip3 install -r requirements.txt
```

## Run
```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Credits
 * [Advanced JAX-RS 22 - REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
 * [base64 in Python](https://docs.python.org/3.7/library/base64.html)
 * [HTTP Header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
 * [Flask](https://palletsprojects.com/p/flask/)
 * [Base64 Concept](https://en.wikipedia.org/wiki/Base64)

## Contact
 * [Twitter](https://www.twitter.com/sakhilelindah) / [Github](https://github.com/sakhi-4096) / [Mail](mailto:sakhilelindah@protonmail.com)
