# M-API (dot py)

### What is it?
_Monitor API_ let's you monitor your system via a RESTful API.

This project uses the lovely Rust for the backend and the wonderful Python for the web server...

Did I mention this program uses [FFI programming](https://en.wikipedia.org/wiki/Foreign_function_interface)? It's my ~~first~~ second FFI-based project, and the performance may not be optimized.

That being said, this project is to help me learn Python and Rust FFI programming. Is it serving its purpose? Absolutely.

For more information on Rust FFI programming, please visit [The Rust FFI Omnibus](http://jakegoulding.com/rust-ffi-omnibus/).

This is also a Python implementation of [mapi](https://github.com/naltun/mapi).

##### ATTN:
This repository is _not_ ready for any production use, and probably never will be. For one, this is a project to help me learn Python and FFI programming; production use should have the web server reimplemented in pure Rust.

Also, features need to be implemented, such as additional system monitoring endpoints and API authorization.

That said, please feel free to use this software however you like.

### Installing
There are two files you will need to use:
* `requirements.txt`, located at the project root
* `Cargo.toml`, located in `mapi.rs/`

Run `pip install -r requirements.txt` at the project's root directory, then head into `mapi.rs/` and run `make`.

#### Rust requirements
```shell
libc = "0.2.0"
sysinfo = "0.8.0"
```

#### Python requirements
```shell
flask
```

### License

GNU GPLv2 because software freedom?

Love your Free/Libre, Open Source Software. For more information on freedom-respecting software, please visit [Wikipedia](https://en.wikipedia.org/wiki/Free_software_movement).
