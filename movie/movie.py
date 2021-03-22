import pandas as pd
import matplotlib.pyplot as plt

data = 'movies.csv'
dataset = pd.read_csv(data)
#print(dataset.shape)
#print(dataset.head(10))

from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
dataset.genres = dataset.genres.str.split('|')
#dataset = explode(dataset, ['genres'])
newdataset = mlb.fit_transform(dataset.genres)
#print(newdataset)
#print(mlb.classes_)
#print(dataset.head(10))
#print(dataset.describe())
afterExpandingGenre = pd.DataFrame(data=newdataset, columns=mlb.classes_)
#print(afterExpandingGenre)
combinedBeforeRating = pd.concat([dataset,afterExpandingGenre],axis = 1,sort = False )
#print(combinedBeforeRating.head(50))
combinedAfterRating = pd.read_csv('ratings.csv')
#combinedAfterRating = combinedAfterRating.sort_values('movieId')
#print(combinedAfterRating.head(50))
combinedBeforeRating = pd.merge(combinedBeforeRating,combinedAfterRating,on='movieId')
#combinedBeforeRating = combinedBeforeRating.append(pd.read_csv('ratings.csv'),sort = False)
combinedBeforeRating = combinedBeforeRating.groupby('movieId').mean().reset_index()
combinedBeforeRating = pd.merge(dataset,combinedBeforeRating,on='movieId')
combinedBeforeRating = combinedBeforeRating.drop(columns = ['genres','userId','timestamp'])
#pd.DataFrame(data=newdataset, columns=mlb.classes_)
#import sys
#sys.stdout = open("f1.txt", "w+")
#print(combinedBeforeRating.head(5))
#combinedBeforeRating.to_csv('nnnnnnnnnnnnn.csv')

#from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


features = combinedBeforeRating.drop(columns = ['rating','movieId','title']).values
#print(features)
lables = combinedBeforeRating.rating.values
for i in range(len(lables)):
    lables[i] = int(lables[i].__round__(2))
    if lables[i]<3:
        lables[i] = 0
    else:
        lables[i] = 1
#print(lables)

features_train,features_test,lables_train,lables_test = train_test_split(features,lables,test_size = 0.8)

my_classifier = KNeighborsClassifier()
my_classifier.fit(features_train,lables_train)
prediction = my_classifier.predict(features_test)
print(my_classifier.score(features_test, lables_test)*100)
#print(prediction)
"""
from pandas.plotting import scatter_matrix
scatter_matrix(dataset)
plt.show()"""
