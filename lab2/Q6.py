color_dict = {
    "red": "#FF0000",
    "green": "#008000",
    "black": "#000000",
    "white": "#FFFFFF",
}


sorteddic = dict(sorted(color_dict.items()))  # sorted by key


print(str(sorteddic).replace(", ", ",\n "))
