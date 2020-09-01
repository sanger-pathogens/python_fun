# fun
A python test for developers

## Install
Clone the repository locally and ideally install in a virtual environment:
```
# Clone the repo locally
git clone https://github.com/sanger-pathogens/fun
cd fun

# Create and activate a virtual environment
virtualenv venv
source venv/bin/activate

# Install fun
pip install .

# Run the tests
python setup.py nosetests
```

## Uninstall
```
pip uninstall fun
```

## Usage
The fun application reads fasta files and compute various statistics.  
Since the application is under development, please see the online help:
```
fun.py -h
```

## Test data
A test fasta file is available in the ```test_data``` directory

## License
Fun is free software, licensed under [GPLv3](https://github.com/seretol/fun/blob/master/LICENSE).

