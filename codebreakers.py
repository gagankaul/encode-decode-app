# An app to encode and decode text using pre-programmed key phrases

# You are responsible for writing a program that will encode or decode a message based off the letter distribution of a predetermined key text. Your program will determine a frequency analysis for two texts and use these letter distributions to create a cipher to either encode or decode a message based off user input. This program is an extension of the Frequency Analysis App.

import abc
from collections import Counter

#Display welcome message
print("Welcome to the Code Breakers App")

#Define the key phrases foe generating keys

#Passage from The Time Machine by HG Wells
key_phrase1 = '''The thing the Time Traveller held in his hand was a glittering metallic framework, scarcely larger than a small clock, and very delicately made. There was ivory in it, and some transparent crystalline substance. And now I must be explicit, for this that follows—unless his explanation is to be accepted—is an absolutely unaccountable thing. He took one of the small octagonal tables that were scattered about the room, and set it in front of the fire, with two legs on the hearthrug. On this table he placed the mechanism. Then he drew up a chair, and sat down. The only other object on the table was a small shaded lamp, the bright light of which fell upon the model. There were also perhaps a dozen candles about, two in brass candlesticks upon the mantel and several in sconces, so that the room was brilliantly illuminated. I sat in a low arm-chair nearest the fire, and I drew this forward so as to be almost between the Time Traveller and the fireplace. Filby sat behind him, looking over his shoulder. The Medical Man and the Provincial Mayor watched him in profile from the right, the Psychologist from the left. The Very Young Man stood behind the Psychologist. We were all on the alert. It appears incredible to me that any kind of trick, however subtly conceived and however adroitly done, could have been played upon us under these conditions.'''

#Passage from Around the World in 80 Days by Jules Verne
key_phrase2 = '''Phileas Fogg, having shut the door of his house at half-past eleven, and having put his right foot before his left five hundred and seventy-five times, and his left foot before his right five hundred and seventy-six times, reached the Reform Club, an imposing edifice in Pall Mall, which could not have cost less than three millions. He repaired at once to the dining-room, the nine windows of which open upon a tasteful garden, where the trees were already gilded with an autumn colouring; and took his place at the habitual table, the cover of which had already been laid for him. His breakfast consisted of a side-dish, a broiled fish with Reading sauce, a scarlet slice of roast beef garnished with mushrooms, a rhubarb and gooseberry tart, and a morsel of Cheshire cheese, the whole being washed down with several cups of tea, for which the Reform is famous. He rose at thirteen minutes to one, and directed his steps towards the large hall, a sumptuous apartment adorned with lavishly-framed paintings. A flunkey handed him an uncut Times, which he proceeded to cut with a skill which betrayed familiarity with this delicate operation. The perusal of this paper absorbed Phileas Fogg until a quarter before four, whilst the Standard, his next task, occupied him till the dinner hour. Dinner passed as breakfast had done, and Mr. Fogg re-appeared in the reading-room and sat down to the Pall Mall at twenty minutes before six. Half an hour later several members of the Reform came in and drew up to the fireplace, where a coal fire was steadily burning. They were Mr. Fogg’s usual partners at whist: Andrew Stuart, an engineer; John Sullivan and Samuel Fallentin, bankers; Thomas Flanagan, a brewer; and Gauthier Ralph, one of the Directors of the Bank of England—all rich and highly respectable personages, even in a club which comprises the princes of English trade and finance.'''

#Define a list of common non-alphabet and punctuation marks
non_letters = ["—", "-",".", "!", ",", "?", ";", "@", "'", "'", '"', '!', '#', '$', " ",'1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Convert all text to lowercase
key_phrase1 = key_phrase1.lower()
key_phrase2 = key_phrase2.lower()

#Generating the first key using key phrase 1

#Remove all non-letters
for each in non_letters:
  if each in key_phrase1:
    key_phrase1 = key_phrase1.replace(each, "")

#Generate the frequency table

letter_count_kp1 = Counter(key_phrase1)

letters_by_occurrence = letter_count_kp1.most_common()

sorted_list = []
for each in letters_by_occurrence:
  sorted_list.append(each[0])

primary_key = {}

for key, letter in zip(sorted(letter_count_kp1.keys()), sorted_list):
  primary_key[key] = letter

choice = input("\nWould you like to encode (e) or decode (d) a message (e/d): ").lower().strip()
message = input("\nEnter your message: ").lower().strip()
for non_letter in non_letters:
  if non_letter in message:
    message = message.replace(non_letter, "")

message_list = list(message)

if choice == "e":
  print("Here is the encoded message: ", end="")
  for each in message_list:
    print(primary_key[each], end="")
elif choice == "d":
  print("Here is the decoded message: ", end="")
  for each in message_list:
    for key, value in primary_key.items():
      if each == value:
        print(key, end="")
else:
  print("This is not a valid response!")




# #Generating the second key using key phrase 2

# #Remove all non-letters
# for each in non_letters:
#   if each in key_phrase2:
#     key_phrase2 = key_phrase2.replace(each, "")

# length_key_phrase2= len(key_phrase2)

# #Generate the frequency table

# letter_count_kp2 = Counter(key_phrase2)
# print(letter_count_kp2)