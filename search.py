from wiki import article_titles, ask_search, ask_advanced_search

# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article titles
#
# Returns: list of article titles containing given keyword (case insensitive).
# If the keyword is empty or no results are found, return an empty list.
#
# Hint: to get list of existing article titles, use article_titles()
def search(keyword):
    """
    Searches for a keyword in the article titles (case insensitive).
    Returns a list of matching titles.
    """
    result = []
    if keyword:
        keyword = keyword.lower()
        titles = article_titles()
        for title in titles:
            if keyword in title.lower():
                result.append(title)
    return result

# 2) 
#
# Function: title_length
#
# Returns 
#
# Parameters:
#   max_length - max character length of article titles
#   titles - list of article titles to search through
#
# Returns: list of article titles from given titles with a length that does
# not exceed max_length number of characters 
def title_length(max_length, titles):
    """
    Returns article titles whose length does not exceed max_length.
    """
    result = []
    for title in titles:
        if len(title) <= max_length:
            result.append(title)
    return result

# 3) 
#
# Function: article_count
#
# Parameters:
#   count - max number of returned articles
#   titles - list of article titles to search through
#
# Returns: list of articles in given titles starting from the 
# beginning that do not exceed given count in total. If there are no 
# given article titles, return an empty list regardless of the count.
# If the max is larger than the # of titles, just return all titles.
def article_count(count, titles):
    """
    Returns a list of articles limited to the number 'count'.
    If count exceeds the number of available titles, returns all titles.
    """
    result = []
    if len(titles) == 0:
        return result
    for i in range(min(count, len(titles))):
        result.append(titles[i])
    return result

# 4) 
#
# Function: random_article
#
# Parameters:
#   index - index at which article title to return
#   titles - list of article titles to search through
#
# Returns: article title in given titles at given index. If
# index is not valid, return an empty string
def random_article(index, titles):
    """
    Returns the article at the provided index or an empty string if the index is out of range.
    """
    if index >= 0 and index < len(titles):
        return titles[index]
    else:
        return ""

# 5) 
#
# Function: favorite_article
#
# Parameters:
#   favorite - favorite article title
#   titles - list of article titles to search through
#
# Returns: True if favorite article is in the given articles
# (case insensitive) and False otherwise
def favorite_article(favorite, titles):
    """
    Checks if the provided favorite article is in the list of titles (case insensitive).
    Returns True if found, otherwise False.
    """
    favorite = favorite.lower()
    for title in titles:
        if title.lower() == favorite:
            return True
    return False

# 6) 
#
# Function: multiple_keywords
#
# Parameters:
#   keyword - additional keyword to search
#   titles - article titles from basic search
#
# Returns: searches for article titles from entire list of available
# articles and adds those articles to list of article titles from basic 
# search
def multiple_keywords(keyword, titles):
    """
    Searches for a second keyword and adds any matching titles to the list from the first search.
    Avoids duplicates.
    """
    more_titles = search(keyword)
    for title in more_titles:
        if title not in titles:
            titles.append(title)
    return titles

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-5)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article titles to contain only ones of the maximum length
        articles = title_length(value, articles)
    if advanced == 2:
        # value stores max number of articles
        # Update article titles to contain only the max number of articles
        articles = article_count(value, articles)
    elif advanced == 3:
        # value stores random number
        # Update articles to only contain the article title at index of the random number
        articles = random_article(value, articles)
    elif advanced == 4:
        # value stores article title
        # Store whether article title is in the search results into a variable named has_favorite
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
        # value stores keyword to search
        # Updated article titles to contain article titles from the first search and the second search
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()