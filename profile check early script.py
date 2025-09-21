import pandas as pd
import io

df = pd.read_csv('profile_list.csv')
blocked_terms = open('BlockedBios.txt', 'r', encoding="utf-8").read().split(",")

def profile_check():
    handle = df[[df['Handle']]]
    for row in df.iterrows():
        if row["PFP"] == 'No':
         block_factor += 50
        num_follewers = df[[df['Followers']]]
        num_following = df[[df['Following']]]
        follow_ratio = num_follewers / num_following
        if follow_ratio < 0.1:
            block_factor += 50
        elif follow_ratio >= 0.1 and follow_ratio < 0.3:
            block_factor += 20
        bio = df[[df['BIO']]]
        for term in blocked_terms:
            if term + " " in bio or " " + term in bio:
                block_factor += 40

        if block_factor >= 110:
            print("blocked")
        elif block_factor < 110 and block_factor >= 60:
            creation_time = int(input("how many days ago was the account created?:"))
        if creation_time < 10:
            print("Account: " + handle + " is blocked.")
        elif creation_time >= 10:
            similar_acc = input("does the person have a similar name/pfp to another account? y/n:")
            if similar_acc == "y":
                print("Account: " + handle + " is blocked.")
            elif similar_acc == "n":
                print("allowed")                                                                        
        else:
            print("allowed")


print(df)
