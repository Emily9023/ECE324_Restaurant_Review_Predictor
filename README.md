# ECE324 Restaurant Review Predictor
Goal: Predict Yelp star ratings based on features about a restaurant. 
# Step 1: Data Collection
In the Data Collection directory, the yelp_scraper.py file was used to scrape Yelp. This data is included in the JSON_Files Directory (along with a collab file that combines the data into a single JSON file). 

The raw data from web scraping is compiled in totalRawData.json within the JSON_Files directory. 

There is an Archive folder with documenting our previous attempt at using the Google Reviews API (and the data collected through that method). 
# Step 2: Data Pre Processing
In the Data Pre Processing directory, there is an ipynb notebook called Data Cleaning. The cleaned data is stored in the cleanedData.csv file. 

We added word embedding vectors for the cuisine feature later on. This is shown in the Data Pre Processing directory, in the Data Cleaning with Cuisine Vec notebook. This final cleaned data is stored in the cleanedData_cuisinevec.csv file. 
# Step 3: Models
In the Models directory, at first we created 3 models (LinearLogisticRegression and 2 Boosting Models).

Next we created two neural network models. Neural Net.ipynb contains 1 basic neural network model and 1 stacked neural network model. 
# Step 4: Generate Coefficients Table
CalculateCoefficients.ipynb contains the simple neural network that is used to calculate the correlation factors between cities.  




