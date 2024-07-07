# A streamlit app to iteratively calculate median values

## Description
This project implements a simple streamlit app allowing user to iteratively create integer values & add them to a list and calculate for each iteration the median. This apps aims to minizime runtime using commands provided by heapq package  

## Features
1. Interactive UI to create integers & sedn to backend for calculation
2. Direct calculation of median values on button click
3. Direct visualization of median values as simple line chart
4. Runtime reduction by finding for each iteration the median in O(1) & applying appendNum in O(logN)

## Technical
1. Using heapq package to mimick a balanced binary tree search
2.  Creating class MedianFinder with children methods appendNum() & getMedian() to be later directly applied on iterations
3.   Using streamlit package to create simple UI

## Requirements
1. Python 3.x
2. proper setup of working directory
3. Streamlit
4. heapq

## How to Use
1. Have at least python 3.x installed
2. Make sure to pip install the streamlit package
3. Make sure to save "app.py" to your correct working directory
4. Have proper browser installed (chrome, firefox or edge)
5. From your console run the command "streamlit run app.py" and press ENTER
6. If asked to verify email in console just press ENTER (to move on) --> URL should be shown then
7. If app does not appear in web browser -> copy URL (localhost) -> paste it to new web browser window --> press ENTER
8. Use (left) sidebar to input whole number manually
9. Click "Add number" to append number to a list & start median calculation
10. View the number list, median value, median list and line chart --> Check if results are correct
11. Repeat as often as you want
12. To empty the browser refresh URL again

## Installation
1. Clone this repository
2. Install the required packages (see above)
