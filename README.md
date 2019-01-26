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

## How it works:

First of all, we perform `Name Entity (NE)` on each sentence using `NLTK`, but `NE` done by `NLTK` is not perfect. Therefore, we wrote our own rules for `(NE)` in our project.
Consider the following sample sentence taken from the `train.tsv` file:

```
Valve Corporation's foundation place is Kirkland, Washington.
``` 
after performing `NE`, we will get `Valve Corporation's` and `Kirkland, Washington`. As these sentences are quite straight forward,  so we will assume the first as Subject and the sencond as Object. Now, the remaining tokens are `place, is` and here you can easily see that after removing the stop word `is`, we are left with `place`, and so we can assume it to be the Predicate.

Now we take the Subject and search its corresponding Wikipedia page. Once we have the page, we seach our Object in that respective page. If the search result returns `true`, we consider our fact as **TRUE** and if the search result returns `false`, we consider our fact as **FALSE**.

Since the approach is Naive, one can simply question; why don't we use predicate to check our facts?

Each fact or sentence can be written in multiple ways.

Example:

**Quaid-e-Azam** was **born** in **Pakistan**  (true fact)

this sentence can also be written as:

The **Birth place** of **Quaid-e-Azam** is **Pakistan** (true fact)

These both sentences will return `True` in our project regardless of the Predicate.

Secondly, out project gives 65% of precision which is greater than the required percentage for the mini project.

Following are the sample run of the trained data set.

##### Data that produces FALSE - POSITVE result
1. **Quaid-e-Azam** was **born** in **India**
1. **Ansoo Lake** is **situated** in **Sindh province**
1. **Quetta** is the **capital** city of **Pakistan**

##### Data that produces TRUE - NEGATIVE result
1. **Microsoft** was not **founded** by **Steve Jobs**
1. **University of Paderborn** is not **located** in **Munich**
1. **Microsoft** does not **own** the **Skype** company.

