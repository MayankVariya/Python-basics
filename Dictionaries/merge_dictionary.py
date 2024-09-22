first_dic = {
    "name":"Your Name",
    "surname":"Your surname"
}

second_dic = {
    "age":23,
    "gender":"Male"
}

merged_dic = {**first_dic,**second_dic}

print(f"Merged dictionary :{merged_dic}")