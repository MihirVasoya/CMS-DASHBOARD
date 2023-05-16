import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# import dash
import plotly.figure_factory as ff
# import matplotlib.pyplot as plt

beneficiary = pd.read_csv("benificiary_d.csv")
#beneficiary1= pd.read_csv("benificiary_c.csv")
inpatient_c = pd.read_csv("inpatient_c.csv")
inpatient_f = pd.read_csv("inpatint_f.csv")
outpatient_c = pd.read_csv("outpatient_c.csv")
# outpatient_f = pd.read_csv("outpatient_f.csv")
#demographic_clicked=False
# Set page title and color
st.set_page_config(page_title=" CMS Dashboard", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")
st.markdown(f"<h1 style='text-align: center; color: #35BAE2 ; width:1360px;height : 100px '>CMS Dashboard</h1>",unsafe_allow_html=True)
#  f"<button style='background-color: white; margin: 5px;'>Demographic</button>",unsafe_allow_html=True)

# Create three columns


colors = ["#F57878", "#C70039", "#900C3F"]
# Add content to each column

#fig1 = px.bar(beneficiary, x='AGE_INTERVAL', y='AGE', color='GENDER', barmode='group')


    
with st.sidebar:
    st.markdown(
        '<div style="background-color: #060505; color:black;height: 50px; width: 298px; border-radius: 5px">'
        '<h2 style="text-align: center;color: white">Demographic</h2>'
        '</div>', unsafe_allow_html=True
    )
    #st.markdown(f"<div style='background-color:{colors[0]}; height: 500px; display: flex; justify-content: center; align-items: center;'>"
    a=['All']          
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
            
    
    
    #count=len(filtered_df)

#st.sidebar.markdown("### No Of Patient")
#st.sidebar.write(f"Demographic: {len(filtered_df)}")

       


    # st.markdown(
    #     '<div style="background-color: #060505;color:black; height: 50px; width: 456px; border-radius: 5px">'
    #     '<h3 style="color: white">Clinical</h3>'
    #     '</div>', unsafe_allow_html=True
    # )

# if st.sidebar.button('Filter'):
    with st.sidebar:
        st.markdown(
            '<div style="background-color: #060505;color:black; height: 50px; width: 298px; border-radius: 5px">'
            '<h2 style="text-align: center;color: white">Clinical</h2>'
            '</div>', unsafe_allow_html=True
        )
       

        
            
            
        diseases = ['ALZHEIMER','HEART FAILURE','KIDNEY','CANCER','CHRONIC OBSTRUCTIVE','DEPRESSN','DIABETES',
                'ISCHEMIC HEART','OSTEOPOROROSIS','RHEUMATOID' ,'STROKE TRANSIENT ISCHEMIC']
        option_1=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox1')
        selected_diseases = st.multiselect('Select diseases', options=diseases,default=['ALZHEIMER','HEART FAILURE'])
        year=['2010','2009','2008']
            #default_option='2008'
        option_2=st.radio( "",( "Inclusion",'Exclusion'),horizontal=True, key='checkbox2')
        year_selected = st.selectbox('Select year', options=year)
            
            
            
        if (year_selected == "2010"):
                    selected_diseases = [x + '_10' for x in selected_diseases]
        elif (year_selected == "2009"):
                    selected_diseases = [x + '_09' for x in selected_diseases]
        else:
                    selected_diseases = [x + '_08' for x in selected_diseases]
            
            
            
        if option_1=="Exclusion":
            
            filtered_df=filtered_df[~filtered_df[selected_diseases].isin(['1']).any(axis=1)]
            st.write(len(filtered_df))
        else:
            filtered_df=filtered_df[filtered_df[selected_diseases].isin(['1']).any(axis=1)]

        # if option_2=="Exclusion":
        #     filtered_df=filtered_df[~filtered_df[year_selected].isin(['1',1])]
        # else:
        #     filtered_df=filtered_df[filtered_df[year_selected].isin(['1',1])]
        #     #st.sidebar.write(f"Clinical: {len(filtered_df1)}")

        option21 = st.selectbox("Select an option", [ "Inpatient", "Outpatient"])    
    
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
            
                
        
                
            #st.sidebar.write(f"Clinical: {len(filtered_df2)}")
    with st.sidebar:
        st.markdown(
            '<div style="background-color: #060505; height: 50px ; color:black; width: 298px; border-radius: 5px ">'
            '<h2 style=" text-align: center;color: white">Financial</h2>'
            '</div>', unsafe_allow_html=True
            )

        # if option21=="Benificiary" :   
        #     option = st.selectbox("Select an option", [ "inpatient", "outpatient"])
        #     if option == "inpatient":
        #         values = st.slider(
        #         label='Select a Range of  Claim Amount:',
        #         min_value=0,
        #         max_value=57000,\
        #         value=(0, 8000),
        #         ) 
        #         filtered_df3 = inpatient_f[(inpatient_f['CLM_PMT_AMT'] >= values[0]) & (inpatient_f['CLM_PMT_AMT'] <= values[1])]
            
        #         values = st.slider(
        #         label='Select a Range of  Claim Utilization :',
        #         min_value=0,
        #         max_value=150,
        #         value=(0, 50),
        #         ) 
        #         filtered_df3 = filtered_df3[(filtered_df3['CLM_UTLZTN_DAY_CNT'] >= values[0]) & (filtered_df3['CLM_UTLZTN_DAY_CNT'] <= values[1])]
        #     #   total=filtered_df3['CLM_PMT_AMT'].sum()

        #     #   st.sidebar.write(f"Financial: {len(filtered_df)}")
        #     #   st.sidebar.write(f"Total Claim Amount: {total}")
        #     else:
            
        #         values = st.slider(
        #         label='Select a Range of  Claim Amount:',
        #         min_value=0,
        #         max_value=3300,
        #         value=(0, 800),
        #         ) 
        #         # filtered_df3 = outpatient_f
        #         filtered_df3 = outpatient_f[(outpatient_f['CLM_PMT_AMT'] >= values[0]) & (outpatient_f['CLM_PMT_AMT'] <= values[1])]
        #         # total=filtered_df3['CLM_PMT_AMT'].sum()
        if option21=='Inpatient':

            values = st.slider(
            label='Select a Range of  Claim Amount:',
            min_value=0,
            max_value=57000,
            value=(0, 8000),
            ) 
            filtered_df1 = filtered_df1[(filtered_df1['CLM_PMT_AMT'] >= values[0]) & (filtered_df1['CLM_PMT_AMT'] <= values[1])]
            
            values = st.slider(
            label='Select a Range of  Claim Utilization :',
            min_value=0,
            max_value=150,
            value=(0, 50),
            ) 
            #   filtered_df3 = outpatient
            filtered_df1 = filtered_df1[(filtered_df1['CLM_UTLZTN_DAY_CNT'] >= values[0]) & (filtered_df1['CLM_UTLZTN_DAY_CNT'] <= values[1])]

        else:
                values = st.slider(
                label='Select a Range of  Claim Amount:',
                min_value=0,
                max_value=3300,
                value=(0, 800),
                ) 
                # filtered_df3 = outpatient
                filtered_df1 = filtered_df1[(filtered_df1['CLM_PMT_AMT'] >= values[0]) & (filtered_df1['CLM_PMT_AMT'] <= values[1])]
                st.write(len(filtered_df1))



            #st.sidebar.write(f"Financial: {len(filtered_df)}")
            #st.sidebar.write(f"Total Claim Amount: {total}")
final1=filtered_df.merge(filtered_df1,how='inner',on=['DESYNPUF_ID'])         
# st.sidebar.write(f"No of Claim: {len(final1)}")
# st.sidebar.write(f"No of Unique Patient: {len(final1['DESYNPUF_ID'].unique())}")

df = final1.drop_duplicates(subset=["DESYNPUF_ID"], keep='first')
# st.write(final1.head())

# col11,col12=st.columns(2)

# col11.metric("",f"No of Unique Patient: {len(final1['DESYNPUF_ID'].unique())}")
# col12.metric("",(f"No of Claim: {len(final1)}"))

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
    st.metric("Total Claim Amount",(f"{final1['CLM_PMT_AMT'].sum()}$"))









col1, col2, col3 = st.columns(3)
with col1:
   
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
