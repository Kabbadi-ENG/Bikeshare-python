import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all','sunday' , 'monday', 'tuesday', 'wednesday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Would you like to see data for Chicago, New York City, or Washington?").lower()
    while city not in CITY_DATA:
        print("Sorry, invalid input.Please choose from the list.")
        city = input("Please choose from these cities: Chicago, New York City, or Washington.").lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Choose a month from  this list to analyse:( January, February, March, April, May, June OR All for all of the months.)").lower()
    while month not in months :
        print("Sorry, invalid input.Please choose from the list.")
        month = input("Please choose from these months : January, February, March, April, May, June OR All for all of the months.").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose a day from  this list to analyse:( Sunday, Monday, Tuesday, Wednesday, Friday, Saturday OR All for all of the days.)").lower()
    while day not in days:
        print("Sorry, invalid input.Please choose from the list.")
        day = input("Please choose from these days : Sunday, Monday, Tuesday, Wednesday, Friday, Saturday OR All for all of the days.").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # I took this code from Practice Solution #3

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
  # change dt.day_name() to dt.weakday_name() if you want the code to work on old version
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("The most common month is:",most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("The most common day of the week is:",most_common_day.title())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df["Start Time"].mode()[0]
    print("The most common start hour is:",most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("The most common start station is:",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("The most common end station is:",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (df["Start Station"]+ " - " + df["End Station"]).mode()[0]
    print("The most most frequent combination of start station and end station trip is:", most_frequent_combination.split(","))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #convert from seconds to days
    total_travel_time = df["Trip Duration"].sum()
    print("The Total Travel time is ",total_travel_time/86400 , "days")

    # TO DO: display mean travel time
     #convert from seconds to minutes

    average_travel_time = df["Trip Duration"].mean()
    print("The Average Travel time is ",average_travel_time/60 , "Minuets")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()

    print("The Counts of user types is: ", user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("the number of customers by genders are: ", gender_count)
    except KeyError:
        print("There is no gender data for this city")    

    # TO DO: Display earliest, most recent, and most common year of birth

    # 1- earliest  year of birth

    try:
        earliest_year = df["Birth Year"].min()
        print("The oldest customers were born in the year: ",earliest_year)
    except KeyError:
        print("there is no Birth Year data for this city")
  
    # 2- most recent year of birth

    try:
        most_recent_year = df["Birth Year"].max()
        print("The yungest customers were born in the year: ",most_recent_year)
    except KeyError:
        print("there is no Birth Year data for this city")

    # 3- most common year of birth

    try:
        most_common_year = df["Birth Year"].mode()[0]
        print("Most customers were born in the year: ",most_common_year)
    except KeyError:
        print("there is no Birth Year data for this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #display 5 lines of raw data from CSV file
lines = 0
def display_raw_data(df):
    lines = 0
    while True:
        raw_data = input("Would you like to see the raw data? Enter yes or no.").lower()
        if raw_data != "yes" :
            return
        lines += 5
        print(df.iloc[lines:lines+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
