#import required packeges
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

#read csv file using pandas
beneficiary = pd.read_csv("benificiary_d.csv")
inpatient_c = pd.read_csv("inpatient_c.csv")
outpatient_c = pd.read_csv("outpatient_c.csv")


# Set page title and color
st.set_page_config(page_title=" CMS Dashboard", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")
st.markdown(f"<h1 style='text-align: center; color: #35BAE2 ; width:1360px;height : 100px '>CMS Dashboard</h1>",unsafe_allow_html=True)

# start sidebar menu where we can appply filters
with st.sidebar:
# start Demographic category
    st.markdown(
        '<div style="background-color: #060505; color:black;height: 50px; width: 298px; border-radius: 5px">'
        '<h2 style="text-align: center;color: white">Demographic</h2>'
        '</div>', unsafe_allow_html=True
    )
   
    a=['All'] 
# four filter apply on demographic 
    options1=st.multiselect('Select age', options=['All'] + list(beneficiary['AGE_INTERVAL'].unique().tolist()),default=a)
    options2=st.multiselect('Select Gender', options=['All'] + list(beneficiary['GENDER'].unique().tolist()),default=a)
    options3=st.multiselect('Select Race', options=['All'] + list(beneficiary['RACE'].unique().tolist()),default=a)
    options4=st.multiselect('Select State', options=['All'] + list(beneficiary['STATE'].unique().tolist()),default=a)


    options12=['All'] + list(beneficiary['AGE_INTERVAL'].unique())
    
       

# Check the filters and update the data frame accordingly
    if 'All' in options1:
             filtered_df = beneficiary
    else:
         filtered_df = beneficiary[beneficiary['AGE_INTERVAL'].isin(options1)]

    if 'All' not in options3:
            filtered_df = filtered_df[filtered_df['RACE'].isin(options3)]
            st.write(len(filtered_df))
    if 'All' not in options2:
            filtered_df = filtered_df[filtered_df['GENDER'].isin(options2)]
            st.write(len(filtered_df))
    if 'All' not in options4:
            filtered_df = filtered_df[filtered_df['STATE'].isin(options4)]
            
    
    
with st.sidebar:
 #start Clinical category
        st.markdown(
            
            '<div style="background-color: #060505;color:black; height: 50px; width: 298px; border-radius: 5px">'
            '<h2 style="text-align: center;color: white">Clinical</h2>'
            '</div>', unsafe_allow_html=True
        )
       

        
            
            
        diseases = ['ALZHEIMER','HEART FAILURE','KIDNEY','CANCER','CHRONIC OBSTRUCTIVE','DEPRESSN','DIABETES',
                'ISCHEMIC HEART','OSTEOPOROROSIS','RHEUMATOID' ,'STROKE TRANSIENT ISCHEMIC']
 # radio button toggel between Inclusive and Exclusive if click inclusive then perform "isin" else  perform "not in"
        option_1=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox1')
        selected_diseases = st.multiselect('Select diseases', options=diseases,default=['ALZHEIMER','HEART FAILURE'])
        year=['2010','2009','2008']
            #default_option='2008'
        option_2=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox2')
        year_selected = st.selectbox('Select year', options=year)
            
            
 # add suffix on disease accroding based on year     
        if (year_selected == "2010"):
                    selected_diseases = [x + '_10' for x in selected_diseases]
        elif (year_selected == "2009"):
                    selected_diseases = [x + '_09' for x in selected_diseases]
        else:
                    selected_diseases = [x + '_08' for x in selected_diseases]
            

# Check the filters and update the data frame accordingly           
        if option_1=="Exclusion":
            
            filtered_df=filtered_df[~filtered_df[selected_diseases].isin(['1']).any(axis=1)]
           
        else:
            filtered_df=filtered_df[filtered_df[selected_diseases].isin(['1']).any(axis=1)]

        # if option_2=="Exclusion":
        #     filtered_df=filtered_df[~filtered_df[year_selected].isin(['1',1])]
        # else:
        #     filtered_df=filtered_df[filtered_df[year_selected].isin(['1',1])]
        #     #st.sidebar.write(f"Clinical: {len(filtered_df1)}")

        
        
# this dropdown is for two sub-catetory in clinical category
        option21 = st.selectbox("Select an option", [ "Inpatient", "Outpatient"])    
# this show inpatient filters
        if option21 == "Inpatient":
            a=['All']
            option_3=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox3')
            options1 = st.multiselect("Admiting Diagnosis", ["All"] + list(inpatient_c["ADMTNG_ICD9_DGNS_CD"].unique()),default=a)

            option_4=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox4')
            options2 = st.multiselect("Select a Diagnosis_1", ["All"] + list(inpatient_c["ICD9_DGNS_CD_1"].unique()),default=a)

            option_5=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox5')
            options3 = st.multiselect("Select a Diagnosis_2", ["All"] + list(inpatient_c["ICD9_DGNS_CD_2"].unique()),default=a)

            option_6=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox6')
            options4= st.multiselect("Select Claim Diagnosis Groupe", ["All"] + list(inpatient_c["CLM_DRG_CD"].unique()),default=a)
            #Procedure = st.multiselect(" Select a Procedure", ["All"] + list(inpatient["ICD9_PRCDR_CD_1"].unique()),default=a)
            
            if 'All' in options1:
                
                filtered_df1 = inpatient_c
            else:
                if option_3=="Exclusion":
                    filtered_df1 = inpatient_c[~inpatient_c['ADMTNG_ICD9_DGNS_CD'].isin(options1)]
                else:
                    filtered_df1 = inpatient_c[inpatient_c['ADMTNG_ICD9_DGNS_CD'].isin(options1)]

            if 'All' not in options2:
                if option_4=="Exclusion":
                 filtered_df1 = filtered_df1[~filtered_df1['ICD9_DGNS_CD_1'].isin(options2)]
                else:
                    filtered_df1 = filtered_df1[filtered_df1['ICD9_DGNS_CD_1'].isin(options2)]
                    
                
            if 'All' not in options3:
                if option_5=="Exclusion":
                  filtered_df1 = filtered_df1[~filtered_df1['ICD9_DGNS_CD_2'].isin(options3)]
                else:
                    filtered_df1 = filtered_df1[filtered_df1['ICD9_DGNS_CD_2'].isin(options3)]
            if 'All' not in options4:
                if option_6=="Exclusion":
                    filtered_df1 = filtered_df1[~filtered_df1['CLM_DRG_CD'].isin(options4)]
                else:
                    filtered_df1 = filtered_df1[filtered_df1['CLM_DRG_CD'].isin(options4)]
                    
            
            #st.sidebar.write(f"Clinical: {len(filtered_df2)}")


   # this show outpatient filters
        else: 
            a=['All'] 
            option_7=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox7')
            options1 = st.multiselect("Admiting Diagnosis", ["All"] + list(outpatient_c["ADMTNG_ICD9_DGNS_CD"].unique()),default=a)

            option_8=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox8')
            options2 = st.multiselect("select a Diagnosis_1", ["All"] + list(outpatient_c["ICD9_DGNS_CD_1"].unique()),default=a)

            option_9=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox9')
            options3 = st.multiselect("select a Diagnosis1_2", ["All"] + list(outpatient_c["ICD9_DGNS_CD_2"].unique()),default=a)
            #CD_3= st.multiselect("CD_3", ["All"] + list(inpatient["ICD9_DGNS_CD_3"].unique()))
            # Procedure = st.multiselect("Select Procedure", ["All"] + list(inpatient["ICD9_PRCDR_CD_1"].unique()),default=a)

            if 'All' in options1:
                filtered_df1 = outpatient_c
            else:
                if option_7=="Exclusion":
                    filtered_df1 = outpatient_c[~outpatient_c['ADMTNG_ICD9_DGNS_CD'].isin(options1)]
                else:
                    filtered_df1 = outpatient_c[outpatient_c['ADMTNG_ICD9_DGNS_CD'].isin(options1)]
            

            if 'All' not in options3:
                if option_8 =="Exclusion":
                  filtered_df1 = filtered_df1[~filtered_df1['ICD9_DGNS_CD_1'].isin(options3)]
                else:
                    filtered_df1 = filtered_df1[filtered_df1['ICD9_DGNS_CD_1'].isin(options3)]
                    
                
            if 'All' not in options2:
                if option_9 =="Exclusion":
                  filtered_df1 = filtered_df1[~filtered_df1['ICD9  _DGNS_CD_2'].isin(options2)]
                else:
                    filtered_df1 = filtered_df1[filtered_df1['ICD9_DGNS_CD_2'].isin(options2)]
            
                
        
                

with st.sidebar:
 #start financial category
        st.markdown(
            '<div style="background-color: #060505; height: 50px ; color:black; width: 298px; border-radius: 5px ">'
            '<h2 style=" text-align: center;color: white">Financial</h2>'
            '</div>', unsafe_allow_html=True
            )

       
 # in clinical category if celect inpatient then here show inpatient financial options
        if option21=='Inpatient':
# this is claim amountslider so we can apply lower limit or upper limit 
            values = st.slider(
            label='Select a Range of  Claim Amount:',
            min_value=0,
            max_value=57000,
            value=(0, 8000),
            ) 
            filtered_df1 = filtered_df1[(filtered_df1['CLM_PMT_AMT'] >= values[0]) & (filtered_df1['CLM_PMT_AMT'] <= values[1])]
 #this is claim utilization slider   
            values = st.slider(
            label='Select a Range of  Claim Utilization :',
            min_value=0,
            max_value=150,
            value=(0, 50),
            ) 
            #   filtered_df3 = outpatient
            filtered_df1 = filtered_df1[(filtered_df1['CLM_UTLZTN_DAY_CNT'] >= values[0]) & (filtered_df1['CLM_UTLZTN_DAY_CNT'] <= values[1])]

        else:
   #this is claim utilization slider
                values = st.slider(
                label='Select a Range of  Claim Amount:',
                min_value=0,
                max_value=3300,
                value=(0, 800),
                ) 
                # filtered_df3 = outpatient
                filtered_df1 = filtered_df1[(filtered_df1['CLM_PMT_AMT'] >= values[0]) & (filtered_df1['CLM_PMT_AMT'] <= values[1])]
                st.write(len(filtered_df1))


# after filtering merge two dataframe base on "DESYNPUF_ID" and store in one data frame
final1=filtered_df.merge(filtered_df1,how='inner',on=['DESYNPUF_ID'])         

# remove duplicates based on "DESYNPUF_ID"
df = final1.drop_duplicates(subset=["DESYNPUF_ID"], keep='first')

# this style for  cards in this show counts of claims ,unique patients ,total amount of claims
style = """
div[data-testid="metric-value-container"] {
    font-size: 1rem;
    font-weight: bold;
    color: #ffffff;
}

div[data-testid="metric-delta-container"] {
    font-size: 1.30rem;
    font-weight: bold;
}

div[data-testid="metric-container"] {
    background-color: #008080;
    border-radius: 10px;
    padding: 1rem;
}
"""

# Display the metrics in a styled box using Streamlit's metric function
col11, col12 ,col13= st.columns(3)

with col11:
    st.write('<style>{}</style>'.format(style), unsafe_allow_html=True)
    st.metric("Number of Unique Patient",f"{len(final1['DESYNPUF_ID'].unique())}")

with col12:
    st.write('<style>{}</style>'.format(style), unsafe_allow_html=True)
    st.metric("Number of Claim",(f"{final1.shape[0]}"))

with col13:
    st.write('<style>{}</style>'.format(style), unsafe_allow_html=True)
    st.metric("Total Claim Amount",(f"${final1['CLM_PMT_AMT'].sum()}"))








# display window devides in to 3 columns
col1, col2, col3 = st.columns(3)
with col1:
# display histogram based on age wise analysis 
    fig = px.histogram(df,
                   x='AGE_INTERVAL',
                   text_auto=True,
                   width=300,
                   title = " Age Base Analysis",
                   height=400
                   

                   )
    st.plotly_chart(fig)

with col2:
     value=df.groupby('RACE')['RACE'].count()
     name=df.groupby('RACE')['RACE'].count().index
     fig1 = px.pie(df, values = df.groupby('RACE')["RACE"].count(),names=name,title = "Race Base Analysis", width=400,height = 400)
     fig1.update(layout=dict(title=dict(x=0.1)))
     fig1.update_traces(textposition='inside', textinfo='percent')
     st.plotly_chart(fig1)

with col3:
        value=df.groupby('GENDER')['GENDER'].count()
        name=df.groupby('GENDER')['GENDER'].count().index
        chart1 = px.pie(df, values = value,names=name,title = "Gender Base Analysis",width=500, height = 400)
        chart1.update(layout=dict(title=dict(x=0.1)))
        st.plotly_chart(chart1)

        
        
        
        
col01,col02=st.columns(2)
with col01:
    st.write(df.head(10))
    if st.button('Download CSV'):
        # Convert DataFrame to CSV and download
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # Encode to base64
            href = f'<a href="data:file/csv;base64,{b64}" download="data.csv"> Click On For Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)


with col02: 
    label_font_size = 16
    fig00 = go.Figure(go.Funnel(
                y=y,
                x=x,
                textinfo="value+percent initial",
                textfont={"size": label_font_size}
            ))

    fig00.update_layout(
                title="Funnel Report",
                # height=800,
                # width=500
            )

    st.plotly_chart(fig00)
# with col4:
#     fig2 = go.Figure(data=go.Choropleth(
#     locations=final1['STATE'], # Spatial coordinates
#     # z = final1['total exports'].astype(float), # Data to be color-coded
#     locationmode = 'USA-states', # set of locations match entries in `locations`
#     colorscale = 'Reds',
#     colorbar_title = "Millions USD",
#     (fig2)

     
# ))


st.write(df.head())
