import requests


class TweetService:
    
    
    def __init__(self) -> None:
        self.tweet_url = "YOUR TWEET API KEY"
    
    
    def get_tweet(self, tweet_serach):
        
        tweet_take = tweet_serach.get()
        
        querystring = {"query":f"<{tweet_take}>"}
        
        headers = {
            "X-RapidAPI-Key": "YOUR RAPID KEY",
            "X-RapidAPI-Host": "YOUR RAPID HOST"
        }
        
        
        tweet_response = requests.get(self.tweet_url, headers=headers, params=querystring)
        json_tweet_data = tweet_response.json()
        data = json_tweet_data["timeline"]
        
        for main_data in data:
            name = main_data["screen_name"]
            date = main_data["created_at"]
            alinti = main_data["quotes"]
            like = main_data["favorites"]
            yer_isareti = main_data["bookmarks"]
            lang = main_data["lang"]
            retweet = main_data["retweets"]
            text = main_data["text"]
            
            
            params = {
                "SHEETY URL NİZİN SONUNDAKİ KELİMEYİ GİRİN" : {
                    "name" : name,
                    "date" : date,
                    "quotes" : alinti,
                    "like" : like,
                    "bookmarks" : yer_isareti,
                    "language" : lang,
                    "retweet" : retweet,
                    "tweet" : text
                }
            }
            
            sheets_url = "YOUR SHEETY URL"
            sheets_barrier = {"Authorization" : "YOUR SHEETY BARRIER CODE"}
            
            
            sheets_post = requests.post(sheets_url, json=params, headers=sheets_barrier)
        return sheets_post