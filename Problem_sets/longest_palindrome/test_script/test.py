import time
import numpy as np
import pickle
# from test_script.solution import longest_palindrome
test_cases = ["ac", "bb", "rrattarr", "defed", "adam", "bb"] #insert test case objects into a list eg [test-case-1, test-case-2, test-case-3]
loops = 10 # loops to be taken for calculating average time, for complex problems, lower this value.

def test_longest_palindrome(user_fun):
    success_flags = []

    # load solution pickle
    with open("solution_fn.pkl", "rb") as f:
        longest_palindrome = pickle.load(f)

    for test_case in test_cases:
        expected_output = longest_palindrome(test_case)
        user_output = user_fun(test_case)

        if user_output == expected_output:
            success_flags.append(1)
        else:
            success_flags.append(0)
        
    success_flag = min(success_flags) 
    
    if success_flag == 1:
        loop_time = []
        for i in range(loops):
            t1 = time.time()
            _ = user_fun(test_cases[0])
            t2 = time.time()
            
            loop_time.append(t2-t1)
        
        print("Passed {}/{} test cases!".format(sum(success_flags), len(success_flags)))
        print("Completed {} loops in average time of {:.7f} s.".format(loops, np.mean(loop_time)))
        print("Your output (first 20 lines limit):")
        # for out in user_output[:20]:
        #     print(out)
        print(user_output)
    else:
        print("Test failed! {}/{} passed.".format(sum(success_flags), len(success_flags)))