from flask import Flask, request, jsonify
import csv
import pandas as pd

allArticles= []
likedArticles = []
unlikedArticles = []

with open('articles.csv', encoding = 'utf8') as f:
    reader = csv.reader(f)

    df = list(reader)
    allArticles = df[1:]

app = Flask(__name__)

@app.route('/get-article')

def getArticle():
    return jsonify({
        'data': allArticles[1:],
        'message': 'success'
    })

@app.route('/liked-articles', methods = ['POST'])

def likedArtilce():
    article = allArticles[0]
    likedArticles.append(article)
    allArticles.pop(0)

    return jsonify({
        'message': 'success'
    })

@app.route('/unliked-articles', methods = ['POST'])

def unlikedArticle():
    article = allArticles[0]
    unlikedArticles.append(article)
    allArticles.pop(0)

    return jsonify({
        'message': 'success'
    })

if(__name__ == '__main__'):
    app.run()
