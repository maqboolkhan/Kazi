Kazi
====
The naive fact checker based on Wikipedia. Using `NLTK` and `Wekipedia` Python packages.

## Team Name:
Faktenprüfung

## Team Members:
Name | Matriculation Number
------------ | -------------
Maqbool Ur Rahim Khan | 6843364
Ali Azmi | 6844310 
Muhammad Hamza | 6845542

## Setup Guide:

### Requirements:
* Python3
* Pip3 

```
python3 setup.py
```

##### Attention: 
Our setup uses Python3 which is aliased as `python3`. If Python 3 command is not available as `python3` then `setup.py` won't work. 

## Train:
In order to execute the training data set, please run the following command.
```
Python3 main.py train
```

## Test:
In order to execute `test`, please run the following command.
```
python3 main.py test
```
##### Note: 
Please make sure that the spellings of *train* and *test* are correct.

## How it works
Following are the sample run of the trained data set.

##### Data that produces FALSE - POSITVE result
1. **Quaid-e-Azam** was **born** in **India**
1. **Ansoo Lake** is **situated** in **Sindh province**
1. **Quetta** is the **capital** city of **Pakistan**

##### Data that produces TRUE - NEGATIVE result
1. **Microsoft** was not **founded** by **Steve Jobs**
1. **University of Paderborn** is not **located** in **Munich**
1. **Microsoft** does not **own** the **Skype** company.

