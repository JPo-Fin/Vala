# Vala Tehtävä 1  Python -koodilla toteutettuna

Ohjelman käynnistys:
VALA_teht_1.py (luettava_tiedosto) (Suorituksen tallennus tiedosto)
esim: VALA_teht_1.py Vala_input.txt Vala_output.txt

THEORY:
Multiples of A and B
Let’s assume that A is 4 and B is 7, so
If we list all the natural numbers below 20 that are multiples of A or B, we get 4, 7, 8, 12, 14
and 16. 
TASK:
Create a program that takes a file as the first command line argument. The file content is list of 
numbers, with 3 numbers per row separated by space and number of rows is undefined (can 
be something between 1 - infinite). First number in a row is A and the second is B, third one is 
the goal number (as in theorem 20). The program has to search all multiples of A and B which 
are below the third number, print it out to screen and also write results to file which was given 
as the second command line argument.
Program should sort out output file by ascending order how many multiples certain row has.
Example input file content:
5 8 31
4 7 20
Example command line command: python my_program.py input.txt output.txt
Example screen output and output file content:
20:4 7 8 12 14 16 
31:5 8 10 15 16 20 24 25 30
    
