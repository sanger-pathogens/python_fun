# fun
A python test for developers

## Install
Clone the repository locally and ideally install in a virtual environment:
```
# Clone the repo locally
git clone https://github.com/sanger-pathogens/python_fun
cd python_fun

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install fun
pip install .

# Run the tests
## The tests are still written in unittest (legacy), 
##  but pytest runs them just fine
pytest
```

## Uninstall
```
pip uninstall python_fun
```

## Usage
The fun application reads fasta files and compute various statistics.  
Since the application is under development, please see the online help:
```
fun.py -h
```

## Test data
A test fasta file is available in the `test_data` directory

## License
Fun is free software, licensed under [GPLv3](https://github.com/sanger-pathogens/python_fun/blob/master/LICENSE).
