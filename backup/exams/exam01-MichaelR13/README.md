# Exam 1

## Rules of Behavior
1. Do not communicate with anyone during the exam (no email, no social media, no Discord, no texting, no phones, no talking, no passing notes, no internet communicating).  If there is any evidence of communicating with anyone during the exam you will receive a zero.
1. You **must** turn off your cell phone and store it away.
1. Your submission **must** be solely you own work without the assistance of anyone by any means.
1. All programming code **must** be written in Python.
1. You **must** use Tuffix to unit test your program.
1. All your code **must** be pushed to Github by the scheduled end of class today.  Any submissions after that time will not be considered.
1. You may use your book.
1. You may use the Internet as a **reference only**.
1. If you have questions, approach the instructor desk.

## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```

1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/CSUF-CPSC223P-STMAY-2023F/exam01-username.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd exam01-username
     ```
     
## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Aircraft Manifest manager.  The program simulates people purchasing airline tickets, checking in, checking bags, and boarding the aircraft.

1. Your are given a main.py file which defines a nested list data structure as follows:
     ```
     [
     	[seat(str), first_name(str), last_name(str), checked_in(bool), no_bags(int), boarded(bool)],
     	[seat(str), first_name(str), last_name(str), checked_in(bool), no_bags(int), boarded(bool)],
     	[seat(str), first_name(str), last_name(str), checked_in(bool), no_bags(int), boarded(bool)],
     	...
     ]
     ```
	While this data is given in the main.py file, your manifest module functions should accept any data that meets the above data structure.  The main.py file also prints out a menu.  The code for the first menu item, Print Seating Chart, is provided for you.  The remaining menu items collect the user input and make the appropriate manifest module functions calls.  Your task is to code all the manifest module functions (you do not need to make any edits to main.py).
1. Edit the `manifest` module to meet the following requirements:
     1. Define a function named `get_passenger_manifest` to meet the following requirements:
          1. Take a `manifest` list as a keyword parameter. The list should meet the data structure requirements listed above.
          1. Create a new list where each inner list is ordered as follows: `[last_name(str), first_name(str), seat(str), checked_in(bool), no_bags(int), boarded(bool)]`.
          1. The new list should only contains inner lists where the `last_name` and `first_name` are not empty strings.
          1. The new list should be sorted (case insensitive) by `last_name` as the primary sort and `first_name` as the secondary sort. (Note: use the example output menu item 2 below to visualize the result).
          1. Return the new list.
     1. Define a function named `purchase_ticket` to meet the following requirements:
          1. Take a `manifest` list as a keyword parameter. The list should meet the data structure requirements listed above.
          1. Take a `first_name` string as a keyword parameter.
          1. Take a `last_name` string as a keyword parameter.
          1. Take a `seat` string as a keyword parameter.
          1. If the seat (case insensitive) is already taken i.e. the `first_name` and `last_name` elements are not empty strings, return a `False`.
          1. If the seat is invalid, return a `False`.
          1. Otherwise, for the appropriate seat in the manifest, set the `first_name` and `last_name`.
     1. Define a function named `cancel_ticket` to meet the following requirements:
          1. Take a `manifest` list as a keyword parameter. The list should meet the data structure requirements listed above.
          1. Take a `seat` string as a keyword parameter.
          1. If the seat (case insensitive) is not already taken i.e. the `first_name` and `last_name` elements are empty strings, return a `False`.
          1. If the seat is invalid, return a `False`.
          1. Otherwise, for the appropriate seat in the manifest, set the `first_name` and `last_name` to empty strings, set the `checked_in` and `boarded` to `False`, and set the `no_bags` to 0.
     1. Define a function named `check_in` to meet the following requirements:
          1. Take a `manifest` list as a keyword parameter. The list should meet the data structure requirements listed above.
          1. Take a `seat` string as a keyword parameter.
          1. If the seat (case insensitive) is not already taken i.e. the `first_name` and `last_name` elements are empty strings, return a `False`.
          1. If the seat is invalid, return a `False`.
          1. Otherwise, for the appropriate seat in the manifest, set the `checked_in` to `True`.
     1. Define a function named `check_bags` to meet the following requirements:
          1. Take a `manifest` list as a keyword parameter. The list should meet the data structure requirements listed above.
          1. Take a `seat` string as a keyword parameter.
          1. Take a `no_bags` int as a keyword parameter.
          1. If the seat (case insensitive) is not already taken i.e. the `first_name` and `last_name` elements are empty strings, return a `False`.
          1. If the seat is invalid, return a `False`.
          1. If the seat passenger has not checked in, return a `False`.
          1. Otherwise, for the appropriate seat in the manifest, set the `no_bags`.
     1. Define a function named `board_aircraft` to meet the following requirements:
          1. Take a `manifest` list as a keyword parameter. The list should meet the data structure requirements listed above.
          1. Take a `seat` string as a keyword parameter.
          1. If the seat (case insensitive) is not already taken i.e. the `first_name` and `last_name` elements are empty strings, return a `False`.
          1. If the seat is invalid, return a `False`.
          1. If the seat passenger has not checked in, return a `False`.
          1. Otherwise, for the appropriate seat in the manifest, set the `boarded` to `True`.
1. Example output:

    ```
	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 1

	** SEATING CHART **
	      A  B  C
	     ========
	  1 | -  -  -
	  2 | x  x  -
	  3 | -  -  x
	  4 | -  x  -
	  5 | -  -  -
	  6 | x  x  x
	  7 | -  x  -
	  8 | x  -  x
	  9 | -  -  -

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 2

	** PASSENGER MANIFEST **
	Last Name   First Name   Seat   Checked-In   No. Bags   Boarded
	=========   ==========   ====   ==========   ========   =======
	Doe         Jane          4B       Yes           2                  
	Eckart      Bob           6A       Yes           1                  
	Evans       Becky         3C                     0                  
	Gates       Bill          7B                     0                  
	Jobs        Steve         6B       Yes           2                  
	Mason       George        8C       Yes           1        Yes       
	McEntee     Todd          6C       Yes           1                  
	Simpson     Becky         8A       Yes           1        Yes       
	stallman    john          2B       Yes           0        Yes       
	Stallman    Richard       2A       Yes           0        Yes       

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 3

	Enter first name: Stephen
	Enter last name: May
	Enter seat: 1a
	Success

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 3

	Enter first name: Katie
	Enter last name: May
	Enter seat: 1b
	Success

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 1

	** SEATING CHART **
	      A  B  C
	     ========
	  1 | x  x  -
	  2 | x  x  -
	  3 | -  -  x
	  4 | -  x  -
	  5 | -  -  -
	  6 | x  x  x
	  7 | -  x  -
	  8 | x  -  x
	  9 | -  -  -

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 2

	** PASSENGER MANIFEST **
	Last Name   First Name   Seat   Checked-In   No. Bags   Boarded
	=========   ==========   ====   ==========   ========   =======
	Doe         Jane          4B       Yes           2                  
	Eckart      Bob           6A       Yes           1                  
	Evans       Becky         3C                     0                  
	Gates       Bill          7B                     0                  
	Jobs        Steve         6B       Yes           2                  
	Mason       George        8C       Yes           1        Yes       
	May         Katie         1B                     0                  
	May         Stephen       1A                     0                  
	McEntee     Todd          6C       Yes           1                  
	Simpson     Becky         8A       Yes           1        Yes       
	stallman    john          2B       Yes           0        Yes       
	Stallman    Richard       2A       Yes           0        Yes       

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 4

	Enter seat: 1a
	Success

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 4

	Enter seat: 1a
	Fail

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 1

	** SEATING CHART **
	      A  B  C
	     ========
	  1 | -  x  -
	  2 | x  x  -
	  3 | -  -  x
	  4 | -  x  -
	  5 | -  -  -
	  6 | x  x  x
	  7 | -  x  -
	  8 | x  -  x
	  9 | -  -  -

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 2

	** PASSENGER MANIFEST **
	Last Name   First Name   Seat   Checked-In   No. Bags   Boarded
	=========   ==========   ====   ==========   ========   =======
	Doe         Jane          4B       Yes           2                  
	Eckart      Bob           6A       Yes           1                  
	Evans       Becky         3C                     0                  
	Gates       Bill          7B                     0                  
	Jobs        Steve         6B       Yes           2                  
	Mason       George        8C       Yes           1        Yes       
	May         Katie         1B                     0                  
	McEntee     Todd          6C       Yes           1                  
	Simpson     Becky         8A       Yes           1        Yes       
	stallman    john          2B       Yes           0        Yes       
	Stallman    Richard       2A       Yes           0        Yes       

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 5

	Enter seat: 1b
	Success

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 2

	** PASSENGER MANIFEST **
	Last Name   First Name   Seat   Checked-In   No. Bags   Boarded
	=========   ==========   ====   ==========   ========   =======
	Doe         Jane          4B       Yes           2                  
	Eckart      Bob           6A       Yes           1                  
	Evans       Becky         3C                     0                  
	Gates       Bill          7B                     0                  
	Jobs        Steve         6B       Yes           2                  
	Mason       George        8C       Yes           1        Yes       
	May         Katie         1B       Yes           0                  
	McEntee     Todd          6C       Yes           1                  
	Simpson     Becky         8A       Yes           1        Yes       
	stallman    john          2B       Yes           0        Yes       
	Stallman    Richard       2A       Yes           0        Yes       

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 6

	Enter seat: 1b
	Number of bags: 2
	Success

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 2

	** PASSENGER MANIFEST **
	Last Name   First Name   Seat   Checked-In   No. Bags   Boarded
	=========   ==========   ====   ==========   ========   =======
	Doe         Jane          4B       Yes           2                  
	Eckart      Bob           6A       Yes           1                  
	Evans       Becky         3C                     0                  
	Gates       Bill          7B                     0                  
	Jobs        Steve         6B       Yes           2                  
	Mason       George        8C       Yes           1        Yes       
	May         Katie         1B       Yes           2                  
	McEntee     Todd          6C       Yes           1                  
	Simpson     Becky         8A       Yes           1        Yes       
	stallman    john          2B       Yes           0        Yes       
	Stallman    Richard       2A       Yes           0        Yes       

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 7

	Enter seat: 1b
	Success

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 2

	** PASSENGER MANIFEST **
	Last Name   First Name   Seat   Checked-In   No. Bags   Boarded
	=========   ==========   ====   ==========   ========   =======
	Doe         Jane          4B       Yes           2                  
	Eckart      Bob           6A       Yes           1                  
	Evans       Becky         3C                     0                  
	Gates       Bill          7B                     0                  
	Jobs        Steve         6B       Yes           2                  
	Mason       George        8C       Yes           1        Yes       
	May         Katie         1B       Yes           2        Yes       
	McEntee     Todd          6C       Yes           1                  
	Simpson     Becky         8A       Yes           1        Yes       
	stallman    john          2B       Yes           0        Yes       
	Stallman    Richard       2A       Yes           0        Yes       

	      *** TUFFY TITAN AIRCRAFT MANIFEST

	1. Print Seating Chart
	2. Print Passenger Manifest
	3. Purchase Ticket
	4. Cancel Ticket
	5. Check In
	6. Check Bags
	7. Board Aircraft
	8. Exit

	Enter menu choice: 8
    ```
1. Edit and run the main.py file to test all the modules and functions using the command below and repeat the steps above until you are satisfied your program output meets the above requirements. I will not grade this file - it is for your use to test the package.

    ```
    python3 -m main
    ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
