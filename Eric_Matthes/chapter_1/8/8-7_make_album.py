######Exercise 8-7

def make_album(artist,album,tracks=''):

#	if tracks:
#		dict = {'artist':artist.title(),'album':album.title(),'tracks':tracks}
#		return dict
#	else:
#		dict = {'artist':artist.title(),'album':album.title()}
#		return dict

# ИЛИ ТАК, меньше кода, более элегантно
	dict = {'artist':artist.title(),'album':album.title(),}
	if tracks:
		dict['tracks'] = tracks
		dict['review'] = '5 stars'
		dict['relisten again?'] = 'yes'
	return dict


alb1 = make_album('limp bizkit','chocolate starfish and the hotdog flavored water',17)
alb2 = make_album('marilyn manson','golden age of grotesque')
alb3 = make_album('papa roach','lovehatetragedy')

alb4 = make_album('the outfield','the outfield',15)
print(alb1)
print(alb2)
print(alb3)
print(alb4)





######Exercise 8-7
print('\n###########')
print('###########\n')

def malb(artist,album,tracks=''):
	dict = {'artist':artist.title(),'album':album.title(),}
	if tracks:
		dict['tracks'] = tracks
	return dict


while True:
	print('\nTell me about musician')
	print('---(Enter `q` to exit the program)---b')

	art = input('\nEnter the name of the musician: ')
	if art == 'q':
		break

	alb = input('Enter the name of the album: ')
	if alb == 'q':
		break

	form_artist = malb(art,alb)
	print(form_artist)
#	print(malb(art,alb))

