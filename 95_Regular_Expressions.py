'''
                    Regular Expressions
Regular expressions, or "regex" for short, are a powerful 
tool for working with strings and text data in Python. 
They allow you to match and manipulate strings based on 
patterns, making it easy to perform complex string 
operations with just a few lines of code.

        Metacharacters in regular expressions
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs

                Importing re Package
In Python, regular expressions are supported by the re module. The basic syntax for working with regular expressions in Python is as follows:

# import re
'''

import re

# pattern = "denial"
pattern = r"[A-Z]oS"
text = '''Denial-of-service attack
Denial-of-service attacks (DoS) are designed to make a machine or network resource unavailable to its intended users.[15] Attackers can deny service to individual victims, such as by deliberately entering a wrong password enough consecutive times to cause the victim's account to be locked, or they may overload the capabilities of a machine or network and block all users at once. While a network attack from a single IP address can be blocked by adding a new firewall rule, many forms of distributed denial-of-service (DDoS) attacks are possible, where the attack comes from a large number of points. In this case defending against these attacks is much more difficult. Such attacks can originate from the zombie computers of a botnet or from a range of other possible techniques, including distributed reflective denial-of-service (DRDoS), where innocent systems are fooled into sending traffic to the victim.[15] With such attacks, the amplification factor makes the attack easier for the attacker because they have to use little bandwidth themselves. To understand why attackers may carry out these attacks, see the 'attacker motivation' section. '''


match = re.search(pattern, text) #It gives first occurence only
print(match)

matches = re.finditer(pattern,text) #It gives all occurences
for match in matches:
    print(match)

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])