#Note1 2am 23 June 2024
I just did the whole the data preprocessing. I started like an hour ago ;-;
Tmr ima try to write all the object classes and functions in this readme file
lol gn

#Note2 3:55pm 24June2024 - 
 Welp Ima try to write what all I did

PART1 - HANDLE MISSING VALUES 
To handle missing values we need to use the sklearn library specifically SimpleImputer from sklearn.impute
Firt we need to initialise an object of the simple imputer class
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
in this line I made an object of the class Simple Imputer and in the constructors I put missing values as np.nan and strategy to mean.


PART2.1 - COLUMN TRANSFORMATION
So in our Data.csv file we can see that in the whole data we can string and int datatypes we need only int datatypes, I first started with the country column. It has 3 counties only France Germany and Spain, best way is to convert that string data into binary vector like 100 for Germany 010 for France and 001 for Spain.
We need to use modules from the sklearn library to be able to do that
Column transformer from sklearn.compose and,
OneHotEncoder from sklearn.preprocessing
we need to make an object of the class Comlumn transformer
ct = ColumnTransformer(transform = (["encoder", OneHotEncoder(), [0]), remainder = "passthrough")
x = np.array(ct.fit_transform(x))

PART 2.2 - LABEL ENCODING
Now we solved the problem of country but we still need to fix out target values
we can use the LablelEncoder from sklearn.preprocessing
y = LabelEncoder().fit_transform(y)

PART 3 - TRAINING TEST SPLIT
We have now preprocessed the entire data for further analysis, we need to split the data into test and train set so that we can train the data based on the training set and match the accuracy of the model with the test set.
To split the data we can use Train_Test_Split from sklearn.selection.
x_train, x_test, y_train, y_test = Train_Test_Split(x,y, test_size = 0.2, random_state = 1)
in the above line of code I have used the parameter Random_state cus in this project i want the data to be same for the entire project.

PART 4 - FEATURE SCALING
We use feature scaling to scale the values to normalise the range of independent variables.
There are 2 main ways to that 


whew Done :D its 4:35 rn so it took 40 mins xd
1)Normalisation - In normalisation the formula is (x - min(x))/(max(x) - min(x)) the value of x stays between 0 and 1.
2)Standardisation - In standardisation the formula is (x - mean(x))/standard_deviation(x) the value stays between -3 to 3
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])
