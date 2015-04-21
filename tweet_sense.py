from __future__ import division
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import os
import sys
import pickle

#scriptpath = "C:\Users\Brian\Desktop\CodeForGit\Twitter"
#sys.path.append(os.path.abspath(scriptpath))

from MovieData2 import MovieData
#from MovieReviews3 import CreateX, ProcessX, Threshold, sigmoid
#from collections import Counter
#import TwitterSearch as TSch

app = Flask(__name__)

MovieData = np.array(MovieData)
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM qwertyuiopasdfghjklzxcvbnm'

def fontsize(len):
	if len <= 23: return "font-size:16px"
	if len <= 26: return "font-size:15px"
	if len <= 29: return "font-size:14px"
	if len <= 32: return "font-size:13px"
	if len <= 35: return "font-size:12px"
	if len <= 38: return "font-size:11px"
	else: return "font-size:10px"

MaxRevToCheck = 1000
MaxRevToPrint = 20
rows = 5
names = [i[0:-5] for i in MovieData[:,0]]
ratings = [str(int(round(float(i)*100)))+"%" for i in MovieData[:,1]]
fontsizes = [fontsize(len(i)) for i in names]

thinnames = ["".join([j for j in i if j not in [":","'"]]) for i in names]

images = ["".join(i.split(" "))+ ".jpg" for i in thinnames]
#images = ['http://127.0.0.1:5000/static/images/' + i for i in images]
images = ['static/images/' + i for i in images]
while len(images)%rows !=0:
	#images.append('http://127.0.0.1:5000/static/images/white_wall.png')
	images.append('static/images/white_wall2.jpg')
	names.append('')
	ratings.append('')
	fontsizes.append('font-size:1px')
images = np.array(images)
names = np.array(names)
ratings = np.array(ratings)
fontsizes = np.array(fontsizes)
images = (images.reshape((len(images)/rows,rows))).T
names = (names.reshape((len(names)/rows,rows))).T
ratings = (ratings.reshape((len(ratings)/rows,rows))).T
fontsizes = (fontsizes.reshape((len(fontsizes)/rows,rows))).T

getimage = dict(zip(names.T.flatten(), images.T.flatten()))
getrating = dict(zip(names.T.flatten(), ratings.T.flatten()))
#getfilename = dict(zip(names.T.flatten(), ["C:\\Users\\Brian\\Desktop\\CodeForGit\\Twitter\\MyReviews2\\" + i for i in MovieData[:,0]] ))

getfilename = dict(zip(names.T.flatten(), ['static/' + i for i in MovieData[:,0]] ))


###Make Tables of Pos and Neg Tweets:###
#ThetaRes = pickle.load(open(r"C:\Users\Brian\Desktop\CodeForGit\Twitter\ThetaRes0326", "rU"))
#FeatureWords = pickle.load(open(r"C:\Users\Brian\Desktop\CodeForGit\Twitter\FeatureWords0326", "rU"))
#featureMeans = pickle.load(open(r"C:\Users\Brian\Desktop\CodeForGit\Twitter\featureMeans0326", "rU"))
#featureSTD = pickle.load(open(r"C:\Users\Brian\Desktop\CodeForGit\Twitter\featureSTD0326", "rU"))


@app.route('/')
def mainpage():
    return render_template('mainpage.html', images = images, names = names, ratings = ratings, fontsizes = fontsizes)

@app.route('/<movie>')
def moviepage(movie):
        
	PosRev = pickle.load(open(getfilename[movie] + " NoLpos", "rU")) 
	
	NegRev = pickle.load(open(getfilename[movie] + " NoLneg", "rU"))
	
	
	return render_template('moviepage.html', image = getimage[movie], name = movie, rating = getrating[movie], PosRev = PosRev, NegRev = NegRev)

@app.route('/Methodology')
def methodpage():
        return render_template('methodpage.html')

@app.route('/Validation')
def validpage():
        return render_template('validpage.html')

	
#@app.route('/signup', methods = ['POST'])
#def signup():
#    email = request.form['email']
#    email_addresses.append(email)
#    print("The email address is '" + email + "'")
#    return redirect('/')

#@app.route('/emails.html')
#def emails():
#    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == "__main__":
    app.run(debug = False)
