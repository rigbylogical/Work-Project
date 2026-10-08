import pandas as pd
import streamlit as st

#Page name
st.set_page_config(page_title="2026 Summer Stats",layout="wide")

#Data
df1 = pd.read_csv('4321Summer.csv')
df2 = pd.read_csv('4321School.csv')

#Dash header
pic,title,logo = st.columns([.75,4,1.2])
with pic:
    st.image("em.jpg")
with title:
    st.title(f"Dashboard 2026 summer")
    st.subheader('''
    2026 Stats
    Driver Name | Pierre Nance
    
    Manager | Kevin Kwieren
    ''')
with logo:
    st.image("lo.png")
st.divider()

# Button installs
button1,button2,button3 = st.columns(3)
with button1:
    summer_stats = st.button("Summer Stats")
with button2:
    school_stats = st.button("School Stats")
with button3:
    raw_data = st.button("Raw Data")

# Summer Sum
most_route = df1['Route'].mode()[0] if not df1['Route'].empty else "N/A"
count = len(df1[df1['Route'].astype(str) == '4321'])
total= len(df1['Route'])
avg_cases = df1['Case Count'].mean()

# School Sum
most2 = df2['Route'].mode()[0] if not df2['Route'].empty else "N/A"
count2 = len(df2[df2['Route'].astype(str) == '4321'])
total2 = len(df2['Route'])
avg_cases2 = df2['Case Count'].mean()

# Daily Summer Stats
monday_avg1 = df1.loc[df1['Day of week'] == 'Monday', 'Case Count'].mean()
tuesday_avg1 = df1.loc[df1['Day of week'] == 'Tuesday', 'Case Count'].mean()
wen_avg1 = df1.loc[df1['Day of week'] == 'Wednesday', 'Case Count'].mean()
thurs_avg1 = df1.loc[df1['Day of week'] == 'Thursday', 'Case Count'].mean()
fri_avg1 = df1.loc[df1['Day of week'] == 'Friday', 'Case Count'].mean()

# Dailu School Stats
monday_avg2 = df2.loc[df2['Day of week'] == 'Monday', 'Case Count'].mean()
tues_avg2 = df2.loc[df2['Day of week'] == 'Tuesday', 'Case Count'].mean()
wed_avg2 = df2.loc[df2['Day of week'] == 'Wednesday', 'Case Count'].mean()
thurs_avg2 = df2.loc[df2['Day of week'] == 'Thursday', 'Case Count'].mean()
fri_avg2 = df2.loc[df2['Day of week'] == 'Friday', 'Case Count'].mean()

#Summer Stats
if summer_stats:
    st.subheader('Summer Stats')
    most, count_of_most, total_routes_ran, aver_case = st.columns(4)
    with most:
        st.metric(label='Most Ran Route',value=most_route)
    with count_of_most:
        st.metric(label='Most Ran Route Count',value=count)
    with total_routes_ran:
        st.metric(label='Total Routes Ran',value=total)
    with aver_case:
        st.metric(label='Average Cases A Day', value=f"{avg_cases:.2f}")
    st.write('##')
    st.subheader('Daily Averages')
    mon1, tue1, wed1, thu1, fri1 = st.columns(5)
    with mon1:
        st.metric(label='Monday Average', value=f'{monday_avg1:.2f}')
    with tue1:
        st.metric(label='Tuesday Average', value=f'{tuesday_avg1:.2f}')
    with wed1:
        st.metric(label='Wednesday Average', value=f'{wen_avg1:.2f}')
    with thu1:
        st.metric(label='Thursday Average', value=f'{thurs_avg1:.2f}')
    with fri1:
        st.metric(label='Friday Average', value=f'{fri_avg1:.2f}')

#School Stats
if school_stats:
    st.subheader('School Stats')
    most22, count_of_most22, total_routes_ran22, aver_case22 = st.columns(4)
    with most22:
        st.metric(label='Most Route Route',value=most2)
    with count_of_most22:
        st.metric(label='Most Route Route Count',value=count2)
    with total_routes_ran22:
        st.metric(label='Total Routes Ran',value=total2)
    with aver_case22:
        st.metric(label='Average Cases A Day', value=f"{avg_cases2:.2f}")
    st.write('##')
    st.subheader('Daily Averages')
    mon2,tue2,wed2,thu2,fri2 = st.columns(5)
    with mon2:
        st.metric(label='Monday Average', value=f'{monday_avg2:.2f}')
    with tue2:
        st.metric(label='Tuesaday Average',value = f'{tues_avg2:.2f}')
    with wed2:
        st.metric(label='Wednesday Average',value = f'{wed_avg2:.2f}')
    with thu2:
        st.metric(label='Thursday Average',value = f'{thurs_avg2:.2f}')
    with fri2:
        st.metric(label='Friday Average',value = f'{fri_avg2:.2f}')
if raw_data:
    st.title('Raw Data')
    st.subheader('Summer Raw Data')
    st.write(df1[['Week', 'Date', 'Day of week', 'Case Count', 'Route']])
    st.divider()
    st.write('##')
    st.subheader('School Raw Data')
    st.write(df2[['Week', 'Date', 'Day of week', 'Case Count', 'Route']])

st.divider()
st.write('##')
st.subheader('Awards')