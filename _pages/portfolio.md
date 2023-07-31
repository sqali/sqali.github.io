---
permalink: /portfolio/
title: "Portfolio"
toc: true
toc_label: "Table of Contents"
toc_icon: "bookmark"

---
*Updated: 08/12/2020*

## 🤖 Computer Vision
### Object Detection with Detectron2

<img src="https://dl.fbaipublicfiles.com/detectron2/Detectron2-Logo-Horz.png" width="200">

A series of notebooks to dive deep into popular datasets for object detection and learn how to train Detectron2 on custom datasets.

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/sqali/object-detection-detectron2)

- [Notebook 4](https://github.com/sqali/object-detection-detectron2/blob/master/04-train-big.ipynb): Train Detectron2 on Open Images dataset to detect musical instruments.
- [Notebook 5](https://github.com/sqali/object-detection-detectron2/blob/master/05-kaggle-global-wheat-detection.ipynb): Apply Detectron2 on [Kaggle Global Wheat Detection Competition](https://www.kaggle.com/c/global-wheat-detection).

<img src="https://raw.githubusercontent.com/sqali/object-detection-detectron2/master/images/output_04.png" width="580">{: .align-center}


### CS231n: Convolutional Neural Networks for Visual Recognition

This is my complete implementation of assignments and projects in [***CS231n: Convolutional Neural Networks for Visual Recognition***](http://cs231n.stanford.edu/) by Stanford (Spring, 2019). NumPy implementations of forward and backward pass of each layer in a convolutional neural network have given me a deep understanding of how state-of-the-art Computer Vision architectures work under the hood. In addition, I explored the inner beauty of Deep Learning by implementing Style Transfer, Deep Dream, Texture Systhesis in PyTorch and generating new images with GANs.

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/sqali/CS231n-CV)

**Selective Topics:**
- [NumPy Implementations of CNN](https://github.com/sqali/CS231n-CV/blob/master/assignment2/cs231n/layers.py): Fully-connected Layer, Batchnorm, Layernorm, Dropout, Convolution, Maxpool.
- [Image Captioning with LSTMs](https://github.com/sqali/CS231n-CV/blob/master/assignment3/LSTM_Captioning.ipynb)
- [Saliency Maps, Deep Dream, Fooling Images](https://github.com/sqali/CS231n-CV/blob/master/assignment3/NetworkVisualization-PyTorch.ipynb)
- [Style Transfer](https://github.com/sqali/CS231n-CV/blob/master/assignment3/StyleTransfer-PyTorch.ipynb)
- [Generative Adversarial Networks (GANs)](https://github.com/sqali/CS231n-CV/blob/master/assignment3/Generative_Adversarial_Networks_PyTorch.ipynb)


---

## 📈 Data Science
### Credit Risk Prediction Web App

[![Open Web App](https://img.shields.io/badge/Heroku-Open_Web_App-blue?logo=Heroku)](http://credit-risk.herokuapp.com/)
[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-blue?logo=Jupyter)](https://github.com/sqali/credit-risk-prediction/blob/master/documents/Notebook.ipynb)
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/sqali/credit-risk-prediction)

After my team preprocessed a dataset of 10K credit applications and built machine learning models to predict credit default risk, I built an interactive user interface with Streamlit and hosted the web app on Heroku server.

<img src="https://sqali.github.io/minimal-portfolio/images/credit-risk-webapp.png" width="580">{: .align-center}

---
### Kaggle Competition: Predict Ames House Price using Lasso, Ridge, XGBoost and LightGBM

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-blue?logo=Jupyter)](https://sqali.github.io/minimal-portfolio/projects/ames-house-price.html)
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/sqali/kaggle-house-price/blob/master/ames-house-price.ipynb)

I performed comprehensive EDA to understand important variables, handled missing values, outliers, performed feature engineering, and ensembled machine learning models to predict house prices. My best model had Mean Absolute Error (MAE) of 12293.919, ranking **95/15502**, approximately **top 0.6%** in the Kaggle leaderboard.

<img src="https://sqali.github.io/assets/images/portfolio/ames-house-price.jpg" width="580">{: .align-center}


---
### Business Analytics Conference 2018: How is NYC's Government Using Money?

[![Open Research Poster](https://img.shields.io/badge/PDF-Open_Research_Poster-blue?logo=adobe-acrobat-reader&logoColor=white)](https://sqali.github.io/minimal-portfolio/pdf/bac2018.pdf)

In three-month research and a two-day hackathon, I led a team of four students to discover insights from 6 million records of NYC and Boston government spending data sets and won runner-up prize for the best research poster out of 18 participating colleges.

<img src="https://sqali.github.io/assets/images/portfolio/bac2018.JPG" width="580">{: .align-center}


## 🤖 Computer Vision
### Document classification using Convolutional Neural Networks

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/sqali/Applied-AI-Assignments/tree/main/Document%20Classification%20Using%20CNN)

This project entails the development of a Convolutional Neural Network (CNN) for the task of document classification. I worked with a dataset of text documents, utilizing the filenames for class label extraction. The challenge involves preprocessing the text data, designing and training a CNN model for classification, and evaluating its performance on this multi-class text categorization task.

<img src="https://sqali.github.io/assets/images/portfolio/1_BEaZkpZJ4mFR-i2U4VOXsA.png" width="580">{: .align-center}

## 🎵 Automatic Speech Recognition
### Spoken Digit Recognition using LSTM

The project revolves around Spoken Digit Recognition. The task involves reading and preprocessing a dataset of speech signals, with the goal of predicting the spoken digit. The project requires the use of LSTM networks for training both raw data and spectrogram-converted data. An additional task is to create augmented data and repeat the training process. The work should follow the provided instructions and graders, and return outputs in the specified formats.

<img src="https://sqali.github.io/assets/images/portfolio/spoken_digit_image.png" width="580">{: .align-center}

