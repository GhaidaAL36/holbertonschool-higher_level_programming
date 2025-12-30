# HTTP and HTTPS Overview

## Background
The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows a client (such as a web browser) to communicate with a server by sending requests and receiving responses.  
HTTPS (HTTP Secure) is a secure version of HTTP that adds an encryption layer using SSL/TLS to protect transmitted data.

---

## Differences Between HTTP and HTTPS

### HTTP
- Sends data in plain text.
- Data can be intercepted or modified by attackers.
- Not secure for sensitive information.

### HTTPS
- Encrypts data using SSL/TLS.
- Protects data confidentiality and integrity.
- Authenticates the server using digital certificates.
- Commonly used for secure websites such as banking and login systems.

**Main Difference:**  
HTTPS encrypts communication, while HTTP does not.

---

## HTTP Request Structure
An HTTP request contains:

1. **Request Line**
   - HTTP Method (`GET`, `POST`, `PUT`, `DELETE`)
   - Request Target (URL or path)
   - HTTP Version (e.g. HTTP/1.1)

2. **Headers**
   - Provide metadata such as `Host`, `Content-Type`, and `Authorization`.

3. **Body (Optional)**
   - Contains data sent to the server (used with POST or PUT).

---

## HTTP Response Structure
An HTTP response contains:

1. **Status Line**
   - HTTP Version
   - Status Code

2. **Headers**
   - Describe the response (Content-Type, Content-Length, etc.).

3. **Body**
   - The response data (HTML, JSON, etc.).

---

## Common HTTP Methods

| Method | Description | Use Case |
|------|------------|---------|
| GET | Retrieves data | Fetching a web page or API data |
| POST | Sends new data | Submitting a form |
| PUT | Updates data | Updating an existing resource |
| DELETE | Removes data | Deleting a resource |

---

## Common HTTP Status Codes

| Status Code | Description | Scenario |
|------------|------------|----------|
| 200 | OK | Request succeeded |
| 201 | Created | Resource created successfully |
| 301 | Moved Permanently | Resource redirected |
| 400 | Bad Request | Invalid client request |
| 401 | Unauthorized | Authentication required |
| 404 | Not Found | Resource does not exist |
| 500 | Internal Server Error | Server failure |

---

## Conclusion
HTTP allows communication between clients and servers but does not provide security. HTTPS enhances HTTP by encrypting data and protecting it from eavesdropping and tampering. Understanding HTTP structure, methods, and status codes is essential for web development and API usage.
