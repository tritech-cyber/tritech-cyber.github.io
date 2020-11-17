def string_concat_repos(a):
	b = "<a href = "+'"'+"https://github.com/"
	b = b + str(a[1])
	b = b +"?tab=repositories\" target =\"_blank\" >"+a[0]+"-"+a[1]+"</a><br />"
	return b

def string_concat_io(a):
    b = "<a href = "+'"'+"https://"
    b = b + a + ".github.io"
    b = b +'"' + " target ="+ '"'+"_blank"+'"'+">"+a[0]+"</a><br />"
    return b

def main():
	users = [['A,Ulises','ulises-aguilar']
,	['A,Miguel A','MiguelAlcalan2020']
,	['B,Christopher Logan','Logan-Benner']
,	['B,Daniel S','danielbrogan26']
,	['D,Andrew','DemonDrew0508']
,	['K,Austin','jkiik']
,	['K,Ian Gerald','kernelpanicts']
,	['Ki,Benjamin','Bennythejet16']
,	['M,Anisha Lee','AwkwardPossum']
,	['M,Marc','***']
,	['M,Gavin ','Gavin-Mulderig']
,	['M O,Osvaldo','Osvaldoolivera']
,	['N,Preston ','cplusplusnewb']
,	['P,Tyler ','IrishPotato101']
,	['R,Alejandro','***']
,	['R,Shawn Eugene','ShawnR7305']
,	['T,Axel','Axel-2002']
,	['V,Juan','ThatGuyJuan']
,	['-','-']
,	['A,Noor','NoorAlrubai']
,	['A,Gerardo ','GerardoAmezcua092']
,	['C,Caelan ','***']
,	['F,Caleb ','Calebpro22']
,	['G,Julia','***']
,	['H,Seth','***']
,	['L,Ian Marco','supernaiian']
,	['M,Cian C','StrawberryIdiot']
,	['M,Caleb Thomas','Warghost13']
,	['P,Jhonathan','***']
,	['S,Cassandra','***']
,	['S,Adam ','Bouncyskoda']
,	['S,Taj','taj-s']
,	['S,Melisa','***']
,	['T,Tristin ','fruztalprojects']
,	['W,Levi ','MagickalWiz']
]
	for n in range (0,len(users)):
		a = users[n]
		#b = string_concat_io(a)
		print(a)

	print("\n\n * * * * * * * * \n\n")
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_repos(a)
		print(b)

if __name__ == '__main__':
    main()

