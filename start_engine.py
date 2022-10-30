from xmlrpc.server import SimpleXMLRPCServer
import logging
import argparse
import json
import pandas as pd

from src.data_loader import fetch_SchedGo
from src.cos_sim import cos_similarity
from src.engine import top_k_recomm


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HackerHub CourseReco-engine")
    parser.add_argument("--basedir", type=str, default="localhost", required=False)
    parser.add_argument("--port", type=int, default=8080, required=False)
    parser.add_argument("--mode", choices=["full", "ecs_mat_sta"], default="ecs_mat_sta", required=False)
    args = parser.parse_args()
    
    
    if args.mode == "ecs_mat_sta":
        obj = json.load(open("./data/ecs_mat_sta.json"))
    elif args.mode == "full":
        config = json.load(open("./config.json"))
        obj = fetch_SchedGo(config, "ucdavis", 202301)
    else:
        print("Unsupported mode, exits.")
    
    df = pd.DataFrame(obj)
    sim_mat = cos_similarity(df["description"])
    
    def top_k_recommendations(liked_course, k):
        return top_k_recomm(sim_mat, df["code"], liked_course, k)

    # start the engine server
    server = SimpleXMLRPCServer((args.basedir, args.port))
    print("Listening on port %i..." % args.port)
    server.register_function(top_k_recommendations, "top_k_recommendations")
    server.serve_forever()
