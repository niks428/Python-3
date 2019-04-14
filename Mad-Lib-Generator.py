"""Mad Libs story that reader can fill in his/her own words into blank spaces that results in a funny story.
Code by: Nikhil Chauhan"""

print ('Starting Mad Libs, Woohoo!')

#'\' used at the end of line to continue same code in nex line.
#this is Paragraph/Story which will be filled with player data.
string="This morning I woke up and felt {} because {} was going to finally {} over the big {} {}.\
 On the other side of the {} were many {}s protesting to keep {} in stores. The crowd began to {} \
 to the rythym of the {}, which made all of the {} very {}. {} tried to {} into the sewers and found \
 {} rats. Needing help, {} quickly called {}. {} appeared and saved {} by flying to {} and dropping {}\
 into a puddle of {}. {} then fell asleep and woke up in the year {}, in a world where {}s ruled the world."
 
 #Shows Fill in the blanks optional in game.
print("This morning I woke up and felt {0} because {0} was going to finally {0} over the big {0} {0}.On theother \
      side of the {0} were many {0}s protesting to keep {0} in stores. The crowd began to {0} to the rythym of the \
      {0}, which made all of the {0} very {0}. {0} tried to {0} into the sewers and found {0} rats. Needing help, {0}\
      quickly called {0}. {0} appeared and saved {0} by flying to {0} and dropping {0} into a puddle of {0}.{0} then \
      fell asleep and woke up in the year {0}, in a world where {0}s ruled the world.".format("_._._._._._._"))

print("\n\n*******Enter Answears**********\n")
name = input('What is your name?')

#a-adjective
a_1= input('Hello! Please enter an Adjective. This can be a word used to describe something! It can be a feeling or a color!')
a_2=input('Enter another Adjective:')
a_3=input('And another Adjective:')

#v-verb
v_1= input ('Okay, Great! Now Enter a Verb. A verb is any word that is an action such as running or hopping or writing!')
v_2=input('And another Verb:')
v_3=input('One more Verb:')

#n-noun
n_1=input('Awesome! Now for a Noun! Please enter a word that is a person, place or thing.')
n_2=input('And another Noun:')
n_3=input('And another Noun:')
n_4=input('Last Noun!')

#t-weird thing
t_1= input('Name an animal that pops into your head!')
t_2=input('What is your favorite food?')
t_3=input('Give the name of a fruit that you despise!')
t_4=input('Enter a number:')
t_5=input('Who is your favorite Superhero?')
t_6=input('Name a country:')
t_7=input('We know you have a sweet tooth! Tell us your favorite dessert!')
t_8=input('Give us a Year:')

print("\n\n")
print (string.format(a_1, name, v_1, a_2, n_1, n_2, t_1, t_2, v_2, n_3, t_3, a_3, name, v_3, t_4, name,\
                     t_5, t_5, name, t_6, name, t_7, name, t_8, n_4))
