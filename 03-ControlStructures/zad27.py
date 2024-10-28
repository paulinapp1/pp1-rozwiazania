facebook=True
twitter=False
instagram=True
#if facebook==True and twitter==True and instagram==True:
 #   print("A person can be a good influencer")
#elif facebook==False and twitter==False and instagram==False:
 #   print("A person can't be a good influencer")
#elif facebook==True and twitter==False and instagram==True:
 #   print("A person can be a good influencer")
if (facebook==True and twitter==True)or(facebook==True and instagram==True)or(instagram==True and twitter==True):
    print("A person can be a good influencer")
else:
    print("A person can't be a good influencer")


