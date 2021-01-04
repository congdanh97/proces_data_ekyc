import os
from pathlib import Path

## Xu ly file du lieu da gan nhan
urls_txt_cccd_name = list(Path("/home/congdanh/Downloads/", "6K_CCCD_NAME_OK_proces").glob("**/*"))

for j in urls_txt_cccd_name:
    string_name_proces = str(j)
    print(string_name_proces)
    string_name_proces = string_name_proces.replace("_-_", "_")
    index_2nd_before_tail=0
    # print("------------------")
    index = len(str(j))
    # print(index)
    index_tail = 0
    index_tail = str(j).rfind('_', 0, index)
    # print(str(index_tail))

    b=0
    index = len(str(j))

    index_2nd_before_tail= str(j).rfind('_', 0,index_tail)
    # print(b)
    # print(str(i))
    # print(str(i)[b])
    print(string_name_proces[index_2nd_before_tail-1])
    if string_name_proces[index_2nd_before_tail-1] == "_":
        if ((index_tail - index_2nd_before_tail) == 2)  or ((index_tail - index_2nd_before_tail) == 3) or ((index_tail - index_2nd_before_tail) == 4) :
            string_name_proces = str(j)
            # string_name_proces[index_2nd_before_tail] = "("
            # string_name_proces[index_tail] = ")"
            string_name_proces = string_name_proces[:index_2nd_before_tail] + "(" + string_name_proces[index_2nd_before_tail + 1 :]
            string_name_proces = string_name_proces[:index_tail] + ")" + string_name_proces[index_tail+1 :]

            string_name_proces = string_name_proces.replace("___", "_")
            string_name_proces = string_name_proces.replace("__", "_")

            os.rename(str(j), string_name_proces)
            print(string_name_proces)
        else:
            string_name_proces = string_name_proces.replace("___", "_")
            string_name_proces = string_name_proces.replace("__", "_")

            os.rename(str(j), string_name_proces)
            print(string_name_proces)
    else:
        string_name_proces = string_name_proces.replace("___", "_")
        string_name_proces = string_name_proces.replace("__", "_")

        os.rename(str(j), string_name_proces)
        print(string_name_proces)


