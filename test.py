
def reverse():
    # in_list should be like [35, 46, 57, 91, 29]
    in_list = [35, 46, 57, 91, 29]

    # reverse each element in the list
    out_list = [int(str(i)[::-1]) for i in in_list]

    # see the difference
    print('in_list:', in_list)
    print('out_list:', out_list)

    

if __name__ == "__main__":
    
    reverse()
