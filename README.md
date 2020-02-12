![](Servirtium-Square.png?raw=true)

Main Servirtium site: http://servirtium.dev

# A Servirtium library for Python 

Demo project that uses it: https://github.com/servirtium/demo-python-climate-data-tck 

## Alpha quality software

Working so far:

* Record and playback of GET

Not Working yet:

* Support for POST, PUT etc.

Help needed from Pythonistas!

## Building Servirtium lib/package for Python3

Execute the following commands to install the package locally:

```
pip3 install requests
cd servirtium-python
pip3 install -e .
```

The 'demo-python-climate-data-tck' demo needs you to have built the Python version of Servirtium 
first as it is presently unpublished in pip-land.

## Running unit tests

```
pip3 install pytest
cd servirtium-python
pytest
```