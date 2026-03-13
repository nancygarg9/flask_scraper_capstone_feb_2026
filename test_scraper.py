# rule of thumb is test every function and class/object that you have written inside your python module(s)
from scraper import scrape_quotes,quotes_to_df


def test_scrape_quotes():
    quotes = scrape_quotes(limit=3)
    assert len(quotes) == 3 # getting back 3 entries in my list or not. 

def test_quotes_to_df():
    df = quotes_to_df(["ThinkPython", "AI"]) # treat this as quotes and we are passing only 2 elements "ThinkPython" and "AI"
    assert df.shape[0] ==  2
    assert "Quote" in df.columns
    # enhancement woudl be add a third column name as "Author" and assert that as well.

#pytest -v - this is how you run it.