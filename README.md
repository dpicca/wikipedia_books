**Wikipedia books**
===================

Note: To run this code, make sure to download first the .json file. Since its size is too big we didn't import it in the code.


This project is undertaken in conjunction with DHTK (The Digital Humanities ToolKit) project as part of the course on Object Oriented Programming at the University of Lausanne, Switzerland. The code was written by Paul Zignani and Catherine Pedroni with the supervision of Davide Picca and Coline Métrailler.

Goals
-----
The goals of this project is, first of all, to work with Wikipedia Books. From a .json file containing the list of pages about Books on Wikipedia, we have to extract the following informations : 

-The Author of each book

-The Title of each book

-The Characters of each book

-And their corresponding description

With these informations, we have to create a dataclass ```Character``` containing the attribute ```Character``` and ```Description```. Afterwards, we have to create a new dataclass ```Book``` containing the attributes ```Title```, ```Author``` and ```Characters```, the attribute ```Characters``` containing the dataclass ```Character```. Finally the project ends with percentage calculation to see how many Books have a list of Characters on their Wikipedia page.

Procedure
---------

The first thing we had to work on were the different regex we were going to use to extract the information needed. If the Author and Title were easily extractable with a regex because of the homogeneity of the way it was written in the file, it was more complicated for the Characters and Descriptions. After many tries, we settled on using three regex instead of one to extract as much information as possible. 
Our code follows this logic: For each book, therefore each entry on the .json file, the ```Dumparser``` class extracts the Character's name and description, creates a dataclass ```Character``` to stock these informations and then puts it all in a list, which leaves us with a list of Characters for each book. It then creates the dataclass ```Book``` and adds to it the corresponding extracted information, i.e Title, Author and the list of Character. Finally, it calculates the percentage of pages containing a list of Character.

Results
-------
After parsing the whole, it shows that only 7% of the Books actually have a Characters list. This number is not that surprising considering a majority of wikipedia Books are either articles or scientific Books rather than Novels. 
Then, among this 7% of Book with a Character list, we were able to extract around 80% of the Characters and their description. 
The results are shown like this :
```
Book(Title='Animalia (book)', Author='Graeme Base', Characters=None)
Book(Title='Anthropology', Author='None', Characters=None)
Book(Title='Blade Runner 2: The Edge of Human', Author='K. W. Jeter', Characters=[Character(Character='Roy Batty', Description='The man which Tyrell used as the template for his combat replicants is in fact a man of considerable instability, suffering from a brain disorder that prevents him from experiencing fear.'), Character(Character='Dave Holden', Description='Starting off bed-ridden after his attack by the replicant Leon, Holden is rescued by Roy who in turn leads him to some startling revelations.')])
