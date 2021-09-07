# Book search App  📖🔍
Interface that allows to search books by name and/or by author using the Open Library API (https://openlibrary.org/developers/api).

## Features ✔️

Search for basic information from books:

- Title
- Author
- First year of publication
- Publisher
- ISBN
- Subject


## Installation ⚙️
1. Clone repository from `https://github.com/fandemisterling100/search_books.git`
2. Install the packages required from the `search_books/` folder via:

	 `$ pip install -r requirements.txt` 

3. Serve page:

	`$ python3 manage.py runserver`


## Usage 🧑‍💻
1. Type a value for author or title or both and click on the **Search** button
 
2. To return to the index page to try another search click on the logo image at the left upper corner of the page.

3. To change the maximum limit of results to display you can change the value of `SEARCH_LIMIT` in the `services.py` file (It is already set to 10).


## Results Guide
The results are presented as follows:

[![results guide]( https://i.ibb.co/t32dWBv/guide.png "results guide")]( https://i.ibb.co/t32dWBv/guide.png "results guide")


## Additional Info
All the commands were executed from an Ubuntu-20.04 window
##### Python Version: 3.8.10
##### pip Version: 20.0.2

