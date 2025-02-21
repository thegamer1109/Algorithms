'''
"fitness" influencers: follower count quadruples each month
"cosmetic" influencers: follower count triples each month
All other influencers: follower count doubles each month

For example, if a fitness influencer starts with 10 followers, then after 1 month they should have 40 followers. After 2 months, they would have 160 followers; etc.

Use a geometric sequence formula that's slightly modified for this problem: total = a1 * r**n >  starting_value * rate^months
'''

def get_follower_prediction(follower_count, influencer_type, num_months):
    
    if influencer_type == "fitness":
        return follower_count * 4**num_months
    if influencer_type == "cosmetic":
        return follower_count * 3**num_months
    else:
        return follower_count * 2**num_months

# better way
'''
# Define the multiplier rates for each influencer type
    rates = {
        "fitness": 4,
        "cosmetic": 3
    }
    # Default rate for other influencer types is 2
    rate = rates.get(influencer_type, 2)
    return follower_count * (rate ** num_months)
'''