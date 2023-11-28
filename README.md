# UnifiedREST

## Description
This Python library provides a standardized way to implement REST clients, inspired by the principles of popular web frameworks like Django, Rails and Laravel. It aims to offer a common language for developers, simplifying the process of maintaining and scaling web projects, especially those involving RESTful API communication.

## Key Features
- **Customizable REST Client:** Use any HTTP client library; comes with a default implementation for Python's Requests.
- **Extensible and Modular:** Easily add custom drivers, authentication modules, serialization, and parsing.
- **Declarative Remote Actions:** Define REST interactions declaratively, encapsulating request and response handling in action classes.
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

class RestClient(ClientBase):
    base_url: str = "https://swapi.dev/api/"


class Person(DTO):
    name: str
    height: int
    mass: int
    hair_color: str


client = RestClient()

await client.run(ClientRequest(
    url="/people/1",
    return_type= Person,
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
