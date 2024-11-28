import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city =input("Please input the city:")
        city = city.lower()
        if city in cities:
            break
        else:
            print('Please enter one of these city: chicago, new york city, washington.')

    # get user input for month (all, january, february, ... , june)
    while True:
        month =input("Please enter any one of the first 6 months. If you do not want a month filter enter 'all':")
        month = month.lower()
        if month in months:
            break
        else:
            print('Please enter any one of these month: \'january\', \'february\', \'march\', \'april\', \'may\', \'june\', \'all\'')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day =input("Please enter the day. If you do not want a day filter enter 'all':")
        day = day.lower()
        if day in days:
            break
        else:
            print('Please enter a valid day.')

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
    
    # Read data
    df = pd.read_csv(CITY_DATA[city])

    # Convert date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 
    # create data for month & day
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # Filter month
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
 
    # Filter day
    if day != 'all': 
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]

    if most_common_month == 1:
        most_common_month = "January"
    elif most_common_month == 2:
        most_common_month = "February"
    elif most_common_month == 3:
        most_common_month = "March"
    elif most_common_month == 4:
        most_common_month = "April"
    elif most_common_month == 5:
        most_common_month = "May"
    elif most_common_month == 6:
        most_common_month = "June"
    elif most_common_month == 2:
        most_common_month = "July"
    elif most_common_month == 3:
        most_common_month = "August"
    elif most_common_month == 4:
        most_common_month = "September"
    elif most_common_month == 5:
        most_common_month = "October"
    elif most_common_month == 6:
        most_common_month = "November"
    else:
        most_common_month = "December"

    print('Most Common Month: ', most_common_month)

    # display the most common day of week
    most_common_day = df['day'].mode()[0] 
    print('Most Common Day of the Week: ', most_common_day)
    print('-'*20)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_day = df['hour'].mode()[0]
    print('Most Common Start Hour:', most_common_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: ", most_commonly_start_station)
    print('-'*20)

    # display most commonly used end station
    most_commonly_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: ", most_commonly_end_station)
    print('-'*20)

    # display most frequent combination of start station and end station trip
    combo_station = df['Start Station'] + " to " +  df['End Station']
    common_combo_station = combo_station.mode()[0]
    print("Most Most Frequent Combination Of Start Station And End Station Trip: ", common_combo_station) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("The Total Travel Time is: {} Hours, {} Minutes, and {} Seconds.".format(hour, minute, second))
    print('-'*20)

    # display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    minute, second = divmod(average_duration, 60)
    if minute > 60:
        hour, minute = divmod(minute, 60)
        print('The Average Travel Time: is {} Hours, {} Minutes, and {} seconds.'.format(hour, minute, second))
    else:
        print('The Average Trip Duration is {} Minutes and {} Seconds.'.format(minute, second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of Each User Type: ", user_types)
    print('-'*20)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Counts of gender:', gender)
    except:
        print('Counts of gender: Data not found')
    print('-'*20)

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()
        print('Oldest birth year: ', earliest)
        print('Youngest birth year: ', recent)
        print('Most common birth year: ', common)
    except:
        print('Display earliest, most recent, and most common year of birth: Data not found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    # Individual trip data.
    start_data = 0
    end_data = 5
    df_length = len(df.index)
    
    while start_data < df_length:
        raw_data = input("Would you like to see the raw data? Enter 'yes' or 'no':")
        if raw_data.lower() == 'yes':
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break

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
    
#Update 2024/11/28
#refactoring
