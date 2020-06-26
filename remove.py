s=input("Enter a string:")
r=' '
for i in range(len(s)):
    if i%2==0:
        r=r+s[i]
print("Modified string is:",r)
