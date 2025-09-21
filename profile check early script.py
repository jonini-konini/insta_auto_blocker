import json

handle = input("Enter user handle: )
def profile_check():
    block_factor = 0
    pfp = input("does the person have a profile picture? y/n:")
    if pfp == "y":
        block_factor += 50
    num_follewers = int(input("how many followers does the person have?:"))
    num_following = int(input("how many people does the person follow?:"))
    follow_ratio = num_follewers / num_following
    if follow_ratio < 0.1:
        block_factor += 50
    num_posts = int(input("how many posts does the person have?:"))
    if num_posts < 5 and num_posts > 0:
        block_factor += 20
    elif num_posts == 0:
        block_factor +=50
    has_story = input("does the person have a story? y/n:")
    if has_story == "n":
        block_factor += 15
    elif has_story == "y":
        block_factor = block_factor
    has_bio = input("does the person have a bio? y/n:")
    if has_bio == "n":
        block_factor += 40
    elif has_bio == "y":
        dm = input("enter the bio info:")
        if dm == "DM for collabs ":
            block_factor += 20
    if block_factor >= 150:
        print("Account: " + handle + " is blocked.")
    elif block_factor < 150 and block_factor >= 100:
        creation_time = int(input("how many days ago was the account created?:"))
        if creation_time < 10:
            print("Account: " + handle + " is blocked.")
        elif creation_time >= 10:
            similar_acc = input("does the person have a similar name/pfp to another account? y/n:")
            if similar_acc == "y":
                print("Account: " + handle + " is blocked.")
            elif similar_acc == "n":
                print("Account: " + handle + " is allowed.")
    else:
        print("Account: " + handle + " is allowed.")


    
profile_check()
