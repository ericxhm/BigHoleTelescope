import json
import anytree
from tqdm import tqdm

# HELPER FUNCTIONS
def before_slash(s):
    """Returns: substring of s; up to, but not including, the first slash
    
    Parameter s: the string to slice
    Precondition: s is not empty"""
    if isinstance(s, str):
        inp = [s]
    else:
        inp = s
    beforeslash = []
    afterslash = []
    for st in inp:
        if '/' in st:
            end = st.index('/')
            afterslash.append(st[end+1:])
        else:
            end = len(st)
#             afterslash.append('')
        beforeslash.append(st[:end])
    return beforeslash, afterslash#[0]

def uniques(alist):
    """
    Returns: The unique elements in the list. 
    
    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list.
    """
    blist = alist[:]
    for x in alist:
        pos = blist.index(x)
        rest = blist[pos+1:]
        if rest.count(x)>0:
            blist.remove(x)

    return blist

def treeify(alist, lecture):
    """
    Turns concepts defined in alist into a tree, returns the top node
    """
    top = anytree.Node(lecture)
    nodes = {}
    names = []
    depth = finddepth(alist)

    for s in alist:
        st = s
        bef, aft = before_slash(st)
        if bef not in names:
            nodes['n{0}'.format(bef)] = anytree.Node(bef, parent=top)
            names.append(bef)
        for d in range(depth-1):
            bef, aft = before_slash(st)
            aft2 = before_slash(aft)[0]
            if aft2 not in names and len(aft2)!=0:
                nodes['n{0}'.format(aft2)] = anytree.Node(aft2, parent=nodes['n{0}'.format(bef)])
                names.append(aft2)
            if len(aft)!=0:
                st = aft
            else:
                break
    return top
        
def finddepth(alist):
    """
    Returns the maximum depth of the tree defined by concepts in alist
    """
    dep = 1
    for s in alist:
        dep = max(dep, s.count('/')+1)
    return dep


def processJSON(title="SML Lec 1_2.txt"):
    """
    Function to process JSON from Azure video indexer
    """
    # OPEN AND LOAD JSON INTO DICTIONARY
    with open(title, "r") as _file:
        new_dic = json.load(_file)
    insights = new_dic["summarizedInsights"]
    
    # GET ALL DICTIONARY KEYS FOR JSON
    keys = []
    for key, value in insights.items():
        keys.append(key)
    
    # print(keys)
    
    # GET ALL KEYWORDS
    keywords = []
    for k in insights["keywords"]:
        keywords.append(k["name"])
    
    print('Keywords: ', keywords, '\n')
    
    # GET ALL TOPICS
    topics = []
    for t in insights["topics"]:
        if len(topics)==0 or topics[-1] != t["name"]:
            topics.append(t["name"])
    
    print('Topics: ', topics, '\n')
        
    if '.txt' in title:
        title = title[:-4]
    top = treeify(topics, title)
    print(anytree.RenderTree(top, style=anytree.render.ContStyle()).by_attr())

if __name__ == '__main__':
    inp = input('Which lecture to index? Type here with .txt extension \n')
    processJSON(str(inp))
