import argparse
import pickle as pkl
import numpy as np
import metric

# Returns list of retrieved top k videos based on the sims matrix
def get_retrieved_videos(sims, k):
    argm = np.argsort(-sims, axis=1)
    topk = argm[:,:k].reshape(-1)
    retrieved_videos = np.unique(topk)
    return retrieved_videos

# Returns list of indices to normalize from sims based on videos
def get_index_to_normalize(sims, videos):
    argm = np.argsort(-sims, axis=1)[:,0]
    result = np.array(list(map(lambda x: x in videos, argm)))
    result = np.nonzero(result)
    return result

def qb_norm(train_test, test_test, args):
    k = args.get("k", 1)
    beta = args.get("beta", 20)
    retrieved_videos = get_retrieved_videos(train_test, k)
    test_test_normalized = test_test
    train_test = np.exp(train_test*beta)
    test_test = np.exp(test_test*beta)

    normalizing_sum = np.sum(train_test, axis=0)
    index_for_normalizing = get_index_to_normalize(test_test, retrieved_videos)
    test_test_normalized[index_for_normalizing, :] = \
        np.divide(test_test[index_for_normalizing, :], normalizing_sum)
    return test_test_normalized

def main():
    args = argparse.ArgumentParser(description= \
            'QB-Norm and Dynamic Inverted Softmax')
    args.add_argument("--sims_train_test_path", type=str, required=True, \
            help="path to the similarity matrix between the captions from training and the videos from testing")
    args.add_argument("--sims_test_path", type=str, required=True, \
            help="path to the similarity matrix between the captions from testing and the videos from testing, this is the original matrix used for computing the metrics")
    args.add_argument("--test_query_masks_path",
            type=str, default=None,
            help="path to the query masks")
    args.add_argument("--beta", default=20.0, type=float)
    args.add_argument("--k", default=1, type=float)
    args = vars(args.parse_args())

    train_test = pkl.load(open(args["sims_train_test_path"], 'rb'))
    test_test = pkl.load(open(args["sims_test_path"], 'rb'))
    msg = "Expected train_test_matrix.shape[1] == test_matrix.shape[1]"
    assert train_test.shape[1] == test_test.shape[1], msg
    test_query_masks_path = args.get("test_query_masks_path", None)
    if test_query_masks_path:
        test_query_masks = pkl.load(open(test_query_masks_path, 'rb'))
    else:
        test_query_masks = None

    print("Metrics before applying QB-Norm")
    print(metric.t2v_metrics(test_test, test_query_masks))

    test_test_normalized = qb_norm(train_test, test_test, args)
    print("Metrics after QB-Norm")
    print(metric.t2v_metrics(test_test_normalized, test_query_masks))

if __name__ == '__main__':
    main()
