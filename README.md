# Google-s-Python-Exercises
Files here are completed exercises taken from Google's Python Class (http://code.google.com/edu/languages/google-python-class/)

The objective of the exercise is to reconstruct an image of an animal. The image has been divided into narrow vertical stripe images, each with its own URL. 
The URLs are hidden in a web server log file. The task is to find the URLs and download all the image stripes to recreate the original image.

The slice URLs are hidden within Apache log files, which are encoded to indicate the server they come from.

The exercise has two parts:

  Part A: Log File to URLs
    In this part, the task is to implement the "read_urls(filename)" function, which extracts the puzzle URLs from a log file. 
    The function should find all the URLs containing the word "puzzle" in the path. Each URL's path should be combined with the server name from the filename to form a full URL. 
    Duplicate URLs should be filtered out, and the list of full URLs should be returned in alphabetical order.

  Part B: Download Images Puzzle
    The second part involves implementing the "download_images()" function. It takes a sorted list of URLs and a directory as inputs. 
    The function downloads the image from each URL into the specified directory. If the directory doesn't exist, it is created. 
    The downloaded images are named using a simple scheme like "img0," "img1," etc. 
    The function also creates an index.html file in the directory, which contains img tags for each local image file. The img tags are placed on a single line without separation.

Once the program is working correctly, opening the generated index.html file in a browser should display the original animal image.
