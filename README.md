<!-- @TODO: use this project's README as base: https://github.com/celery/kombu -->
# UnifiedREST

## Description
This Python library provides a standardized way to implement REST clients. It aims to offer a common language for developers, simplifying the process of maintaining and scaling web projects, especially those involving RESTful API communication.

## Key Features
- **Customizable REST Client:** Use any HTTP client library; comes with a default implementation for Python's Requests.
- **Extensible and Modular:** Easily add custom drivers, authentication modules, serialization, and parsing.
- **Pydantic Integration:** Leverages Pydantic for validation and internal implementation, ensuring type safety and consistency.
- **Developer Friendly:** Reduces cognitive load and streamlines onboarding for new developers in projects.

## Installation

```bash
pip install unifiedrest
```

## Quick Start
To get started with the Python REST Client Library, here's a basic example:

```python
from unifiedrest import *
from pydantic import BaseModel

# define our REST client
class MyRestClient(ClientBase):
    base_url: str = "https://swapi.dev/api/"

client = MyRestClient()

# GET https://swapi.dev/api/people/1
class Person(ModelBase):
    name: str
    height: int
    mass: int
    hair_color: str

await client.run(ClientRequest(
    url="/people/1",
    return_type=Person,
))

# Output:
# RunnerResponseDTO(
#     data=Person(
#         name='Luke Skywalker',
#         height=172,
#         mass=77,
#         hair_color='blond'
#     ),
#     http_code=200,
# )
```

For more detailed examples, refer to the included Jupyter notebooks (`01-rest-basic.ipynb` and `02-rest-declarative.ipynb`).

## Contributing
Contributions are welcome! Please read our Contributing Guide for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the file for details.
