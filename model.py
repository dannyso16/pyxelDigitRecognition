import numpy as np
import pickle
from PIL import Image
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.externals import joblib

def train():
    digits = load_digits()
    X = digits.data
    y = digits.target

    # print(X.shape) # (1797, 64)
    # print(y.shape) # (1797,)

    X_train,X_test,y_train,y_test = train_test_split(X, y)

    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    # print(knn.score(X_test, y_test)) # 0.98

    # save model
    with open('knn_digit.pkl', 'wb') as f:
        pickle.dump(knn, f)


def load_predict() -> int:

    with open('knn_digit.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    img = Image.open("images/screen_shot.png")
    img = img.convert('L') # conver (r,g,b) to 0-255
    img = (255 - np.array(img))//16 + 1 # convert to 0-15
    img = img.reshape(1, 64)

    pred = loaded_model.predict(img)[0] # np.array to int
    # print("PREDICT: ", pred)
    return pred


# === main ====-
# train()
# load_predict()
