def data_types():
    int_ex = 100
    str_ex ="Hello, world!"
    float_ex = 31.67
    bool_ex = False
    list_ex = [1,2,3,"hELLO",True,[1,2]]
    dict_ex = {"key":"val"}
    tuple_ex = (1,2,3,"Hello", True)
    set_ex = {1,2,'A'}

    types =[type(int_ex), type(str_ex),type(float_ex),type(bool_ex),
            type(list_ex),type(dict_ex),type(tuple_ex),type(set_ex)]
    
    print(f"[{', '.join(t.__name__ for t in types)}]")

if __name__ == '__main__':
    data_types()
