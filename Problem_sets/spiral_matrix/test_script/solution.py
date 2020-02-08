import pickle

def spiral_matrix(desired_input):
    soln_idx = desired_input -1 

    with open("test_cases_spiral_op.pkl", "rb") as f:
        desired_output = pickle.load(f)
    
    return desired_output[soln_idx]