from xmlrpc.server import SimpleXMLRPCServer
import logging
import argparse

from src.fetch_data import get_from_csv
from src.cos_sim import cos_similarity
from src.engine import top_k_recomm

demo_file = "./data/demo_data.csv"

# ToDo: load and stored computed similarity matrix from storage

def top_k_recommendations(liked_course, k):
    
    df = get_from_csv(demo_file)
    sim_mat = cos_similarity(df["description"])
    return top_k_recomm(sim_mat, df["code"], liked_course, k)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HackerHub CourseReco-engine")
    parser.add_argument('--basedir', type=str, default="localhost", required=False)
    parser.add_argument('--port', type=int, default=8080, required=False)
    args = parser.parse_args()

    server = SimpleXMLRPCServer((args.basedir, args.port))
    print("Listening on port %i..." % args.port)
    server.register_function(top_k_recommendations, "top_k_recommendations")
    server.serve_forever()
