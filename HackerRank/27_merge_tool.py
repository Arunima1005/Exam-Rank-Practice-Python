# import textwrap
def merge_the_tools(string, k):
    # your code goes here
    # s = textwrap.fill(string, k)
    # print(s)
    st = []
    for i in range(0, len(string), k):
        st.append(string[i:i+k])
    # print(st)
    original=[]
    for v in st:
        result = ""
        for c in v:
            if c not in result:
                result += c
        original.append(result)
    for o in original:
        print(o)
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)