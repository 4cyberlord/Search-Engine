# Search Engine: Part 1

## Starter Code

**search.py**: file for adding functionality to search
**wiki.py**: do not change this file. provides raw article data and functions to help you write the search code:
`article_titles()`: returns complete list of article titles our search engine will have access to
`ask_search()`: asks user for a keyword to search for
`ask_advanced_search()`: displays and asks user for advanced options search
**search_tests.py**: file for adding unit and integration tests
**search_tests_helper.py**: do not change this file. provided functions to help you write integration
 tests:
`print_basic()`: returns string to ask user for basic search keyword
`print_advanced()`: returns string to ask user for advanced search option
`print_advanced_option()`: returns string to ask user for advanced search question
`get_print()`: returns printed string when running entire search program

Note: there is pass in each function, which prevents Python from raising an error when a function has no code inside of it. When you're done implementing the function, you can delete pass.

# Instructions

# Functionality

# Do this part in search.py

The `display_results()` function is already implemented for you. It contains all of the required prompts and calls all of the search functions in the right places. Your job is to implement each of the 6 functions. There are more details in the comments (read them as they may answer any questions about edge cases) above each function but at a high level:

`search(keyword)`: Searches all article titles from wiki.article_titles() and returns a list of all article titles that contain the keyword (case insensitive)
title_length(max_length, titles): Returns a list of titles that are less than or equal to max_length in character count.
`article_count(count, titles)` : Returns the first count articles from the titles. If count is larger than the length of the titles, just return all titles.
`random_article(index, titles)`: Returns the article in titles at index or an empty string if index is invalid. Index is positive but must be within the length of the string.
`favorite_article(favorite, titles)`: Returns True or False depending on if the titles contain your favorite article (case insensitive)
`multiple_keywords(keyword, titles)`: Searches all article titles from wiki.article_titles() using keyword and returns a combined list of the basic search articles followed by the new articles.
The "Run" button will run search.py so you can run searches.

# Testing

Do this part in search_tests.py

You will write both unit tests and integration tests to verify the correctness of your program. To run your tests you must click "Terminal" and then type in python3 search_tests.py . This is different than in the past because the "Run" button can only be configured to run one file and this time it runs search.py.

# Unit tests

Please add all of your unit tests under the section labeled:

##############
# UNIT TESTS #
##############
Write at least 3 unit tests per function you defined (you do not need to write unit tests for the display_results() function). Ensure that you cover all edge cases for each function (ex: case sensitivity, empty lists, etc.). An example unit test has been provided for you that tests one input/output to the search function. You should define 6 different unit test functions that:

Are uniquely named and named beginning with "test_". It is suggested to put all unit tests for a given function in a function named test_function_name (ex: test_multiple_keywords)
Have one parameter named "self"
Are indented one time to be inside the "TestSearch" class
Use either assert output == expected or self.assertEqual(output, expected) to run an individual assertion. The latter will give a more descriptive error message.
Integration tests

Please add all of your integration tests under the section labeled:

#####################
# INTEGRATION TESTS #
#####################
Write at least 5 different integration tests for verifying the behavior of the entire program. You do not need to cover every possible scenario with your integration tests but you do need to write one integration test per advanced search option. An example integration test has been provided for you that tests advanced option # 6 (None). Each separate integration test should be in its own function that:

Is uniquely named and named beginning with "test_"
Has two parameters "self" and "input_mock"
Is indented one time to be inside the "TestSearch" class
Has the line `@patch('builtins.input')` as the line preceding the function definition
Uses either assert output == expected or self.assertEqual(output, expected) to run an individual assertion. The latter will give a more descriptive error message.