#Video 1
#This is how to print documents
print("Hello, World!")

#video 2
#this is how to print a variable
#Python does not require variable declaration or semicolons. It operates on white space alone (looking at you js)
#variables are still lowercase and use underscores
message = "This is a message"
#use double quotes because if you need to contract a word python is going to count it as the end of the string ('bobby's world' vs "bobby's world")
#and vise versa
print(message)
message2="""This is a multi-line string in the 1900s, this was called a heredoc"""
#This also works but its a bit confusing
print(len(message2)) #prints the length of the string (len stands for length)
#here we are looking for a specific character in the string
print(message[0]) #prints the first character in the string
