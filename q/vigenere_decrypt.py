from lib import *

def main():
  plain = get_plaintext()
  key = "MATH"
  K = shifted_set_from_word(key)
  c = alphabetic_encrypt(plain, K)

  print(c[:32])
  print("key length", len(key))
  print(estimate_r(I_c_from_text(c), len(c)))

def get_plaintext():
  return [ a for a in """
    g, O goddess, the anger of Achilles son of Peleus, that brought countless ills upon the Achaeans. Many a brave soul did it send hurrying down to Hades, and many a hero did it yield a prey to dogs and vultures, for so were the counsels of Jove fulfilled from the day on which the son of Atreus, king of men, and great Achilles, first fell out with one another.
    And which of the gods was it that set them on to quarrel? It was the son of Jove and Leto; for he was angry with the king and sent a pestilence upon the host to plague the people, because the son of Atreus had dishonoured Chryses his priest. Now Chryses had come to the ships of the Achaeans to free his daughter, and had brought with him a great ransom: moreover he bore in his hand the sceptre of Apollo wreathed with a suppliant's wreath and he besought the Achaeans, but most of all the two sons of Atreus, who were their chiefs.
    "Sons of Atreus," he cried, "and all other Achaeans, may the gods who dwell in Olympus grant you to sack the city of Priam, and to reach your homes in safety; but free my daughter, and accept a ransom for her, in reverence to Apollo, son of Jove."
    On this the rest of the Achaeans with one voice were for respecting the priest and taking the ransom that he offered; but not so Agamemnon, who spoke fiercely to him and sent him roughly away. "Old man," said he, "let me not find you tarrying about our ships, nor yet coming hereafter. Your sceptre of the god and your wreath shall profit you nothing. I will not free her. She shall grow old in my house at Argos far from her own home, busying herself with her loom and visiting my couch; so go, and do not provoke me or it shall be the worse for you."
    The old man feared him and obeyed. Not a word he spoke, but went by the shore of the sounding sea and prayed apart to King Apollo whom lovely Leto had borne. "Hear me," he cried, "O god of the silver bow, that protectest Chryse and holy Cilla and rulest Tenedos with thy might, hear me oh thou of Sminthe. If I have ever decked your temple with garlands, or burned your thigh-bones in fat of bulls or goats, grant my prayer, and let your arrows avenge these my tears upon the Danaans."
    Thus did he pray, and Apollo heard his prayer. He came down furious from the summits of Olympus, with his bow and his quiver upon his shoulder, and the arrows rattled on his back with the rage that trembled within him. He sat himself down away from the ships with a face as dark as night, and his silver bow rang death as he shot his arrow in the midst of them. First he smote their mules and their hounds, but presently he aimed his shafts at the people themselves, and all day long the pyres of the dead were burning.
    For nine whole days he shot his arrows among the people, but upon the tenth day Achilles called them in assembly- moved thereto by Juno, who saw the Achaeans in their death-throes and had compassion upon them. Then, when they were got together, he rose and spoke among them.
    "Son of Atreus," said he, "I deem that we should now turn roving home if we would escape destruction, for we are being cut down by war and pestilence at once. Let us ask some priest or prophet, or some reader of dreams (for dreams, too, are of Jove) who can tell us why Phoebus Apollo is so angry, and say whether it is for some vow that we have broken, or hecatomb that we have not offered, and whether he will accept the savour of lambs and goats without blemish, so as to take away the plague from us."
    With these words he sat down, and Calchas son of Thestor, wisest of augurs, who knew things past present and to come, rose to speak. He it was who had guided the Achaeans with their fleet to Ilius, through the prophesyings with which Phoebus Apollo had inspired him. With all sincerity and goodwill he addressed them thus:-
    "Achilles, loved of heaven, you bid me tell you about the anger of King Apollo, I will therefore do so; but consider first and swear that you will stand by me heartily in word and deed, for I know that I shall offend one who rules the Argives with might, to whom all the Achaeans are in subjection. A plain man cannot stand against the anger of a king, who if he swallow his displeasure now, will yet nurse revenge till he has wreaked it. Consider, therefore, whether or no you will protect me."
    And Achilles answered, "Fear not, but speak as it is borne in upon you from heaven, for by Apollo, Calchas, to whom you pray, and whose oracles you reveal to us, not a Danaan at our ships shall lay his hand upon you, while I yet live to look upon the face of the earth- no, not though you name Agamemnon himself, who is by far the foremost of the Achaeans."
    Thereon the seer spoke boldly. "The god," he said, "is angry neither about vow nor hecatomb, but for his priest's sake, whom Agamemnon has dishonoured, in that he would not free his daughter nor take a ransom for her; therefore has he sent these evils upon us, and will yet send others. He will not deliver the Danaans from this pestilence till Agamemnon has restored the girl without fee or ransom to her father, and has sent a holy hecatomb to Chryse. Thus we may perhaps appease him."
    With these words he sat down, and Agamemnon rose in anger. His heart was black with rage, and his eyes flashed fire as he scowled on Calchas and said, "Seer of evil, you never yet prophesied smooth things concerning me, but have ever loved to foretell that which was evil. You have brought me neither comfort nor performance; and now you come seeing among Danaans, and saying that Apollo has plagued us because I would not take a ransom for this girl, the daughter of Chryses. I have set my heart on keeping her in my own house, for I love her better even than my own wife Clytemnestra, whose peer she is alike in form and feature, in understanding and accomplishments. Still I will give her up if I must, for I would have the people live, not die; but you must find me a prize instead, or I alone among the Argives shall be without one. This is not well; for you behold, all of you, that my prize is to go elsewhither."
    And Achilles answered, "Most noble son of Atreus, covetous beyond all mankind, how shall the Achaeans find you another prize? We have no common store from which to take one. Those we took from the cities have been awarded; we cannot disallow the awards that have been made already. Give this girl, therefore, to the god, and if ever Jove grants us to sack the city of Troy we will requite you three and fourfold."
    Then Agamemnon said, "Achilles, valiant though you be, you shall not thus outwit me. You shall not overreach and you shall not persuade me. Are you to keep your own prize, while I sit tamely under my loss and give up the girl at your bidding? Let the Achaeans find me a prize in fair exchange to my liking, or I will come and take your own, or that of Ajax or of Ulysses; and he to whomsoever I may come shall rue my coming. But of this we will take thought hereafter; for the present, let us draw a ship into the sea, and find a crew for her expressly; let us put a hecatomb on board, and let us send Chryseis also; further, let some chief man among us be in command, either Ajax, or Idomeneus, or yourself, son of Peleus, mighty warrior that you are, that we may offer sacrifice and appease the the anger of the god."
    Achilles scowled at him and answered, "You are steeped in insolence and lust of gain. With what heart can any of the Achaeans do your bidding, either on foray or in open fighting? I came not warring here for any ill the Trojans had done me. I have no quarrel with them. They have not raided my cattle nor my horses, nor cut down my harvests on the rich plains of Phthia; for between me and them there is a great space, both mountain and sounding sea. We have followed you, Sir Insolence! for your pleasure, not ours- to gain satisfaction from the Trojans for your shameless self and for Menelaus. You forget this, and threaten to rob me of the prize for which I have toiled, and which the sons of the Achaeans have given me. Never when the Achaeans sack any rich city of the Trojans do I receive so good a prize as you do, though it is my hands that do the better part of the fighting. When the sharing comes, your share is far the largest, and I, forsooth, must go back to my ships, take what I can get and be thankful, when my labour of fighting is done. Now, therefore, I shall go back to Phthia; it will be much better for me to return home with my ships, for I will not stay here dishonoured to gather gold and substance for you."
    And Agamemnon answered, "Fly if you will, I shall make you no prayers to stay you. I have others here who will do me honour, and above all Jove, the lord of counsel. There is no king here so hateful to me as you are, for you are ever quarrelsome and ill affected. What though you be brave? Was it not heaven that made you so? Go home, then, with your ships and comrades to lord it over the Myrmidons. I care neither for you nor for your anger; and thus will I do: since Phoebus Apollo is taking Chryseis from me, I shall send her with my ship and my followers, but I shall come to your tent and take your own prize Briseis, that you may learn how much stronger I am than you are, and that another may fear to set himself up as equal or comparable with me."
    The son of Peleus was furious, and his heart within his shaggy breast was divided whether to draw his sword, push the others aside, and kill the son of Atreus, or to restrain himself and check his anger. While he was thus in two minds, and was drawing his mighty sword from its scabbard, Minerva came down from heaven (for Juno had sent her in the love she bore to them both), and seized the son of Peleus by his yellow hair, visible to him alone, for of the others no man could see her. Achilles turned in amaze, and by the fire that flashed from her eyes at once knew that she was Minerva. "Why are you here," said he, "daughter of aegis-bearing Jove? To see the pride of Agamemnon, son of Atreus? Let me tell you- and it shall surely be- he shall pay for this insolence with his life."
    And Minerva said, "I come from heaven, if you will hear me, to bid you stay your anger. Juno has sent me, who cares for both of you alike. Cease, then, this brawling, and do not draw your sword; rail at him if you will, and your railing will not be vain, for I tell you- and it shall surely be- that you shall hereafter receive gifts three times as splendid by reason of this present insult. Hold, therefore, and obey."
    "Goddess," answered Achilles, "however angry a man may be, he must do as you two command him. This will be best, for the gods ever hear the prayers of him who has obeyed them."
    He stayed his hand on the silver hilt of his sword, and thrust it back into the scabbard as Minerva bade him. Then she went back to Olympus among the other gods, and to the house of aegis-bearing Jove.
    But the son of Peleus again began railing at the son of Atreus, for he was still in a rage. "Wine-bibber," he cried, "with the face of a dog and the heart of a hind, you never dare to go out with the host in fight, nor yet with our chosen men in ambuscade. You shun this as you do death itself. You had rather go round and rob his prizes from any man who contradicts you. You devour your people, for you are king over a feeble folk; otherwise, son of Atreus, henceforward you would insult no man. Therefore I say, and swear it with a great oath- nay, by this my sceptre which shalt sprout neither leaf nor shoot, nor bud anew from the day on which it left its parent stem upon the mountains- for the axe stripped it of leaf and bark, and now the sons of the Achaeans bear it as judges and guardians of the decrees of heaven- so surely and solemnly do I swear that hereafter they shall look fondly for Achilles and shall not find him. In the day of your distress, when your men fall dying by the murderous hand of Hector, you shall not know how to help them, and shall rend your heart with rage for the hour when you offered insult to the bravest of the Achaeans."
    With this the son of Peleus dashed his gold-bestudded sceptre on the ground and took his seat, while the son of Atreus was beginning fiercely from his place upon the other side. Then uprose smooth-tongued Nestor, the facile speaker of the Pylians, and the words fell from his lips sweeter than honey. Two generations of men born and bred in Pylos had passed away under his rule, and he was now reigning over the third. With all sincerity and goodwill, therefore, he addressed them thus:-
    "Of a truth," he said, "a great sorrow has befallen the Achaean land. Surely Priam with his sons would rejoice, and the Trojans be glad at heart if they could hear this quarrel between you two, who are so excellent in fight and counsel. I am older than either of you; therefore be guided by me. Moreover I have been the familiar friend of men even greater than you are, and they did not disregard my counsels. Never again can I behold such men as Pirithous and Dryas shepherd of his people, or as Caeneus, Exadius, godlike Polyphemus, and Theseus son of Aegeus, peer of the immortals. These were the mightiest men ever born upon this earth: mightiest were they, and when they fought the fiercest tribes of mountain savages they utterly overthrew them. I came from distant Pylos, and went about among them, for they would have me come, and I fought as it was in me to do. Not a man now living could withstand them, but they heard my words, and were persuaded by them. So be it also with yourselves, for this is the more excellent way. Therefore, Agamemnon, though you be strong, take not this girl away, for the sons of the Achaeans have already given her to Achilles; and you, Achilles, strive not further with the king, for no man who by the grace of Jove wields a sceptre has like honour with Agamemnon. You are strong, and have a goddess for your mother; but Agamemnon is stronger than you, for he has more people under him. Son of Atreus, check your anger, I implore you; end this quarrel with Achilles, who in the day of battle is a tower of strength to the Achaeans."
    And Agamemnon answered, "Sir, all that you have said is true, but this fellow must needs become our lord and master: he must be lord of all, king of all, and captain of all, and this shall hardly be. Granted that the gods have made him a great warrior, have they also given him the right to speak with railing?"
    Achilles interrupted him. "I should be a mean coward," he cried, "were I to give in to you in all things. Order other people about, not me, for I shall obey no longer. Furthermore I say- and lay my saying to your heart- I shall fight neither you nor any man about this girl, for those that take were those also that gave. But of all else that is at my ship you shall carry away nothing by force. Try, that others may see; if you do, my spear shall be reddened with your blood."
    When they had quarrelled thus angrily, they rose, and broke up the assembly at the ships of the Achaeans. The son of Peleus went back to his tents and ships with the son of Menoetius and his company, while Agamemnon drew a vessel into the water and chose a crew of twenty oarsmen. He escorted Chryseis on board and sent moreover a hecatomb for the god. And Ulysses went as captain
    These, then, went on board and sailed their ways over the sea. But the son of Atreus bade the people purify themselves; so they purified themselves and cast their filth into the sea. Then they offered hecatombs of bulls and goats without blemish on the sea-shore, and the smoke with the savour of their sacrifice rose curling up towards heaven.
    Thus did they busy themselves throughout the host. But Agamemnon did not forget the threat that he had made Achilles, and called his trusty messengers and squires Talthybius and Eurybates. "Go," said he, "to the tent of Achilles, son of Peleus; take Briseis by the hand and bring her hither; if he will not give her I shall come with others and take her- which will press him harder."
    He charged them straightly further and dismissed them, whereon they went their way sorrowfully by the seaside, till they came to the tents and ships of the Myrmidons. They found Achilles sitting by his tent and his ships, and ill-pleased he was when he beheld them. They stood fearfully and reverently before him, and never a word did they speak, but he knew them and said, "Welcome, heralds, messengers of gods and men; draw near; my quarrel is not with you but with Agamemnon who has sent you for the girl Briseis. Therefore, Patroclus, bring her and give her to them, but let them be witnesses by the blessed gods, by mortal men, and by the fierceness of Agamemnon's anger, that if ever again there be need of me to save the people from ruin, they shall seek and they shall not find. Agamemnon is mad with rage and knows not how to look before and after that the Achaeans may fight by their ships in safety." 
    """.upper() if a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ]
main()
