input_stream  = open("input.txt", "r")
output_stream = open("output.txt", "w")

lines = input_stream.readlines()
output_stream.writelines(lines)

input_stream.close()
output_stream.close()
