# Python Challenge
Team International challenge


## Set up
 - Install a Python version that is greater than 3.6
 - Install pipenv
 - Run: `pipenv  --python <PYTHON_VERSION>` 
 - Install packages: `pipenv install`
 - To run tests: `pytest tests.py`


## Observations and notes
- Getters and setters were implemented,
- `typing` was implemented partially. Custom types were not implemented for the sake of the implemented time,
- tests were included and can be run with `pytest`
- Private attribute were implemented
- Operations `less`, `greater` and `between` run on constant time `O(1)`,
- Operation `build_stats` runs on linear time `O(n)`,
- Took less than 5 hours to implement and test.