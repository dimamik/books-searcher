from api.server import run_server
from recommender_logic.wrapper_recommender import WrapperRecommender

recommender = WrapperRecommender(10000, 10000)

if __name__ == '__main__':
    # Load data to cache from server
    run_server()
    pass
