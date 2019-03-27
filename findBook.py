#Check if a book is existing in our collection
collectionOfBooks = ["The Marvels", "Cinderalla", "Tin-Tin", "Mickey Mouse"]
print("Enter the name of the book you want")
bookToBeChecked = input()
for book in collectionOfBooks:
    if book == bookToBeChecked:
        print("Yes, We do carry the copy of that book")
        break
else:
        print("Sorry, We don't carry that book")
