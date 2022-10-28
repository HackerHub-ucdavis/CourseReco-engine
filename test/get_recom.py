import xmlrpc.client

k = 3
liked = ["MAT 135A", "ECS 154", "ECS 120", "STA 131A"]

with xmlrpc.client.ServerProxy("http://localhost:8080/") as proxy:
    for key in liked:
        print(key + ": " + str(proxy.top_k_recommendations(key, k)))
