import streamlit as st
from PIL import Image

# deploy
# Set up page configuration
st.set_page_config(page_title="Uber Demand-Supply Gap Analysis", layout="wide")

# Sidebar - Always open
st.sidebar.title("Navigation")
selected_section = st.sidebar.radio("Choose a Section", ["About Data", "Dashboard"])

# Add a button for the Jupyter Notebook link in the sidebar
st.sidebar.markdown("---")  # Separator
st.sidebar.markdown("### Resources")
if st.sidebar.button("Open Jupyter Notebook"):
    st.sidebar.markdown(
        "[View Notebook](https://colab.research.google.com/drive/1xHBBKqBatoMFYyHqEsTvd8HlY8Jdmm9i?usp=sharing#scrollTo=6STgju9mmFom) :notebook:",  # Replace with your actual Jupyter Notebook URL
        unsafe_allow_html=True,
    )

# About Data Section
if selected_section == "About Data":
    st.title("About the Data")
    st.write(
        """
        This dashboard analyzes Uber's demand and supply gap. 
        It highlights key patterns in ride requests, supply shortages, and trends over time.
        """
    )
    st.markdown("### Key Features of the Data:")
    st.markdown(
        """
        - **Request ID**: A unique token representing a customer request.
        - **Pickup point**: Customer pickup point with two levels based on customer's location 
          (City-represents customers to be picked up at the city and dropped to the airport; 
          Airport-represents customers to be picked up from the airport and dropped to the city).
        - **Driver ID**: Unique identification number of a driver.
        - **Status**: Represents the customer request status (trip completed, cancelled, or no cars available).
        - **Request Timestamp**: Contains date and time information at which the request was registered.
        - **Drop Timestamp**: Contains date and time information at which the trip was completed.  
        """
    )
    st.markdown("### Features Developed:")
    st.markdown(
        """
        - **Demand Analysis**: Total ride requests over time.
        - **Supply Analysis**: Fulfilled and unfulfilled ride requests.
        - **Gap Insights**: Peak time shortages and trends.
        """
    )

# Dashboard Section
elif selected_section == "Dashboard":
    st.title("Dashboard: Uber Demand-Supply Gap Analysis")
    # Display images dynamically
    st.header("Visualizations: Uber Demand-Supply Gap")
    col1, col2 = st.columns(2)  # Create two columns for displaying images

    # List of images from output1.png to output12.png
    for i in range(1, 13):  # Adjust range as needed
        image_path = f"output{i}.png"
        try:
            image = Image.open(image_path)
            if i % 2 != 0:  # Odd images go to col1
                with col1:
                    st.image(image, caption=f"Visualization {i}", use_container_width=True)
            else:  # Even images go to col2
                with col2:
                    st.image(image, caption=f"Visualization {i}", use_container_width=True)
        except FileNotFoundError:
            st.error(f"Image '{image_path}' not found.")
st.title("""
         Conclusion
**The analysis reveals significant supply-demand gaps during peak hours, with the highest issues observed in
 the morning and evening. Addressing these gaps could involve increasing driver availability during these times
   or offering incentives for drivers to work during peak demand periods. Further exploration and targeted 
   strategies could help in balancing the supply-demand equilibrium more effectively.**
"""
   )
