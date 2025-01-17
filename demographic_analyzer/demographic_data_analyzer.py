import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('demographic_analyzer/adult.data.csv', sep=',')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series([len(df.loc[df['race'] == race]) for race in df['race'].unique()])
    race_count.index = df['race'].unique()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors']) / len(df['education'])) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    lower_education = df[~df['education'].isin(advanced_education)]

    advanced_edu_high_income = higher_education[higher_education['salary'] == '>50K']
    lower_education_high_income = lower_education[lower_education['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = round((len(advanced_edu_high_income) / len(higher_education)) * 100, 1)
    lower_education_rich = round((len(lower_education_high_income) / len(lower_education)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == df['hours-per-week'].min()]
    
    rich_percentage = ((len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100 )

    # What country has the highest percentage of people that earn >50K?

    highest_earning_country = ((df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100).idxmax()
    highest_earning_country_percentage = round(((df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_people_IN = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = rich_people_IN['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
