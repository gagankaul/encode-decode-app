# An app to encode and decode text using pre-programmed key phrases

# You are responsible for writing a program that will encode or decode a message based off the letter distribution of a predetermined key text. Your program will determine a frequency analysis for two texts and use these letter distributions to create a cipher to either encode or decode a message based off user input. This program is an extension of the Frequency Analysis App.

import abc
from collections import Counter

#Display welcome message
print("Welcome to the Code Breakers App")

#Define the key phrases foe generating keys

#Passage from The Time Machine by HG Wells
key_phrase1 = '''The thing the Time Traveller held in his hand was a glittering metallic framework, scarcely larger than a small clock, and very delicately made. There was ivory in it, and some transparent crystalline substance. And now I must be explicit, for this that follows—unless his explanation is to be accepted—is an absolutely unaccountable thing. He took one of the small octagonal tables that were scattered about the room, and set it in front of the fire, with two legs on the hearthrug. On this table he placed the mechanism. Then he drew up a chair, and sat down. The only other object on the table was a small shaded lamp, the bright light of which fell upon the model. There were also perhaps a dozen candles about, two in brass candlesticks upon the mantel and several in sconces, so that the room was brilliantly illuminated. I sat in a low arm-chair nearest the fire, and I drew this forward so as to be almost between the Time Traveller and the fireplace. Filby sat behind him, looking over his shoulder. The Medical Man and the Provincial Mayor watched him in profile from the right, the Psychologist from the left. The Very Young Man stood behind the Psychologist. We were all on the alert. It appears incredible to me that any kind of trick, however subtly conceived and however adroitly done, could have been played upon us under these conditions. “Would you like to see the Time Machine itself?” asked the Time Traveller. And therewith, taking the lamp in his hand, he led the way down the long, draughty corridor to his laboratory. I remember vividly the flickering light, his queer, broad head in silhouette, the dance of the shadows, how we all followed him, puzzled but incredulous, and how there in the laboratory we beheld a larger edition of the little mechanism which we had seen vanish from before our eyes. Parts were of nickel, parts of ivory, parts had certainly been filed or sawn out of rock crystal. The thing was generally complete, but the twisted crystalline bars lay unfinished upon the bench beside some sheets of drawings, and I took one up for a better look at it. Quartz it seemed to be.'''

#Passage from Around the World in 80 Days by Jules Verne
key_phrase2 = '''Phileas Fogg, having shut the door of his house at half-past eleven, and having put his right foot before his left five hundred and seventy-five times, and his left foot before his right five hundred and seventy-six times, reached the Reform Club, an imposing edifice in Pall Mall, which could not have cost less than three millions. He repaired at once to the dining-room, the nine windows of which open upon a tasteful garden, where the trees were already gilded with an autumn colouring; and took his place at the habitual table, the cover of which had already been laid for him. His breakfast consisted of a side-dish, a broiled fish with Reading sauce, a scarlet slice of roast beef garnished with mushrooms, a rhubarb and gooseberry tart, and a morsel of Cheshire cheese, the whole being washed down with several cups of tea, for which the Reform is famous. He rose at thirteen minutes to one, and directed his steps towards the large hall, a sumptuous apartment adorned with lavishly-framed paintings. A flunkey handed him an uncut Times, which he proceeded to cut with a skill which betrayed familiarity with this delicate operation. The perusal of this paper absorbed Phileas Fogg until a quarter before four, whilst the Standard, his next task, occupied him till the dinner hour. Dinner passed as breakfast had done, and Mr. Fogg re-appeared in the reading-room and sat down to the Pall Mall at twenty minutes before six. Half an hour later several members of the Reform came in and drew up to the fireplace, where a coal fire was steadily burning. They were Mr. Fogg’s usual partners at whist: Andrew Stuart, an engineer; John Sullivan and Samuel Fallentin, bankers; Thomas Flanagan, a brewer; and Gauthier Ralph, one of the Directors of the Bank of England—all rich and highly respectable personages, even in a club which comprises the princes of English trade and finance. It was Phileas Fogg, whose head now emerged from behind his newspapers, who made this remark. He bowed to his friends, and entered into the conversation. The affair which formed its subject, and which was town talk, had occurred three days before at the Bank of England. A package of banknotes, to the value of fifty-five thousand pounds, had been taken from the principal cashier’s table, that functionary being at the moment engaged in registering the receipt of three shillings and sixpence. Of course, he could not have his eyes everywhere. Let it be observed that the Bank of England reposes a touching confidence in the honesty of the public. There are neither guards nor gratings to protect its treasures; gold, silver, banknotes are freely exposed, at the mercy of the first comer. A keen observer of English customs relates that, being in one of the rooms of the Bank one day, he had the curiosity to examine a gold ingot weighing some seven or eight pounds. He took it up, scrutinised it, passed it to his neighbour, he to the next man, and so on until the ingot, going from hand to hand, was transferred to the end of a dark entry; nor did it return to its place for half an hour. Meanwhile, the cashier had not so much as raised his head. But in the present instance things had not gone so smoothly. The package of notes not being found when five o’clock sounded from the ponderous clock in the “drawing office,” the amount was passed to the account of profit and loss. As soon as the robbery was discovered, picked detectives hastened off to Liverpool, Glasgow, Havre, Suez, Brindisi, New York, and other ports, inspired by the proffered reward of two thousand pounds, and five per cent. on the sum that might be recovered. Detectives were also charged with narrowly watching those who arrived at or left London by rail, and a judicial examination was at once entered upon.'''

#Define a list of common non-alphabet characters and punctuation marks
non_letters = ['“', '”',"—", '’',"-",".", "!", ",", "?", ";", ":","@", "'", "'", '"', '!', '#', '$', " ",'1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Convert all text to lowercase
key_phrase1 = key_phrase1.lower()
key_phrase2 = key_phrase2.lower()

#Remove non-English characters and all punctuation from both phrases
for each in non_letters:
  if each in key_phrase1:
    key_phrase1 = key_phrase1.replace(each, "")
    key_phrase2 = key_phrase2.replace(each, "")

#Build the letter frequency list from first key phrase
letter_count_1 = Counter(key_phrase1)
letters_by_occurrence_1 = letter_count_1.most_common()
sorted_list_1 = []
for each in letters_by_occurrence_1:
  sorted_list_1.append(each[0])


#Build the letter frequency list from second key phrase
letter_count_2 = Counter(key_phrase2)
letters_by_occurrence_2 = letter_count_2.most_common()
sorted_list_2 = []
for each in letters_by_occurrence_2:
  sorted_list_2.append(each[0])

#Generate the key using sorted_list_1 and sorted_list_2
primary_key = {}
for letter1, letter2 in zip(sorted_list_1, sorted_list_2):
  primary_key[letter1] = letter2

#Get uer input
choice = input("\nWould you like to encode (e) or decode (d) a message (e/d): ").lower().strip()
message = input("\nEnter your message: ").lower().strip()

#Remove non-English characters and punctuation from message 

if choice == "e":
  for non_letter in non_letters:
    if non_letter in message:
      message = message.replace(non_letter, "")
    message_list = list(message)
  print("Here is the encoded message: ", end="")
  for each in message_list:
    print(primary_key[each], end="")
elif choice == "d":
  message_list = list(message)
  print("Here is the decoded message: ", end="")
  for each in message_list:
    for key, value in primary_key.items():
      if each == value:
        print(key, end="")
else:
  print("This is not a valid response!")