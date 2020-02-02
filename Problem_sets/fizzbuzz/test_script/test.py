import time
import numpy as np
from test_script.solution import fizzbuzz
test_cases = [list(range(1,100))]
loops = 10

def test_fizzbuzz(user_fun):
    success_flags = []
    for test_case in test_cases:
        expected_output = fizzbuzz(test_case)
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
        for out in user_output[:20]:
            print(out)
    else:
        print("Test failed! {}/{} passed.".format(sum(success_flags), len(success_flags)))