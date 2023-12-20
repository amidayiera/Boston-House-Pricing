# Boston-House-Pricing


## Software and Tools Requirements

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [HerokuAccount](https://heroku.com)
4. [Git CLI](https://cli.github.com/)
 

## Overview
[The Boston Housing Dataset](https://fairlearn.org/main/user_guide/datasets/boston_housing_data.html) is a well known dataset in the field of machine learning, used for regression analysis. The goal of this project is to predict the selling price of a house in the Boston (MA) area. 

### Data Features
- Variables - There are 13 attributes in each case of the dataset. They are:  
  `CRIM` - per capita crime rate by town  
  `ZN` - proportion of residential land zoned for lots over 25,000 sq.ft.  
  `INDUS` - proportion of non-retail business acres per town.  
  `CHAS` - Charles River dummy variable (1 if tract bounds river; 0 otherwise)  
  `NOX` - nitric oxides concentration (parts per 10 million)  
  `RM` - average number of rooms per dwelling  
  `AGE` - proportion of owner-occupied units built prior to 1940  
  `DIS` - weighted distances to five Boston employment centres  
  `RAD` - index of accessibility to radial highways  
  `TAX` - full-value property-tax rate per $10,000  
  `PTRATIO` - pupil-teacher ratio by town  
  `B` - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town  
  `LSTAT` - % lower status of the population  

## Create a new environment

```
conda create -p venv python==3.7 -y
``` 
## Installation of libraries

```
pip3 install -r requirements.txt
```

## Launch and Run Flask App
```
python app.py
```
The server should be running on `http://localhost:5000/`</s>

## License

[Apache License](http://www.apache.org/licenses/LICENSE-2.0)


### Disclaimer: 
The Boston Housing dataset is one of the datasets currently callable in fairlearn.datasets module. In the past, it has commonly been used for benchmarking in popular machine learning libraries, including scikit-learn and OpenML. 

However, as the machine learning community has developed awareness about fairness issues with popular benchmarking datasets, the Boston Housing data has been phased out of many libraries.

We migrated the dataset to Fairlearn after it was phased out of scikit-learn in June 2020. The dataset remains in Fairlearn as an example of how systemic racism can occur in data and to show the effects of Fairlearn’s unfairness assessment and mitigation tools on real, problematic data.

We also think this dataset provides an interesting case study of how fairness is fundamentally a socio-technical issue by exploring how societal biases manifest in data in ways that can’t simply be fixed with technical mitigation approaches (although the harms they engender may be mitigated)