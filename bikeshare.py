import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = ''
    month = ''
    day = ''
    while True:
        city = input("which city u would like to know? Chicago, New York,or Washington? ").lower().title()
        #python bikeshare.py
        if city == 'Chicago':
            print("okay "+city)
            break
        if city == 'New York':
            print("okay " + city)
            break
        if city == 'Washington':
            print("okay "+city)
            break


    # AsK them if they want filter
    while True:
        filter = input("Would you like to filter the data by month, day,both or not at all?").lower()
        if filter == 'month':
            while True:
                month = input("which month? January, February, March, April, May, or June?")
                if month == 'January' or 'February' or 'March' or 'April' or 'May' or 'June':
                    print("okay")
                    break
            return city, month, 'all'

        if filter == 'day':
            while True:
                day = input("Which day? Please typ your response as Integer(e.g., 1= Sunday)")
                if int(day) >= 1 or day <= 7:
                    print("okay")
                    break
            return city, 'all', day

        if filter == 'both':
            while True:
                month = input("which month? January, February, March, April, May, or June?")
                if month == 'January' or 'February' or 'March' or 'April' or 'May' or 'June':
                    print("okay")
                    break

            while True:
                day = int(input("Which day? Please typ your response as Integer(e.g., 1= Sunday)"))
                if int(day) >= 1 or day <= 7:
                    print("okay")
                    break
            return city, month, day

        if filter == 'not at all':
            return city, 'all', 'all'


          #python bikeshare.py



    # TO DO: get user input for month (all, january, february, ... , june)




    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)



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

    if city == 'New York':
        city = 'new_york_city'
    filename = city + '.csv'

    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month == 'all' and day == 'all':
        return df

    if month != 'all':
        m = 0
        if month == 'January':
            m = 1
        if month == 'February':
            m = 2
        if month == 'March':
            m = 3
        if month == 'April':
            m = 4
        if month == 'May':
            m = 5
        if month == 'June':
            m = 6
        print(str(m))

        df = df[df['Start Time'].dt.month == m]
        df.info()
    if day != 'all':
        df = df[df['Start Time'].dt.day == int(day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['month'] = df['Start Time'].dt.month
    m = df['month'].mode()[0]
    print('\nthe most common month:{}'.format(m))

    # TO DO: display the most common day of week

    df['day'] = df['Start Time'].dt.day
    d = df['day'].mode()[0]
    print('\nthe most common day of week:{}'.format(d))

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.month
    h = df['hour'].mode()[0]
    print('\nthe most common hour:{}'.format(h))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_satation = df['Start Station'].mode()[0]
    print('\nthe most commonly used start station:{}'.format(start_satation))

    # TO DO: display most commonly used end station

    end_satation = df['End Station'].mode()[0]
    print('\nthe most commonly used end station:{}'.format(end_satation))


    # TO DO: display most frequent combination of start station and end station trip

    a=df.groupby(['Start Station','End Station']).size().idxmax()
    str1 = ','.join(a)
    freqenz = df[(df['Start Station'] == 'Lake Shore Dr & Monroe St') & (df['End Station'] == 'Streeter Dr & Grand Ave')]['Start Station'].count()
    print('\nthe most requent combination of start station and end station trip:{},count:{}'.format(str1,str(freqenz)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('\nthe total travel time:{}'.format(str(total)))

    # TO DO: display mean travel time

    mean = df['Trip Duration'].mean()
    print('\nthe mean travel time:{}'.format(str(mean)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_dict = df.groupby('User Type').size().to_dict()
        user_typ = []
        for i in user_dict:
            user_typ.append(i)
        for j in user_typ:
            print('user types:{},count:{}\n'.format(j,user_dict.get(j)))
    except:
        print("no such User Type")

    # TO DO: Display counts of gender
    try:
        gender_dict = df.groupby('Gender').size().to_dict()
        gender_typ = []
        for i in gender_dict:
            gender_typ.append(i)
        for j in gender_typ:
            print('gender types:{},count:{}\n'.format(j,gender_dict.get(j)))
    except:
        print("sry,no Gender Info")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()

        print('\nthe earliest year of birth:{}'.format(earliest))


        most_recent = df['Birth Year'].max()
        print('\nthe most_recent year of birth:{}'.format(most_recent))

        most_common = df['Birth Year'].mode()[0]
        print('\nthe most_recent year of birth:{}'.format(most_common))

    except:
        print("sry,no birth year's info")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')

    start_loc = 0
    while (view_data == 'yes'):
        print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
        i+=5
        view_data = input("Do you wish to continue?: yes/no").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
