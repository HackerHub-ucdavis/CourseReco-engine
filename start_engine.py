from xmlrpc.server import SimpleXMLRPCServer
import logging
import argparse
import json
import pandas as pd

from src.data_loader import fetch_SchedGo
from src.cos_sim import cos_similarity
from src.engine import top_k_recomm


def top_k_recommendations(liked_course, k, subjects):
    config = json.load(open("./config.json"))
    obj = fetch_SchedGo(config, "ucdavis", 202301, subjects)

    # save some memory
    df = pd.DataFrame(obj)
    sub_df = df[["description", "code"]]
    del df

    sim_mat = cos_similarity(sub_df["description"])
    return top_k_recomm(sim_mat, sub_df["code"], liked_course, k)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HackerHub CourseReco-engine")
    parser.add_argument("--basedir", type=str,
                        default="localhost", required=False)
    parser.add_argument("--port", type=int, default=8080, required=False)
    args = parser.parse_args()

    # start the engine server
    server = SimpleXMLRPCServer((args.basedir, args.port))
    print("Listening on port %i..." % args.port)
    server.register_function(top_k_recommendations, "top_k_recommendations")
    server.serve_forever()
