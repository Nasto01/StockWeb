st.title('This is title')
st.header('THis is header')
st.subheader('This is subheader')
st.write('This is text')

"""
# header
## subheader

"""

{
    'key':'value'
    
}
list = [1,2,3]

st.write(list) 

st.sidebar.write('write tis sidebar')

df = pd.DataFrame (np.random.randn(40,20), columns=('col %d' % i for i in range(20)))

st.dataframe(df)