'''
[['Maffia, Anisha Lee','AwkwardPossum']
,['Melendez, Marcelo ','***']
,['Mulderig, Gavin ','Gavin-Mulderig']
,['Munoz Olivera, Jose Osvaldo','Osvaldoolivera']
,['Norskog, Preston ','cplusplusnewb']
,['Poteet, Tyler ','IrishPotato101']
,['Rebolledo Torres, Alejandro','***']
,['Rogers, Shawn Eugene','ShawnR7305']
,['Telles, Axel','Axel-2002']
,['Valle,Juan','ThatGuyJuan']
,['-','-']
,['Al Rubai, Noor Haqui Hussein',' NoorAlrubai']
,['Amezcua, Gerardo ','GerardoAmezcua092']
,['Chastain, Caelan ','***']
,['Ferguson, Caleb ','Calebpro22']
,['Gruse,Julia','***']
,['Hadley, Seth','***']
,['Luna Quiroz, Ian Marco','supernaiian']
,['McConn, Cian C','StrawberryIdiot']
,['Moore, Caleb Thomas','Warghost13']
,['Padron, Jhonathan Atzietl','***']
,['Santos, Cassandra Melissa','***']
,['Skoda, Adam ','Bouncyskoda']
,['Sohi, Taj','taj-s']
,['Suljovic, Melisa','***']
,['Torres, Tristin ','fruztalprojects']
,['Wood, Levi ','MagickalWiz']




'Aguilar, Ulises','ulises-aguilar'
'Alcalan, Miguel A','MiguelAlcalan2020'
'Benner, Christopher Logan','Logan-Benner'
'Brogan, Daniel S','danielbrogan26'
'DiCero, Andrew James','DemonDrew0508'
'Katz, Austin','jkiik'
'Kern, Ian Gerald','kernelpanicts'
'Kilgore, Benjamin','Bennythejet16'
'Maffia, Anisha Lee','AwkwardPossum'
'Melendez, Marcelo A','***'
'Mulderig, Gavin J','Gavin-Mulderig'
'Munoz Olivera, Jose Osvaldo','Osvaldoolivera'
'Norskog, Preston L','cplusplusnewb'
'Poteet, Tyler J','IrishPotato101'
'Rebolledo Torres, Alejandro','***'
'Rogers, Shawn Eugene','ShawnR7305'
'Telles, Axel','Axel-2002'
'Valle,Juan','ThatGuyJuan'
'-','-'
'Al Rubai, Noor Haqui Hussein',' NoorAlrubai'
'Amezcua, Gerardo D','GerardoAmezcua092'
'Chastain, Caelan B','***'
'Ferguson, Caleb T','Calebpro22'
'Gruse,Julia','***'
'Hadley, Seth','***'
'Luna Quiroz, Ian Marco','supernaiian'
'McConn, Cian C','StrawberryIdiot'
'Moore, Caleb Thomas','Warghost13'
'Padron, Jhonathan Atzietl','***'
'Santos, Cassandra Melissa','***'
'Skoda, Adam B','Bouncyskoda'
'Sohi, Taj','taj-s'
'Suljovic, Melisa','***'
'Torres, Tristin J','fruztalprojects'
'Wood, Levi H','MagickalWiz'


Juan Valle	ThatGuyJuan
Adam Skoda	Bouncyskoda
Benjamin Kilgore	Bennythejet16
Ulises Aguilar	ulises-aguilar
Shawn Rogers	ShawnR7305
Caleb Moore	Warghost13
Austin Katz	jkiik
Cian C McConn	StrawberryIdiot
Jose Osvaldo Munoz Olivera	Osvaldoolivera
Axel Telles Cervantes	Axel-2002
Levi Wood (MagickalWiz)	MagickalWiz
Daniel Brogan	danielbrogan26
Taj Sohi	taj-s
Tyler James Poteet	IrishPotato101
Christopher Logan Benner	Logan-Benner
Anisha Maffia	AwkwardPossum
Benjamin Kilgore	Bennythejet16
Andrew James DiCero Jr 	DemonDrew0508
Caleb T Ferguson	Calebpro22
Miguel Alcalan	MiguelAlcalan2020
Noor Al Rubai	 NoorAlrubai
Gerardo Amezcua	GerardoAmezcua092
preston norskog	cplusplusnewb
Ian Luna Quiroz	supernaiian
Juan Valle	ThatGuyJuan
Ian Gerald Kern	kernelpanicts
Tristin Torres	fruztalprojects
Miguel Alcalan	MiguelAlcalan2020
Gavin Mulderig	Gavin-Mulderig



icebowl
ThatGuyJuan
Bouncyskoda
Bennythejet16
ulises-aguilar
ShawnR7305
Warghost13
jkiik
StrawberryIdiot
Osvaldoolivera
Axel-2002
MagickalWiz
danielbrogan26
taj-s
IrishPotato101
Logan-Benner
AwkwardPossum
Bennythejet16
DemonDrew0508
Calebpro22
MiguelAlcalan2020
NoorAlrubai
GerardoAmezcua092
cplusplusnewb
'''



'''
    users = ("Masoninja", "ElonMusk2018", "Delgado0001","junior-delatorre","JorgeFernandezJr",
            "Braeden42","Ngrade7","EvanIsakson00","Erduin17","NoahMcGe",
            "tylersul02","esperanzavillasenor","42silasweis","ObadiahBorms02",
            "S3thBr0wn","devonchen42","bcooper58","nathanhigley","EvanRichard2",
            "Aces14","bulletghost1","jadenbrewer","InfiniteGeo","masonguinn",
            "pedro-1970","HavensRyan","Jony-5","CyberCrypter2810","cmtthomas",
            "Treyster509v2","Bryan1998","trihstonmadden")
    for n in range (0,len(users)):
        a = users[n]
        b = string_concat(a)
        print(b)
'''


"""
# b = '"' + a + '"'
b = b + "target ="+'"'+"blank"+'"'+">"+a"</a><br />"
<a href = "https://github.com/Masoninja?tab=repositories" class = "link" target = "_blank"> Mason	A </a><br />
AMPM  = ("Masoninja", "ElonMusk2018", "Delgado0001","junior-delatorre","JorgeFernandezJr",
        "Braeden42","Ngrade7","EvanIsakson00","Erduin17","NoahMcGe",
        "tylersul02","esperanzavillasenor","42silasweis","ObadiahBorms02",
        "S3thBr0wn","devonchen42","bcooper58","nathanhigley","EvanRichard2",
        "Aces14","bulletghost1","jadenbrewer","InfiniteGeo","masonguinn",
        "pedro-1970","HavensRyan","Jony-5","CyberCrypter2810","cmtthomas",
        "Treyster509v2","Bryan1998","trihstonmadden")
"""
