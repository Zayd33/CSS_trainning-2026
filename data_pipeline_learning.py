# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 09:58:02 2026

@author: ATMOSPHERIC SERVICE
Data Pipeline for ETL
"""
# Import Pandas
import pandas as pd


# Ingest these datasets into memory using read_csv and save as apps and reviews variable
apps = pd.read_csv("apps_data.csv")
reviews = pd.read_csv("review_data.csv")

# Take peak at the two data sets with print function or view in variable explorer
#print(reviews)


# View the columns, shape and data types of the data sets
print(apps.columns)
print(apps.shape)
print(apps.dtypes)

"""
The most common data pipeline structure consits of extracting, transforming, and loading data - ETL

step 1 - write out the 3 functions
- extract
- transform
- load
"""



# Extract Function - getting from data source, loading in memory
def extract(file_path):
    
    # Read the file into memory
    df = pd.read_csv(file_path)
    
    # Now, print the details about the file    
    print(df.shape)
    print(df.dtypes)
    
    # Print the type of each column
    print(df.columns)
    
    # Finally, print a message before returning the DataFrame
    print(f"{file_path} dataframe has been loaded")
    return df


# Call the function (create apps_data and reviews_data)
apps_data = extract("apps_data.csv")
reviews_data = extract("review_data.csv")


# Take a peek at one of the DataFrames
print(f"Resuts of apps_data below: {apps_data}")

# Transform Function
def transform(apps,reviews,category,min_rating,min_reviews):

    # Print statement for observability
    print(f"Transform dataset: Category - {category}, min_rating - {min_rating}, min_reviews - {min_reviews}")
    
    # Drop any duplicates from both DataFrames (also have the option to do this in-place)
    reviews.drop_duplicates(inplace=True)
    apps.drop_duplicates(subset=["App"],inplace=True)
    
    # Find all of the apps and reviews in the food and drink category    
    # Filter apps by category using query
    apps.query("Category == @category",inplace=True)
    print("------------------------")
    print(apps)
    
    # Filter reviews for matching apps
    # keeps only the rows in reviews where reviews App column value
    # matches with App name in apps in dataframe
    reviews.query("App in @apps.App", inplace=True)
    print("------------------------")
     
    
    # Keep only relevant review columns
    reviews = reviews[["App", "Sentiment_Polarity"]]
    print(reviews)  
    
    # Aggregate review sentiments
    aggregated_reviews= reviews.groupby("App").mean()
    
    # Merge reviews back into apps
    apps = apps.join(aggregated_reviews,on="App",how="left")
    
    # Keep only needed columns apps
    apps = apps[["Apps", "Rating","Reviews","Installs","Sentiment_Polarity"]] 
    
    
    # Convert apps "Reviews" to integer
    apps["Reviews"] = apps["Reviews"].astype("int32")
    
    # Filter based on rating and review count
    #min_rating = 4.0
    apps.query("Rating > @min_rating and Reviews >= @min_reviews", inplace = True)

    # Reset Index
   apps.reset_index(drop=True, inplace=True)
    # Sort the top apps by rating and review
    ///
    
    # Persist this DataFrame as top_apps.csv file
    
    # Print what has happened so far
    
    # Return the transformed DataFrame
    top_apps = ""
    return top_apps
    
# Call the function
top_apps_data = transform(apps_data, reviews_data, "FOOD_AND_DRINK", 4.0, 1000)

# Show the data

# Import sqlite

# Load Function

    # Create a connection object
    
    # Write the data to the specified table (table_name)
    
    # Read the data, and return the result (it is to be used)
    
    # Add try/except to handle error handling and assert to check for conditions
    
# Call the function
    
