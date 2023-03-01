def breakingRecords(scores):
    # Write your code here
    maxx = minn = scores[0]
    high_score = 0
    low_score = 0
    for i in scores:
        if i > maxx:
            high_score += 1
            maxx = i
        if i < minn:
            low_score += 1
            minn = i
    return(high_score, low_score)
