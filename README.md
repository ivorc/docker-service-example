# A Python / Tornado Example

# Usage Instructions

Create a Python virtualenv. A virtualenv isolates Python environments so that
packages installed in one environment don't affect others.

From the commannd line, install the virtual environment.

 * ```pip install virtualenv```

Create the virtual environment:

 * ```virtualenv env```

Start using it:

 * Windows
   * ```.\env\Scripts\activate.bat```
 * Linux
   * ```source bin/activate```

Install packages into the virtualenv:

```
pip install pymongo flask psutil jsonpickle pytest coverage tornado motor pytest-cov
```

Go into the establishment_service directory:

 * ```cd establishment_service```

Install the establishment_service package into the environment:

 * ```pip install -e .```

The import process uses:
 * Flask to provide a HTTP status endpoint

The systems use:
 * pymongo to access MongoDB
 * psutil to determine the current RAM consumption
 * jsonpickle for JSON handling
 * pytest for easy unit testing
 * coverage to calculate code coverage for unit tests

The web service uses:
 * tornado for running a web server
 * motor for asynchronous mongodb support

# Running (Import)
```
python3 import_data.py
```

# Running the establishment service REST service

```
python3 app.py
```

To test it:

 * ``` http://localhost:8888/establishment/563a13a2edf60c2478052035```
 * ``` http://localhost:8888/establishment/```

# Running Test Cases

Run the tests:

 * ```py.test```

Get code coverage stats:

 * ```py.test --cov```

Create a HTML report

 * ```py.test --cov --cov-report=html```
