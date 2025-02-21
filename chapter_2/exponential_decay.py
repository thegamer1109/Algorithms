'''
Complete the decayed_followers function.

It calculates the final value of a quantity after a certain time has passed, given its initial value and a rate of decay. Return the remaining followers.

remaining_total = quantity * ( retention_rate ^ time )

>>>>>>>>>>>>>>>>>>>>>>>>> The retention_rate is the opposite of fraction_lost_daily. If an influencer lost 0.2 (or 20%) of their followers each day, then the retention rate would be 0.8 (or 80%). <<<<<<<<<<<<<<<<<<<<<<

Example
intl_followers = 100

fraction_lost_daily = 0.5

After 0 days: 100 followers

After 1 day: 50 followers

After 2 days: 25 followers

After 3 days: 12.5 followers (rounded down)
'''

def decayed_followers(intl_followers, fraction_lost_daily, days):
    if fraction_lost_daily == 0:
        return intl_followers
    
    cntdwn = days
    current_followers = intl_followers
    while cntdwn > 0:
        current_followers = current_followers*(1-fraction_lost_daily)
        cntdwn -= 1
    return current_followers

if __name__ == '__main__':
    print(decayed_followers(1200, .09, 16))

# better way
'''
def decayed_followers(intl_followers, fraction_lost_daily, days):
    retention_rate = 1 - fraction_lost_daily
    return int(intl_followers * (retention_rate ** days))
'''