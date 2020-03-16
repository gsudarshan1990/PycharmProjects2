"""
Write a function that reads a text file and counts the number of characters in
it.  Print both the text file and the number of characters. Do this so that the
printout isn't doubled space (use an end=""  argument in the print statement).
Also, skip a line before printing the count. Note that it is easy to get the
number of characters in each line using the len() function.
Here is my run for HumptyDumpty.txt.  Let me point out one thing that is not
visible here and is a bit technical.  At the end of each of the first three
lines there is a <newline> character.  These are invisible.  If you do the count
by eye, you are likely to come up short by these three characters, but they
are visible to len() and you should count them -- they are part of the 141
"letters" in the humptydumpty.txt file.  Counting them makes this an easier
function for you to write.


"""

def read_line_from_file(filename):
   count=0
   with open(filename) as file_header:
       for line in file_header:
           line=line.strip()
           print(line)
           words=line.split()
           length_words=len(words)
           for word in words:
              length=len(word)
              count=count+length
           count=count+length_words-1

   print("The total number of character ",count)










read_line_from_file("E:\Python_Latest_Besant_Technologies\All_Text_Files\humptydumpty.txt")