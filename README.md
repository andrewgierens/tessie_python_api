# Tessie Python API Wrapper
![Total downloads for the project](https://static.pepy.tech/badge/tessie-api) ![Last 30 days downloads for the project](https://static.pepy.tech/badge/tessie-api/month)


## Description
Tessie Python API Wrapper is a simple wrapper designed to interact with various APIs exposed by Tessie.

https://pypi.org/project/tessie-api/

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
from tessie_api import get_state_of_all_vehicles

async def main():
    async with aiohttp.ClientSession() as session:  # ClientSession is created here and will be closed when exiting the block
        data = await get_state_of_all_vehicles(session=session, api_key="TESSIE_KEY", only_active=True)
        print(data)

if __name__ == "__main__":
    asyncio.run(main())
```

## Tests
```bash
pip install -e .
pytest
```

## Contributing
Contributions to Tessie Python API Wrapper are welcome and appreciated. If you have any suggestions or bug reports, please open an issue in the repository.
[creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License
This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributors
<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/andrewgierens">
            <img src="https://avatars.githubusercontent.com/u/4150500?v=4" width="100;" alt="andrewgierens"/>
            <br />
            <sub><b>Andrew Gierens</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Bre77">
            <img src="https://avatars.githubusercontent.com/u/2647914?v=4" width="100;" alt="Bre77"/>
            <br />
            <sub><b>Brett Adams</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/KrzysztofHajdamowicz">
            <img src="https://avatars.githubusercontent.com/u/24268470?v=4" width="100;" alt="KrzysztofHajdamowicz"/>
            <br />
            <sub><b>KrzysztofHajdamowicz</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->
