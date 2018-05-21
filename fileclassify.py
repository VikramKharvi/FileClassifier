import shutil, os, sys
from flask import Flask,render_template,redirect, url_for, request
import nltk
from textblob import TextBlob
from rake_nltk import Rake
xt=''
def location(loc,fol):

	r = Rake()
	a=[]
	b=[]

	with open (loc, "r") as myfile:
		fs=myfile.readlines()
	txt=fs[0]

	#blob
	blob = TextBlob(txt)
	x=(blob.noun_phrases)
	a=list(x)

	#Rake
	r.extract_keywords_from_text(txt)
	c=r.get_ranked_phrases()
	b=list(c)

	s=[]
	f1=open("a.txt","w+")
	for item in a:
		f1.write("%s\n" % item)
	f1.close()

	f2=open("b.txt","w+")
	for item in b:
		f2.write("%s\n" % item)
	f2.close()

	with open('b.txt') as f2:
		lines1 = f2.read().splitlines()

	with open('a.txt') as f1:
		lines2 = f1.read().splitlines()

	for element in lines1:
		if element in lines2:
			s.append(element)
	global xt
	xt=s[0]
	tds=str(fol)
	fds=tds[1:-1]
	ata = fds+'/'+xt
	print(ata)
	aa=ata[1:]
	print(aa)
	if not os.path.exists(aa):
		os.makedirs(aa)
	shutil.copy('/root/FSProject/input.txt', aa)
	return xt


#FLASK
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_name():
	if request.method == 'POST':
   		loca = request.form['location']
   		fold = request.form['folder']
   		loc=loca.encode('ascii','ignore')
   		fol=fold.encode('ascii','ignore')
   		location(loc,fol)
	return render_template('index.html', name = "Done",nlp=xt)

if __name__ == '__main__':
   app.run(debug = True)






