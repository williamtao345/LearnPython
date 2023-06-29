file_name = "removeReturn.txt"

file = open(file_name, "r")

new_string = file.read().replace("\n", " ")

file.close()

file = open(file_name, "w")
file.write(new_string)
file.close()
