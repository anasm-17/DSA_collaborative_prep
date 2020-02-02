# DSA_collaborative_prep
A collaborative preparation repo for Data Structures and Algorithms problems that is open to public for participation. 

## Usage
Fork and/or clone this repo, navigate to the folder of your desired problem set, and make your solution script, be sure to import the test library of the respective problem set, pass your solution function as an object inside the test function. The standard for now will be 

```
from test_script import test_<problem_set_name>
```

### Example
For the fizzbuzz.py problem, go to "Problem_sets/fizzbuzz" and create your solution script.

```
from test_script.test import test_fizzbuzz

def yoursolutionfunc(some_input):
  --- Your solution ---
 
 
if __name__ == '__main__':
    test_fizzbuzz(yoursolutionfunc)
```

Then open your terminal and run your script. 

Happy coding! 

## Contributing
The repository will be more fruitful for the community with your contribution. Please follow the guidelines here if you wish to participate: [CONTRIBUTING.md](https://github.com/anasm-17/DSA_collaborative_prep/blob/master/CONTRIBUTING.md)
