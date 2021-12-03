#%%
# preorder
def DFS_pre(v):
    if v>7:
        return
    else:  
        print(v, end=' ')
        DFS_pre(v*2) # left node
        DFS_pre(v*2+1) # right node
        
if __name__=="__main__":
    DFS_pre(1)

# %%
# inorder
def DFS_in(v):
    if v>7:
        return
    else:  
        DFS_in(v*2) # left node
        print(v, end=' ')
        DFS_in(v*2+1) # right node
        
if __name__=="__main__":
    DFS_in(1)

# %%
# postorder
def DFS_pos(v):
    if v>7:
        return
    else:  
        DFS_pos(v*2) # left node
        DFS_pos(v*2+1) # right node
        print(v, end=' ')
        
if __name__=="__main__":
    DFS_pos(1)
