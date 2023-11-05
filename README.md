# Tessie Python API Wrapper

## Description
Tessie Python API Wrapper is a simple wrapper designed to interact with various APIs exposed by Tessie.

## Getting Started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- Python version >=3.5

### Installation
To install Tessie Python API Wrapper, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/andrewgierens/sems_portal_api.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
To use Tessie Python API Wrapper, you need to have Python and `aiohttp` installed. Here’s a quick example to get you started:

```python
import asyncio
from status import get_status

async def main():
    data = await get_status("VIN")
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
```

## Contributing
Contributions to Tessie Python API Wrapper are welcome and appreciated. If you have any suggestions or bug reports, please open an issue in the repository.
[creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License
This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
If you have any questions or want to reach out, you can contact me at apgierens@gmail.com