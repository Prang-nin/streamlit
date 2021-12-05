import streamlit as st

class multipage: 
    """
    This class will combine multipage of application
    """
    def __init__(self):
        """
        initializering object with empty list of page
        """
        self.pages =[]
    
    def addPage(self, title, function):
        """
        parameter : 
        title: The title of each page
        function: The render function of eaxh page
        """
        self.pages.append(
            {
                'title':title,
                'function':function
            }
        )
    
    def run(self):
        """
        This function create a dropdown selection box and run the app function
        according to selected page title
        """
        # Create a dropdown selectbox to select the page to run
        page = st.sidebar.selectbox(
            'Navigation is here!',
            self.pages,
            format_func =lambda page: page['title']
        )
        # run the selected function
        page['function']()