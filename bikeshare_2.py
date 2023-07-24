import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ["january", "february", "march", "april","may", "june"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Please select a city (Chicago, Washington or New York City): ")
    while city.lower() not in ["chicago", "new york city", "washington"]:
        city = input("Please select a valid city: ")
      
      
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    month = input("Please select a month to filter by (from January to June), or 'all' to apply no month filter: ")
    while month.lower() not in ["january", "february", "march", "april","may", "june", "all"]:
        month = input("Please select a valid month: ")    
    # get user input for month (all, january, february, ... , june)

    day = input("Please select a day of the week to filter by, or 'all' to apply no day filter: ")
    while day.lower() not in ["monday", "tuesday", "wednesday", "thrusday", "friday", "saturday", "sunday", "all"]:
        day = input("Please select a valid day: ")
    # get user input for day of week (all, monday, tuesday, ... sunday)


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
    
    df = pd.read_csv(CITY_DATA[city.lower()])

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    
    if month != 'all':
        month = MONTHS.index(month) + 1
    
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    
    print('Most Popular Start Month:', MONTHS[popular_month - 1].title())


    # display the most common day of week
    popular_day = df['day'].mode()[0]
    
    print('Most Popular Start Day:', popular_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Used Start Station:', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('Most Used End Station:', popular_end_station)


    # display most frequent combination of start station and end station trip
    df['Station Combination'] = df["Start Station"].str.cat(df["End Station"], sep=' // ')
    popular_combination = df['Station Combination'].mode()[0]
    
    print('Most frequent combination of start station and end station trip:', popular_combination)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: ", df["Trip Duration"].sum())


    # display mean travel time
    print("Mean travel time: ", df["Trip Duration"].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of user types:\n", df["User Type"].value_counts(), "\n")

    if city.lower() != "washington":
        # Display counts of gender
        print("Count of gender:\n", df["Gender"].value_counts(), "\n")


        # Display earliest, most recent, and most common year of birth
        print ("Earliest year of birth: ", df["Birth Year"].min())
        print ("Most recent year of birth: ", df["Birth Year"].max())
        print ("Most common year of birth: ", df["Birth Year"].mode())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
