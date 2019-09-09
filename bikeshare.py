import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data! It\'s interesting!!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which data would you like to analyze for Chicago, New York City, or Washington?').lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("\n Sorry! Enter an appropriate city")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('For which month do you wish to analyze for January, February, March, April, May, June Or All?').lower()
        if month not in ['all', 'january', 'february','march','april','may','june']:
            print("\n Choose a valid month")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('For which day do you like to see the data for All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday?').lower()
        if day not in ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            print('\n Choose a valid day')
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('\n The most common month is : ', most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\n The most common day of week is : ', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('\n The most common start hour is : ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print('\n The most common start station is : ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print('\n The most common end station is : ', most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    Combination_startend_station = df.groupby(['Start Station', 'End Station']).count()
    print("\n The most frequent combination of start station and end station trip is : ", most_common_start_station, "and", most_common_end_station)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('\n The total time travel is : ', Total_travel_time/86400, " Number of Days")


    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('\n The mean time travel is : ', Mean_travel_time/60, " In Minutes")


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
  
    user_types = df['User Type'].value_counts()
    print('\n The count of user types are: ', user_types)
    
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\n The gender count is: ', gender_count)
    except KeyError:
        print("\n Gender data not available for this city")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_birth = np.min(df['Birth Year'])
        print('\n Earliest year of birth is : ', earliest_year_birth)
   
        most_recent_birth = np.max(df['Birth Year'])
        print('\n Most recent year of birth is : ', most_recent_birth)
   
        common_year_birth = df['Birth Year'].mode()
        print('\n Most common year of birth is : ', common_year_birth)
    except:
        print("\n Data not available for birth date in this city")
        
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
