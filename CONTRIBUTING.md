# How to contribute

First of all, thank you for taking the time to contribute and making this repository more fruitful. 

#### Table Of Contents

* [Code of conduct](#code-of-conduct)
* [Submitting an alternate solution](#submitting-an-alternate-solution)
* [Submitting a problem with a solution](#submitting-a-problem-with-a-solution)
* [Submitting a problem without a solution](#submitting-a-problem-without-a-solution)

## Code of conduct

This project and everyone participating is governed by the [DSA collaborative prep code of conduct](https://github.com/anasm-17/DSA_collaborative_prep/blob/master/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code, please report unacceptable behavior to [anas.m.017@gmail.com](anas.m.017@gmail.com)

## Submitting an alternate solution

You can submit an alternate solution to an existing problem, create your solution in the directory of the problem and follow the following template for your solution script:

```
from test_script.test import test_<problem_set_dir_name>

def yoursolutionfunc(some_input):
  --- Your solution ---
 
 
if __name__ == '__main__':
    test_fizzbuzz(yoursolutionfunc)
```
#### Steps
1. Fork and clone the repo.
2. Save your solution script as "<problem_set_dir>/<problem_set_dir_name>_<your_github-username>.py" eg. "fizzbuzz/fizzbuzz_anasm-17.py". `yoursolutionfunc` can be any name you like. You may use any name you like, but this will help me incorporate your github repository into the leaderboard feature (coming soon).
3. You may download the alternate solution template [here](https://github.com/anasm-17/DSA_collaborative_prep/blob/master/templates/dir-name_your-github-user.py) or copy it from the templates folder.
4. Make sure you are caught up with this upstream branch, commit and push changes to your forked repo and then submit a pull request.

## Submitting a problem with a solution

For problems of difficulty levels `difficult` to `very difficult` your problem set directory will have to be accompanied with a pseudocode/diagrams that explains your thought process (it's actually extremely difficult solving such problems without pseudocode and diagrams, so you can export raw pictures of your scratch paper, etc).

#### Steps
1. Fork and clone this repo into your system.
1. Copy the contents of the [templates folder](https://github.com/anasm-17/DSA_collaborative_prep/tree/master/templates) into your new problem directory so Problem_sets/<new_problem_dir>/ 
2. Edit the files as per the instructions in the template.
3. post your solution and keep your solution as the test_script/solution.py, this will be the benchmark till a better solution comes along.
4. Explain the problem within the `problem_statement.md` file, be sure to cite if you have copied the description from somewhere.
5. For problems rated `difficult` or higher add images or pseudocode to explain your thought process in deriving the solution.
6. Make sure you are caught up with this upstream branch, commit and push these changes to your repo and submit a pull request.

## Submitting a problem without a solution

Sometimes, we may find a problem that we would love to solve but are unable to, don't worry! We are here to assist each other. Follow the steps for submitting a problem without a solution.

#### Steps
1. Fork and clone this repo into your system.
1. Copy the contents of the [templates folder](https://github.com/anasm-17/DSA_collaborative_prep/tree/master/templates) into your new problem directory so Problem_sets/<new_problem_dir>/ 
2. Explain the problem within the `problem_statement.md` file, be sure to cite if you have copied the description from somewhere.
3. Make sure you are caught up with this upstream branch, commit and push changes to your forked repo and then submit a pull request.

Thank you for contributing! Happy coding!
