def string_concat_repos(a):
    b = "<a href = "+'"'+"https://github.com/"
    b = b + a
    b = b +"?tab=repositories\" target =\"_blank\" >"+a+"</a><br />"
    # b = b +"?tab=repositories\" target ="+ '"'+"_blank"+'"'+">"+a+"</a><br />"
    return b

def string_concat_io(a):
    b = "<a href = "+'"'+"https://"
    b = b + a + ".github.io"
    b = b +'"' + " target ="+ '"'+"_blank"+'"'+">"+a+"</a><br />"
    return b

def main():
	users = ('magickalwiz','ulises-aguilar','bennythejet16', 'cplusplusnewb','alejandrorebolledo',  'logan-benner',
    			'mini-ray', 'supernaiian','thatguyjuan','bouncyskoda','shawnr7305','jkiik',
                'strawberryidiot','osvaldoolivera','axel-2002','danielbrogan26','taj-s','irishpotato101','awkwardpossum',
                'DemonDrew0508')

	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_io(a)
		print(b)

	print("\n\n * * * * * * * * \n\n")
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_repos(a)
		print(b)

if __name__ == '__main__':
    main()

'''
http://github.com/icebowl
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
