#String are immutable
a = "!!!Paadi!!!!!!! Paadi!!!"
print(len(a)) #It gives total character size
print(a) 
print(a.lower()) #It can convert into all lowercase characters
print(a.upper()) #It can convert into all Uppercase characters
print(a.strip("!")) #It removes any white spaces before and after the string.
print(a.rstrip("!")) #It removes only trailing(ending) characters.
print(a.replace("Paadi", "Bhess")) #It replaces all occurences of a string (Do you want)

str1 = "Brand Paadi"
print(str1.split(" ")) #Splits the string at the whitespace " " and gives into list.

str2 = "introduction to paadI"
print(str2.capitalize()) #It gives only 1st character of string to Uppercase & rest other character Lowercase.
print(str2.center(75)) # It aligns string to the center as per parameters given by user.
print(str2.center(55, "."))

print(a.count("Paadi")) #It returns the number comman character as given by user
print(a.endswith("!!!")) #It checks if the strings ends with a given value. If yes then return true,else return false.

str3 = "He's name is Paadi. He/She is an Honest."
print(str3.find("is")) #It seach for the first occurrence of given value and return the index where it is present and value absent frome string then return -1
print(str3.index("is")) ##It seach for the first occurrence of given value and return the index where it is present and value absent frome give substring not found error

str4 = "WelcomeToTheConsole"
print(str4.isalnum())  #It returs true only if string only consists of A-Z,a-z,(0-9).

str4 = "Welcome"
print(str4.isalpha())  #It return true only if string only consists of A-Z,a-z.

str5 = "welcom paadi"
print(str5.islower()) #It return true if all the characters in the string are lowercase, else it return false.

str5 = "Welcome Paadi"
print(str5.isupper()) #It return true if all the characters in the string are uppercase, else it return false.

str5 = "We wise you a Tulsi Poojan"
print(str5.isprintable()) #It return true if all the values within the given strings are printable,else return false.

str6 = "          " #using spacebar
print(str6.isspace()) #It returns true only and only if the string contains white spaces, else return false.
str6 = "        " #using Tab
print(str6.isspace()) 

str7 = "World Health Organization"
print(str7.istitle()) # It return true only if the first letter of each word of the string is capitalized, else return false
print(str7.startswith("World")) #It checks if the strings starts with a given value. If yes then return true, else false
print(str7.swapcase()) #It changes the character casing of the string.Uppercase are converted to lowercase and lowercase to uppercase.

str1 = "He's name is Paadi. Paadi is an honest man."
print(str1.title()) #It capitalizes each letter of the word within the string