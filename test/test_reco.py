import xmlrpc.client

k = 3
liked = ["MAT 127B", "ECS 020", "ECS 120", "STA 131A"]
list_subj = ["MAT", "ECS", "STA"]

with xmlrpc.client.ServerProxy("http://localhost:8080/") as proxy:
    for key in liked:
        print(key + ": " + str(proxy.top_k_recommendations(key, k, list_subj)))
