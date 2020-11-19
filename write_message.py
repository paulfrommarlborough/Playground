""" write_message.py:  file write examples """

filename="test_write.txt"
with open(filename, 'w') as f:
        f.write("write a line to the file...\n")
        f.write("write the next line to the file...\n")


# while loop to get reasons , write to file and get out
filereasons="reasons.txt"
done = 0
while not done:
    reason = input("why: ");
    if reason == 'done':
        done=1
    else:
        with open(filereasons, 'a') as fr:
            fr.write(reason)
            fr.write("\n")
            
