# Session Authentication 
Is a stateful authentication method commonly used in web applications.

## Description
It involves the use of sessions to keep track of authenticated users. When a user logs in, a session is created, and a unique session identifier (session ID) is stored on the server. This session ID is then shared with the client, typically through a cookie. The client includes the session ID in subsequent requests, allowing the server to identify and authenticate the user for the duration of the session. Session authentication is often used in conjunction with cookies to maintain the user's authenticated state. 
> It is a widely used authentication mechanism for web applications, providing a way to associate user-specific information with the client's requests.

## Features
* **Stateful Authentication:** Session authentication is stateful, meaning that it keeps track of the user's authentication state on the server.
* **Session ID:** A unique session ID is generated and stored on the server upon user authentication. This session ID is then shared with the client, often through a cookie, and is used to identify the user's session in subsequent requests.
* **Server-Side Storage:** User session details are stored on the server, allowing administrators to manage and invalidate sessions if necessary.
* **User Interaction:** Once a session is established, the user can interact with the application without repeatedly providing credentials.
* **Security Considerations:** Session authentication is susceptible to attacks such as session hijacking and cross-site request forgery, and requires careful implementation to ensure security.
* **Expiration and Invalidation:** Sessions have an expiration time, and can be invalidated by the server, providing a level of control over user sessions.
* **Traditional Web Applications:** Session authentication is commonly used in traditional web applications, where the server maintains the user's session state.

## Credits
 * [Advanced JAX-RS 22 - REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
 * [Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
 * [Flask](https://palletsprojects.com/p/flask/)
 * [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

## Contact
 * [Twitter](https://www.twitter.com/sakhilelindah) / [Github](https://github.com/sakhi-4096) / [Mail](mailto:sakhilelindah@protonmail.com)
