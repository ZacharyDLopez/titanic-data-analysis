import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    passenger_data = pd.read_csv('titanic.csv')
    return passenger_data

def data_cleaning(passenger_data):
    print("Data Cleaning W/ Dropna: \n")
    
    rows_before = len(passenger_data)
    print("Obervations before removing missing values: ")
    print(passenger_data)

    passenger_data.dropna(inplace=True)
    
    print("\nObervations after removing missing values: ")
    print(passenger_data)
    
    print("\nNumber of rows removed: ", rows_before - len(passenger_data))

def data_cleaning_with_drop(passenger_data):
    print("\nData Cleaning W/ Drop: ")

    columns_before = len(passenger_data.columns)
    rows_before = len(passenger_data)

    print("\nObervations before removing missing values: ")
    print(passenger_data)

    print("\nObervations after removing missing values in the deck column: ")
    passenger_data.drop(columns=['deck'],inplace=True)
    print(passenger_data)

    print("\nObervations after removing missing values in all rows: ")
    passenger_data.dropna(inplace=True)

    print(passenger_data)
    print("\nNumber of columns removed: ", columns_before - len(passenger_data.columns))
    print("\nNumber of rows removed: ", rows_before - len(passenger_data))

    return passenger_data


def histogram_of_fare_before_removing_extremes(passenger_data):
    plt.hist(passenger_data['fare'],density=True, bins=30)
    plt.ylabel('Probability')
    plt.xlabel('Fare')
    plt.title('Histogram of Fare Before Removing Extremes')
    plt.show()

def filtered_data_by_std(passenger_data):
    print("\nThe Standard Deviation and Mean of Fare: ")

    standard_deviation = passenger_data['fare'].std()
    print("\nStandard Deviation of Fare: ", standard_deviation, "/",standard_deviation.round(2))

    print()

    mean = passenger_data['fare'].mean()
    print("Mean of Fare: ", mean ,"/",mean.round(2))
    

    print("\nFilter out observations with fare greater than or less than the standard deviation: ")

    print("\nObservations with fare greater than the standard deviation: ")
    filtered_data_above_std = passenger_data.loc[passenger_data['fare'] > standard_deviation]
    print(filtered_data_above_std)

    print("\nObservations with fare less than the standard deviation: ")
    filtered_data_below_std = passenger_data.loc[passenger_data['fare'] < standard_deviation]
    print(filtered_data_below_std)

    return filtered_data_above_std, filtered_data_below_std

def histogram_of_fare_after_removing_extremes(passenger_data):
    filtered_data_above_std, filtered_data_below_std = filtered_data_by_std(passenger_data)

    plt.hist(filtered_data_above_std['fare'],density=True, bins=30)
    plt.ylabel('Probability')
    plt.xlabel('Fare')
    plt.title('Histogram of Fare After Removing Extremes Above Standard Deviation')
    plt.show()

    plt.hist(filtered_data_below_std['fare'],density=True, bins=30)
    plt.ylabel('Probability')
    plt.xlabel('Fare')
    plt.title('Histogram of Fare After Removing Extremes Below Standard Deviation')
    plt.show()

def boxplot_of_fare(passenger_data):
    plt.boxplot(passenger_data['fare'])
    plt.ylabel('Fare')
    plt.title('Boxplot of Fare')
    plt.show()


def remove_outliers_fare_and_age(passenger_data):
    fare_Q3 = passenger_data['fare'].quantile(0.75)
    fare_Q1 = passenger_data['fare'].quantile(0.25)

    IQR = fare_Q3 - fare_Q1

    lower_bound_fare = fare_Q1 - 1.5 * IQR
    upper_bound_fare = fare_Q3 + 1.5 * IQR

    age_Q3 = passenger_data['age'].quantile(0.75)
    age_Q1 = passenger_data['age'].quantile(0.25)

    IQR = age_Q3 - age_Q1

    lower_bound_age = age_Q1 - 1.5 * IQR
    upper_bound_age = age_Q3 + 1.5 * IQR

    for index, row in passenger_data.iterrows():
        if row['fare'] < lower_bound_fare or row['fare'] > upper_bound_fare:
            passenger_data.drop(index, inplace=True)
        elif row['age'] < lower_bound_age or row['age'] > upper_bound_age:
            passenger_data.drop(index, inplace=True)

    return passenger_data
    

def histogram_of_fare_and_age_after_removing_outliers(passenger_data):
    passenger_data = remove_outliers_fare_and_age(passenger_data)

    plt.hist(passenger_data['fare'],density=True, bins=30)
    plt.ylabel('Probability')
    plt.xlabel('Fare')
    plt.title('Histogram of Fare After Removing Outliers')
    plt.show()

    plt.hist(passenger_data['age'],density=True, bins=30)
    plt.ylabel('Probability')
    plt.xlabel('Age')
    plt.title('Histogram of Age After Removing Outliers')
    plt.show()


def boxplot_of_fare_and_age_after_removing_outliers(passenger_data):
    plt.boxplot(passenger_data['fare'])
    plt.ylabel('Fare')
    plt.title('Boxplot of Fare After Removing Outliers')
    plt.show()

    plt.boxplot(passenger_data['age'])
    plt.ylabel('Age')
    plt.title('Boxplot of Age After Removing Outliers')
    plt.show()

    
def main():
    passenger_data = load_data()
    new_passenger_data = load_data()

    data_cleaning(passenger_data)

    data_cleaning_with_drop(new_passenger_data)

    histogram_of_fare_before_removing_extremes(new_passenger_data)

    histogram_of_fare_after_removing_extremes(new_passenger_data)

    boxplot_of_fare(new_passenger_data)

    histogram_of_fare_and_age_after_removing_outliers(new_passenger_data)

    boxplot_of_fare_and_age_after_removing_outliers(new_passenger_data)
main()
