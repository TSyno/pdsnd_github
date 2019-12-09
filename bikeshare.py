import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
        try:
            city = input('Which city are you interested in(chicago, new york city or washington)?').lower()
            if city in CITY_DATA:
                break
            else:
                print("\nPlease enter one of the listed cities\n")
        except KeyboardInterrupt:
            print('Please enter one of the listed cities')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try: 
            month = input('Which month of the year (from January to June) would you like to view data for (Enter all for all months)').lower()
            if month in MONTH_DATA:
                break
            else:
                print('\nPlease enter a valid month or all\n')
        except KeyboardInterrupt:
            print('Please enter a valid month or all')            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Day of week(Enter all for all days)?').lower()
            if day in DAY_DATA:
                break
            else:
                print('\nPlease enter a valid day or all\n')
        except KeyboardInterrupt:
            print('Please enter a valid day or all')
            

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    #most_common_month = months[df['month'].mode()[0]].title()
    print(MONTH_DATA[df['month'].mode()[0]].title(), 'is the most common month')
    

    # TO DO: display the most common day of week
    print(df['day_of_week'].mode()[0].title(), 'is the most common day of week')

    # TO DO: display the most common start hour
    #common_start_hour = 
    print(df['Start Time'].mode()[0].hour, 'hrs is the most common start hour')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0], 'is the most commonly used start station')


    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0], 'is the most commonly used end station')


    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_combination = df['frequent_combination'].mode()[0]
    print('The most frequent combination of start and end station is ', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total time of travel is {} seconds '.format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean time of travel is {} seconds'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    
    subscriber_count = user_type_count.iloc[0]
    print('There are {} users that are suscribers'.format(subscriber_count))
    
    customer_count = user_type_count.iloc[1]
    print('There are {} users that are customers'.format(customer_count))
    
    unknown_usertype_count = df['User Type'].isnull().sum()
    print('There are {} unidentified user types'.format(unknown_usertype_count))
    
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        
        # Display counts of gender
        gender_type_count = df['Gender'].value_counts()
        
        male_count = gender_type_count.iloc[0]
        print('There are {} males'.format(male_count))
        
        female_count = gender_type_count.iloc[1]
        print('There are {} females'.format(female_count))
        
        nogender_type_count = df['Gender'].isnull().sum()
        print('\nThere are {} unidentified genders'.format(nogender_type_count))
        
    else:
        print('Gender information is not available for this city')


    # TO DO: Display earliest, most recent, and most common year of birth
    #Check for birth year column
    if 'Birth Year' in df:
        
        # Display earliest, most recent, and most common year of birth
        earliest_birthyear = df['Birth Year'].min()
        print('The earliest birth year is ', earliest_birthyear)
        
        most_recent_birthyear = df['Birth Year'].max()
        print('The most recent birth year is ', most_recent_birthyear)
        
        most_common_birthyear = df['Birth Year'].mode()[0]
        print('The most common birth year is ', most_common_birthyear)
        
    else:
        print('\nBirth Year information is not available for this city\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):    
    i = 0
    j = 5      
    #get user input for data displaying successive five rows of data at a time
    while True:
        data = input('Would you like to view the raw data(5 rows at a time)? Enter yes or no\n')
        if data.lower() == 'yes':
            print('These are 5 rows of the raw data\n', df.iloc[i:j])  
            i += 5
            j += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #print(df.describe)
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
