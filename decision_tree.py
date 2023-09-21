#-------------------------------------------------------------------------
# AUTHOR: Rebecca Glatts
# FILENAME: decision_tree.py
# SPECIFICATION: Creating a decision tree from a csv file with features and classes
# FOR: CS 4210- Assignment #1
# TIME SPENT: 4 hours (total assignment)
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         #print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
feature_to_value = { 'Young' : 1, 'Presbyopic' : 2, 'Prepresbyopic' : 3, 
                     'Myope' : 4, 'Hypermetrope' : 5,
                     'No' : 6, 'Yes' : 7, 
                     'Normal': 8, 'Reduced' : 9}

for row in db:
  a = []
  for i in range (4):
    a.append(feature_to_value.get(row[i]))
  X.append(a)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
class_to_value = {'Yes' : 1, 'No' : 2}
for row in db:
   Y.append(class_to_value.get(row[4]))

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
