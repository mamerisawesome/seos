# Seos

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/seos)](https://pypi.python.org/pypi/seos/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/mamerisawesome/seos/graphs/commit-activity)
[![Coverage](https://raw.githubusercontent.com/mamerisawesome/seos/master/assets/coverage.svg?sanitize=true)](https://github.com/mamerisawesome/seos)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

Simple Extractor on Sheets (or SEOS) is an extraction tool focused on Google Sheet data scraping. It uses Google's Python API client to access those data; this allows the library to access on a lower level functions defined by Google without the need of using another Sheets abstraction.

## Features

Seos features are put below and their status if they're well-tested using PyTest.

| Feature | Status            |
|----------------|-------------------|
| **Connection to a Google Sheet given an OAuth credentials file and Sheet ID** | ![Passed unit test](https://img.shields.io/static/v1?label=&message=Passed%20unit%20tests&color=green) |
| **Extraction on a sheet with a defined scope** | ![Passed unit test](https://img.shields.io/static/v1?label=&message=Passed%20unit%20tests&color=green) |
| **Sheet name switching** | ![Passed unit test](https://img.shields.io/static/v1?label=&message=Passed%20unit%20tests&color=green) |

## Installation

```bash
# if using poetry
# highly recommended
poetry add seos

# also works with standard pip
pip install seos
```

## Getting Started

Seos uses APIs defined by Google to access Sheets data; but the idea is that developing with Seos should be understandable when connecting to a data and changing contexts; e.g. change in Sheet Name or change in scope.

The initial step would be to pass a credentials file and the sheet ID as an entrypoint to the data. It assumes that you have a credentials file taken from `Google Cloud` in `JSON format`.

```python
from seos import Seos
extractor = Seos(
    credentials_file="./credentials.json"
    spreadsheet_id="<SPREADSHEET-ID>"
)
```

Once an extractor context is created, we can then define the `sheet name` and `scope` then executing extract if you're happy with the parameters.

```python
extractor.sheet_name = "Report - June 1, 1752"
extractor.scope = "A1:D1"
extractor.extract()
```

With this, changing the scope and the sheet name will act as a cursor for your sheet data. We can get anything from the sheet just by changing the scope.

```python
extractor.sheet_name = "Report - June 1, 1752"
extractor.scope = "A1:D" # get all from A1 until end of column D
extractor.extract()
```

We can even do sheet switching if necessary for data that contains several contexts.

```python
extractor.sheet_name = "Report - June 1, 1752"
extractor.scope = "A1:D"
extractor.extract()

extractor.sheet_name = "Report - June 2, 1752"
extractor.scope = "B5:G5"
extractor.extract()
```
