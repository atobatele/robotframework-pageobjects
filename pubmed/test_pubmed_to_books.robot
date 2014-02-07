*** Settings ***

Documentation  A test of flow from pubmed to Books, showing how we might properly encapsulate the AUT(s)
...
Library    PubmedPageLibrary
Library    BooksPageLibrary

*** Test Cases ***

Test PubMed To Books
    
    Open Pubmed
    Search Pubmed  breast cancer
    Find Related Data From Pubmed In  books
    Click Books Docsum Item  0
    Click Table Of Contents Books
    Close Books

