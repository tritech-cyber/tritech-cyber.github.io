def string_concat(a):
    b = "<a href = "+'"'+"https://"
    b = b + a + ".github.io"
    b = b +'"' + " target ="+ '"'+"_blank"+'"'+">"+a+"</a><br />"
    return b

if __name__ == '__main__':
	users = ('ulises-aguilar','ezekielborms','dunham543','evanharvill','bennythejet1',    
				'evanharvill','thormiller','CPlusPlusNewb','alejandrorebolledo','Masoninja',  'logan-benner',     
				'NoahMcGe','42silasweis','havensryan','Jacheson32','liluda','ChefboyRD',     
				'bluehorse07','mini-ray','hittjeremy', 'supernaiian', 'hondo2121',     
				'petergrutherford','jskye3293',   
				'piluvr','magickalwiz', 'spacewaster','jony-5','bulletghost1','CyberCrypter2810')
				
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat(a)
		print(b)



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
