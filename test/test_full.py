import xmlrpc.client

k = 3
liked = ["AAS 050", "AAS 107B"]

with xmlrpc.client.ServerProxy("http://localhost:8080/") as proxy:
    for key in liked:
        print(key + ": " + str(proxy.top_k_recommendations(key, k)))
