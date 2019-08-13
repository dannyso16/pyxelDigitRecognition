# pyxelDigitRecognition

## Handwriting digit recognition implemented in [Pyxel](https://github.com/kitao/pyxel) and [sklearn](https://scikit-learn.org/stable/)!

![play](<https://github.com/dannyso16/pyxelDigitRecognition/blob/master/images/play.gif>)

You can use this program as a cheap painting software.

![paint](<https://github.com/dannyso16/pyxelDigitRecognition/blob/master/images/paint.gif>)



## Features

- Drag a mouse : draw a line
- `s`: Recognize what number you write
- `Delete`: Clear the canvas 


## Installation

1. Install Python3 and Pyxel.
2. Clone or copy this repository.
3. `python main.py` at the command line.


## Train your model

A trained model is pickled as `knn_digit.pkl`.
The Algorithm is 'K nearest neightbor', and dataset is [Digit dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html).

You can retrain with `model.py`