manifest.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|10|manifest.py file submitted and meets the program requirements |
|6|unit test passes Test01_get_passenger_manifest|
|2|unit test passes Test02_purchase_ticket_success|
|2|unit test passes Test03_purchase_ticket_fail_seat_taken|
|2|unit test passes Test04_purchase_ticket_fail_invalid_seat|
|2|unit test passes Test05_cancel_ticket_success|
|2|unit test passes Test06_cancel_ticket_fail_seat_not_assigned|
|2|unit test passes Test07_cancel_ticket_fail_invalid_seat|
|2|unit test passes Test08_check_in_success|
|2|unit test passes Test09_check_in_fail_seat_not_assigned|
|2|unit test passes Test10_check_in_fail_invalid_seat|
|2|unit test passes Test11_check_bags_success|
|2|unit test passes Test12_check_bags_fail_seat_not_assigned|
|2|unit test passes Test13_check_bags_fail_invalid_seat|
|2|unit test passes Test14_check_bags_fail_passenger_not_checked_in|
|2|unit test passes Test15_board_aircraft_success|
|2|unit test passes Test16_board_aircraft_fail_seat_not_assigned|
|2|unit test passes Test17_board_aircraft_fail_invalid_seat|
|2|unit test passes Test18_board_aircraft_fail_passenger_not_checked_in|
