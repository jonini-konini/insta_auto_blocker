import pandas as pd
import io

df = pd.read_csv('profile_list.csv')

def profile_check():
    for row in df.iterrows():
        if row['PFP'] == 'Yes':
            block_factor = 0
        elif row["PFP"] == 'No':
         block_factor += 50
        num_follewers = df[[df['Followers']]]
        num_following = df[[df['Following']]]
        follow_ratio = num_follewers / num_following
        if follow_ratio < 0.1:
            block_factor += 50
        elif follow_ratio >= 0.1 and follow_ratio < 0.3:
            block_factor += 20
        has_bio = input("does the person have a bio? y/n:")
        if has_bio == "n":
            block_factor += 40
        elif has_bio == "y":
            dm = input("enter the bio info:")
        if dm == "DM for collabs ":
            block_factor += 20
        if block_factor >= 150:
            print("blocked")
        elif block_factor < 150 and block_factor >= 100:
            creation_time = int(input("how many days ago was the account created?:"))
        if creation_time < 10:
            print("blocked")
        elif creation_time >= 10:
            similar_acc = input("does the person have a similar name/pfp to another account? y/n:")
            if similar_acc == "y":
                print("blocked")
            elif similar_acc == "n":
                print("allowed")
        else:
            print("allowed")


print(df)
