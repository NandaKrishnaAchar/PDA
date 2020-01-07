import json
import gzip

rating=[]
review_text=[]
i=0
j=0
g = gzip.open('Industrial_and_Scientific.json.gz', 'rb')
for l in g:
    b=(str(l[:-1])[2:-1])
    if(j<10000):
        try:
            res = json.loads(b)
            review_text.append(res['reviewText'])
            rating.append(res['overall'])
            j=j+1
            
        except:
            i=i+1
    else:
        print(i,"Sentences removed.\n10,000 review text and rating samples created.")
        print("Rating List Size: ",len(rating)," Review Text Size: ",len(review_text))
        print("Done!!")
        break

