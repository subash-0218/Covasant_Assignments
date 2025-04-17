import requests

def helloj_post(url,obj):
    return requests.post(url,json=obj)
     
if __name__ == '__main__':
    url = "http://127.0.0.1:8000/helloj"
    obj = dict(name = "Subash",format="json")
    resp = helloj_post(url, obj)
    print(resp.json())
