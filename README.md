# Controller
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/StykMartin/controller.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/StykMartin/controller/context:python)[![Coverage Status](https://coveralls.io/repos/github/StykMartin/controller/badge.svg?branch=master)](https://coveralls.io/github/StykMartin/controller?branch=master)

This project aims to replace the current implementation of Beaker Lab Controller, however, API will remain the same.

This is a strong requirement, otherwise, tooling like Restraint would be locked out of the loop.

## Changes
- Only Python 3 implementation
- ASGI instead of WSGI
- REST API only. XMLRPC interface is not supported
- RHEL7+ support. ANAMON for older distributions will be no longer available.
