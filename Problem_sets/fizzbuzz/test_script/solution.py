def fizzbuzz(int_list):
    out_list = []
    for i in int_list:
        output = ""
        if i%3 == 0:
            output+="Fizz"
        if i%5 == 0:
            output+="Buzz"
        if output:
            out_list.append(output)
        else:
            out_list.append(i)
    
    return out_list