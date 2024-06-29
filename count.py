def count_chars(s):
    dch=dict()
    for ch in s:
        if ch in dch:
            dch[ch]+=1
        else:
            dch[ch]=1
     return dch
st=input('enter a string')
t=st.split()
cnt=count_chars(t)
for k in cnt:
    print(k,cnt[k])
    
