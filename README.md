# Simple Local OAuth Callback Server

A minimal HTTP server for handling OAuth callback redirects locally.

## Usage

### Clone the repository

```sh
git clone https://github.com/aspeckt-112/simple-local-oauth-callback-server.git
```
### Go to the newly cloned repository
```sh
cd simple-local-oauth-callback-server
```

### Run the server with Python 3

```sh
python3 callback_server.py
```

The server will listen on [http://localhost:8080](http://localhost:8080).  
When an OAuth provider redirects to `http://localhost:8080/?code=...`, the server will print the received code to the console.

You can use this server alongside tools like [Bruno](https://www.usebruno.com) to quickly develop and test APIs that require OAuth authentication.

## Requirements

- Python 3.x