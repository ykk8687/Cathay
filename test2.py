
def cal_char():
    alphbat_dict = {}
    # in_str should be like "Hello welcome to Cathay 60th year anniversary"
    in_str = input("Enter a string:")

    for s in in_str:
        if alphbat_dict.__contains__(s.lower()):
            alphbat_dict[s.lower()] += 1
        else:
            alphbat_dict[s.lower()] = 1

    for key, value in alphbat_dict.items():
        print(key+" "+str(value))
    

if __name__ == "__main__":

    cal_char()
    
    
