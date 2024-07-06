# Task: Create flow & UI where (1) user iteratively generates integers (2) each integer stored to one list (2) median for each list iteration is calculated 
#       (3) chart of each calculated median is plotted
# We use heapq package (balanced binary tree search!) to work with heaps to minimize runtime as: O(1) for getMedain and O(logN) for appendNum() method
# using streamlit to create simple UI
import streamlit as st 
import heapq

# Create MedianFinder class with 2 methods appendNum() and getMedian()   
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    # define method appendNum() as heapq iteration, to check list length of small/large variables and balance them
    def appendNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    # define method getMedian() calculating median if heap lists are even and select median if odd
    def getMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return float(self.large[0])
        
# Create minimal streamlit App
st.title("Median finder",anchor=False)

# Initialize MedianFinder class and empty lists to be populated with results
if 'median_finder' not in st.session_state:
    st.session_state.median_finder = MedianFinder()
if 'number_list' not in st.session_state:
    st.session_state.number_list = []
if 'median_list' not in st.session_state:
    st.session_state.median_list = []

# Input field for user to add integers
new_number = st.sidebar.number_input("Type whole number:", value=0)

# Button (in sidebar) to add user integer to lists and save them 
if st.sidebar.button("Add number"):
    st.session_state.median_finder.appendNum(new_number)
    st.session_state.number_list.append(new_number)
    current_median = st.session_state.median_finder.getMedian()
    st.session_state.median_list.append(current_median)

# Display current median value
if st.session_state.median_list:
    current_median = st.session_state.median_list[-1]
    st.write(f"Current median: {current_median}")

# Display all integers and median values in lists
st.write(f"Number list: {st.session_state.number_list}")
st.write(f"Median list: {st.session_state.median_list}")

# Create median line chart from median_list, growing iteratively
st.line_chart(st.session_state.median_list,x_label="Iterations", y_label="Median values")