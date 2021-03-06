#program compares oliver.txt with kiersten.txt

#converts oliver.txt and kiersten.txt to lists
def convert_textfiles(file, listy_list):
    with open (file, 'r') as input_file:
        data = input_file.read()
        

    #input_file.close()
    listy_list = data.split(',')

    return listy_list
    
    
#converts lists back to textfiles
def convert_list(file, listy_list):
    output_file = open(file, 'w')
    
    for show in listy_list:
        output_file.write(show + ',')
        
    #output_file.close()
    
    
#searches lists in textfiles or lists
def search_lists(oliver, kiersten):
    match = False
    found = 0
    #list_one = ["banana", "orange", "apple"]
    #list_two = ["monkey", "dog", "cat", "apple"]

    
    for items in oliver:
        for data in kiersten:
            #print(items + " == " + data)
            if data == items:
                found = found + 1
                if(found == 1):
                    print("Match or matches found")
                    
                print(data)
                match = True
                
                
    return match

oliver = []
kiersten = []


oliver_file = 'oliver.txt'
kiersten_file = 'kiersten.txt'

oliver = convert_textfiles(oliver_file, oliver)

kiersten = convert_textfiles(kiersten_file, kiersten)


user = input("Enter user's name: ")
user_input = input("\nEnter movie or tv show: ")

while(user_input != 'q'):
    if (user == "Oliver" or user == "oliver"):
        print("Entering data for Oliver. Enter 'q' to quit. Enter 'u' to change users.")
        oliver.append(user_input)
    if (user == "Kiersten" or user == "kiersten"):
        print("Entering data for Kiersten. Enter 'q' to quit. Enter 'u' to change users.")
        kiersten.append(user_input)
    user_input = input("Enter movie or tv show: ")
    if (user_input == 'u'):
        user = input("Enter user's name: ")

convert_list(oliver_file, oliver)
convert_list(kiersten_file, kiersten)

#search for matches between lists
print("Searching for matches... this may take a minute")
match = search_lists(oliver, kiersten)
if(match == False):
    print("Match not found")
                     
