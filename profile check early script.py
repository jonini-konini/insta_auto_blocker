import pandas as pd
import io

df = pd.read_csv('profile_list.csv')
blocked_terms = open('BlockedBios.txt', 'r', encoding="utf-8").read().split(",")

def profile_check():
    block_factor = 0
    handle = df.set_index("Handle")
    for i in df.itertuples():
        if i[7].find("No") != -1:
         block_factor += 50
        num_follewers = i[4]
        num_following = i[5]
        follow_ratio = num_follewers / num_following
        if follow_ratio < 0.1:
            block_factor += 50
        elif follow_ratio >= 0.1 and follow_ratio < 0.3:
            block_factor += 20

        if block_factor >= 80:
            print("blocked")
        elif block_factor < 80 and block_factor >= 60:
            creation_time = i[9]
            if creation_time < 10:
                print("Account: " + handle + " is blocked.")
            elif creation_time >= 10:
                duplicate_rows = df[df.duplicated(subset=['User Name'], keep=False)]
                if not duplicate_rows.empty:
                 print("Account: " + handle + " is blocked.")
            else :
                print("Account: " + handle + " may require further inspection.")                                                                        
        else:
            print("allowed")

profile_check()