import pandas as pd

# DATASETS PREPARATION

# import dataset
df = pd.read_csv('datasets/Cost_of_Living_Index_2022.csv')

# drop useless tables
clean_df = df.drop(['Rank', 'Cost of Living Index', 'Rent Index', 'Groceries Index', 'Restaurant Price Index',
                    'Local Purchasing Power Index'], axis=1)

# add cost of living price table
clean_df["Cost of Living Plus Rent Index in dollars"] = 5500 * (clean_df['Cost of Living Plus Rent Index'] / 100)


# CONSTANTS ------------------------------------------------------------------------------------------------------------
NY_COST_OF_LIVING = 5500  # the cost of living in NY city is estimated at 5500$
PI = 12  # period interest (usually = 12 because there is 12 months in a year)


def get_compound_interest_added_value(val: any, cmpi: any):
    """
    This method calculates the compound interest added value only
    :param val: total value invested
    :param cmpi: total value with compound interest
    :return: the compound interest added value
    """
    return round(cmpi - val)


def get_total_wealth(ia: any, ma: any, year: any, ir: any):
    """
    This method calculates the compound interest
    :param ia : initial amount invested
    :param ma: monthly invested amount
    :param year: duration of the investment (in years)
    :param ir: interest rate (ex: tipm = 5 => interest rate of 5% per year)
    :return: the total wealth accumulated over the years
    """
    return round(((ma * (((1 + (ir / PI / 100)) ** ((year * PI) + 1)) - 1) / (ir / PI / 100)) - ma) +
                 (ia * (1 + ((ir / 100) / PI)) ** (PI * year)))


def get_total_ma(ia: any, ma: any, year: any):
    """
    This method calculates the total value monthly invested (without compound interest)
    :param ia : initial amount invested
    :param ma: monthly invested amount
    :param year: duration of the investment (in years)
    :return: the total wealth accumulated over the years without taking compound value in account
    """
    return round(ia + (ma * 12 * year))


def get_ia_with_compound_interest(ia: any, year: any, ir: any):
    """
    This method calculates the value of the initial amount invested with the compound interest
    :param ia: initial amount invested
    :param year: duration of the investment (in years)
    :param ir:
    :return:
    """
    return round(ia * (1 + ((ir / 100) / PI)) ** (PI * year))


def get_monthly_income(tw:any , independence_duration: any):
    """
    This method calculates monthly income by taking into account the total wealth and the fact that the user want an
    unlimited income or not.
    More details on the choice of the "magic numbers" here : https://youtu.be/RGU0q3gVqb8
    :param tw: the total wealth (calculate with compound interest)
    :param independence_duration: value to know if user prefer an infinite revenue or 30 years guaranteed income
    :return: the monthly income
    """
    if int(independence_duration) < 0:
        monthly_income = tw / 480
    else:
        monthly_income = tw / 320
    return round(monthly_income)


def filter_countries(income):
    countries = clean_df['Country'][clean_df['Cost of Living Plus Rent Index in dollars'] <= income]
    return countries
