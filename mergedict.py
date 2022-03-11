def mergedict(dict_1,dict_2):
    if (type(dict_1)!='dict_keys' and type(dict_2)!='dict_values') and (len(dict_1)!=len(dict_2)):
        return "two sources must be of type 'dict_keys' and 'dict_values' and have same lenth."
    else:
        new_dict={}
        for i in range(len(dict_1)):
            new_dict[list(dict_1)[i]]=list(dict_2)[i]
        return new_dict