import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#Web App Title

def app():
    st.markdown('''
    ## ** The Pandas profiling APP **
    ### An overall assessment tool for data observation.🌏
    ---
    ''')
    st.markdown(''' ** Pandas Profiling ** is one of many methods that fast and effective way to help you 
    get the overview of your raw data before working on Data pre-processing. 📌''')
    st.write(' 1.Drag and Drop your data in csv format or use our sample data.')
    st.write(' 2.The data.csv file will be shown as INPUT DATA.')
    st.write(' 3.The report will display data set info and variables types of each attributes.')

    # The Upload CSV file function will be located on left side bar
    with st.sidebar.header(' Upload your CSV file'):
        uploadFile = st.sidebar.file_uploader("Please upload your CSV file")
        st.sidebar.markdown('''
        🏄‍♂️ **Please make sure that your file is in the right format**
        Or ** use ** [IMDd movie example file](https://raw.githubusercontent.com/Prang-nin/dataAnalysis/main/TMDb_updated.CSV)
        ''')

    # Apply Pandas Profiling REport
    if uploadFile is not None:
        @st.cache
        def load_csv():
            csvFile = pd.read_csv(uploadFile)
            return csvFile
        df = load_csv()
        profile = ProfileReport(df, explorative=True)
        st.header('**INPUT DATA **')
        st.subheader('Display your raw input data')
        st.write(df)
        st.write('---')
        st.header('** Pandas Profiling Report**')
        st_profile_report(profile)
    else:
        st.info('Waiting for CSV file to be upload.')
        if st.button('Click here! to explore with the IMDb sample data'):
            # Using sample data if the button is clicked
            @st.cache
            def downloadSample():
                url="https://raw.githubusercontent.com/Prang-nin/dataAnalysis/main/TMDb_updated.CSV"
                sampleCSV = pd.read_csv(url)
                return sampleCSV
            df = downloadSample()
            profile = ProfileReport(df, explorative=True)
            st.header('**INPUT DATA **')
            st.write(df)
            st.write('---')
            st.header('** Pandas Profiling Report**')
            st_profile_report(profile)


