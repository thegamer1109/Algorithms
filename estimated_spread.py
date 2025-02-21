"""
In the social media industry, there is a concept called "spread": how much a post spreads due to "reshares" after all of the original author's followers see it. 
As it turns out, social media posts spread at an exponential rate! We've found that the estimated spread of a post can be calculated with this formula:

estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

In the formula above, average_audience_followers is an average calculated from each number within the audiences_followers argument - which is a list containing the individual follower counts of the author's followers. 
For example, if audiences_followers = [2, 3, 2, 19], then:

the author has 4 total followers
each follower has their own 2, 3, 2, and 19 followers, respectively.
Complete the get_estimated_spread function by implementing the formula above. The only input is audiences_followers, which is a list of the follower counts of all the followers the author has. 
Return the estimated spread. If the audiences_followers list is empty, return 0.
"""

def get_estimated_spread(audiences_followers):
    
    if len(audiences_followers) == 0:
        return 0
    
    # calc num of followers ([2, 3, 2, 19] = 4)
    
    num_followers = len(audiences_followers)
    
    # calc average followers for followers ([2, 3, 2, 19] = 6.5)
    
    temp = 0
    for i in audiences_followers:
        temp += i
    
    average_audience_followers = temp / num_followers
    
    # return estemated spread
    estimated_spread = average_audience_followers * ( num_followers ** 1.2 )
    
    return estimated_spread

if __name__ == '__main__':
    test = [2,3,2,19]
    
    print(get_estimated_spread(test))