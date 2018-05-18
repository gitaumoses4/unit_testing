# Python Unit Testing Example
[![Build Status](https://travis-ci.org/gitaumoses4/unit_testing.svg?branch=develop)](https://travis-ci.org/gitaumoses4/unit_testing)
[![Coverage Status](https://coveralls.io/repos/github/gitaumoses4/unit_testing/badge.svg?branch=develop)](https://coveralls.io/github/gitaumoses4/unit_testing?branch=develop)
![license](https://img.shields.io/github/license/gitaumoses4/unit_testing.svg)

A basic implementation of a Linked List with basic list implementation such as:

 - Insertion
 - Deletion
 - Checking existence of an element
 - Checking emptiness of the list
 - Get the length of the linked list

## Installation
To run the tests first create the virtual environment

```bash 
python3 -m venv venv
```
Activate the virtual environment
```bash
source venv/bin/activate
```

Finally install the requirements in order to perform the tests with `nosetests` and `coverage`
```bash
pip install -r requirements.txt
```

## Testing
```bash
nosetests test_linked_list.py
```

With coverage
```bash
nosetests --with-coverage test_linked_list.py
```