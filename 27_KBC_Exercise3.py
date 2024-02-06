#Create a program capable of displaying question to the user like kbc.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is talking home after playing the game.
import random

welcome = "Welcome to the KBC Contest"
print(welcome.center(85,"."))

Questions = [["The International Literacy Day is observed on", "sep 8", "Nov 28", "3.May 2" "Sep 22"],
["The language of Lakshadweep. a Union Territory of India, is","Tamil","Hindi","Malayalam","Telugu"],
["In which group of places the Kumbha Mela is held every twelve years?","Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar"],
["Bahubali festival is related to","Islam","Hinduism","Buddhism","Jainism","June 26","Oct 14","Nov 15","Dec 2"]]

levels = [1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000]
# for cases in range(1):
# cases = print(int(random.randint(1, 5)))
for i in range(0,len(Questions)):
    Questionsuestion = Questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a.{Questions[1]}                    b.{Questions[2]}")
    print(f"c.{Questions[3]}                    d.{Questions[4]}")
    reply = int(input("Enter your answer (1-4) "))
    # if(reply)