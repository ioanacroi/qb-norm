This repo provides code for *QB-Norm* ([```Cross Modal Retrieval with Querybank Normalisation```](https://vladbogo.github.io/QB-Norm/))

**Usage example**

```
python dynamic_inverted_softmax.py --sims_train_test_path msrvtt/tt-ce-train-captions-test-videos-seed0.pkl --sims_test_path msrvtt/tt-ce-test-captions-test-videos-seed0.pkl --test_query_masks_path msrvtt/tt-ce-test-query_masks.pkl
```

To test *QB-Norm* on your own data you need to:
1. Extract the similarity matrix between the caption from the training split and the videos from the testing split ``` path/to/sims/train/test```
2. Extract testing split similarity matrix (similarities between testing captions and testing video) ``` path/to/sims/test ```
3. Run *QB-Norm*
```
python dynamic_inverted_softmax.py --sims_train_test_path path/to/sims/train/test --sims_test_path path/to/sims/test
```

**Data**

The similarity matrices for each method were extracted using the official repositories as follows: [CE+](https://github.com/albanie/collaborative-experts), [TT-CE+](https://github.com/albanie/collaborative-experts), [CLIP2Video](https://github.com/CryhanFang/CLIP2Video), [CLIP4Clip](https://github.com/ArrowLuo/CLIP4Clip) (we used the official repo to train from scratch new models since they do not provide pre-trained weights).
You can download the extracted similarity matrices for training and testing here: [MSRVTT](http:/www.robots.ox.ac.uk/~vgg/research/teachtext/QB-Norm/msrvtt-sims.tar.gz), [MSVD](/projects/vgg/vgg/WWW/research/teachtext/QB-Norm/msvd-sims.tar.gz), [DiDeMo](/projects/vgg/vgg/WWW/research/teachtext/QB-Norm/didemo-sims.tar.gz), [LSMDC](/projects/vgg/vgg/WWW/research/teachtext/QB-Norm/lsmdc-sims.tar.gz).

**QB-Norm Results on MSRVTT Benchmark**

| Model | Split | Task | R@1 | R@5 | R@10 | MdR | Geom |
| ----- | ------| ---- | --- | --- | ---- | --- | --- |
| CE+   | Full | t2v | <sub><sup>14.4<sub>(0.1)</sub></sup></sub> | <sub><sup>37.4<sub>(0.1)</sub></sup></sub> | <sub><sup>50.2<sub>(0.1)</sub></sup></sub> | <sub><sup>10.0<sub>(0.0)</sub></sup></sub> | <sub><sup>30.0<sub>(0.1)</sub></sup></sub> |
| CE+ (+QB-Norm) | Full | t2v | <sub><sup>16.4<sub>(0.0)</sub></sup></sub> | <sub><sup>40.3<sub>(0.1)</sub></sup></sub> | <sub><sup>52.9<sub>(0.1)</sub></sup></sub> | <sub><sup>9.0<sub>(0.0)</sub></sup></sub> | <sub><sup>32.7<sub>(0.1)</sub></sup></sub> |
| TT-CE+    | Full  | t2v  | <sub><sup>14.9<sub>(0.1)</sub></sup></sub> | <sub><sup>38.3<sub>(0.1)</sub></sup></sub> | <sub><sup>51.5<sub>(0.1)</sub></sup></sub> | <sub><sup>10.0<sub>(0.0)</sub></sup></sub> | <sub><sup>30.9<sub>(0.1)</sub></sup></sub> |
| TT-CE+ (+QB-Norm) | Full | t2v | <sub><sup>17.3<sub>(0.0)</sub></sup></sub> | <sub><sup>42.1<sub>(0.2)</sub></sup></sub> | <sub><sup>54.9<sub>(0.1)</sub></sup></sub> | <sub><sup>8.0<sub>(0.0)</sub></sup></sub> | <sub><sup>34.2<sub>(0.1)</sub></sup></sub> |

**QB-Norm Results on MSVD Benchmark**

| Model | Split | Task | R@1 | R@5 | R@10 | MdR | Geom |
| ----- | ------| ---- | --- | --- | ---- | --- | --- |
| TT-CE+ | Full | t2v | <sub><sup>25.4<sub>(0.3)</sub></sup></sub> | <sub><sup>56.9<sub>(0.4)</sub></sup></sub> | <sub><sup>71.3<sub>(0.2)</sub></sup></sub> | <sub><sup>4.0<sub>(0.0)</sub></sup></sub> | <sub><sup>46.9<sub>(0.3)</sub></sup></sub> |
| TT-CE+ (+QB-Norm) | Full | t2v | <sub><sup>26.6<sub>(1.0)</sub></sup></sub> | <sub><sup>58.6<sub>(1.3)</sub></sup></sub> | <sub><sup>71.8<sub>(1.1)</sub></sup></sub> | <sub><sup>4.0<sub>(0.0)</sub></sup></sub> | <sub><sup>48.2<sub>(1.2)</sub></sup></sub> |
| CLIP2Video | Full | t2v | <sub><sup>47.0</sup></sub> | <sub><sup>76.8</sup></sub> | <sub><sup>85.9</sup></sub> | <sub><sup>2.0</sup></sub> | <sub><sup>67.7</sup></sub> |
| CLIP2Video (+QB-Norm) | Full | t2v| <sub><sup>48.0</sup></sub> | <sub><sup>77.9</sup></sub> | <sub><sup>86.2</sup></sub> | <sub><sup>2.0</sup></sub> | <sub><sup>68.5</sup></sub> |

**QB-Norm Results on DiDeMo Benchmark**

| Model | Split | Task | R@1 | R@5 | R@10 | MdR | Geom |
| ----- | ------| ---- | --- | --- | ---- | --- | --- |
| TT-CE+ | Full | t2v | <sub><sup>21.6<sub>(0.7)</sub></sup></sub> | <sub><sup>48.6<sub>(0.4)</sub></sup></sub> | <sub><sup>62.9<sub>(0.6)</sub></sup></sub> | <sub><sup>6.0<sub>(0.0)</sub></sup></sub> | <sub><sup>40.4<sub>(0.4)</sub></sup></sub> |
| TT-CE+ (+QB-Norm) | Full | t2v | <sub><sup>24.2<sub>(0.7)</sub></sup></sub> | <sub><sup>50.8<sub>(0.7)</sub></sup></sub> | <sub><sup>64.4<sub>(0.1)</sub></sup></sub> | <sub><sup>5.3<sub>(0.5)</sub></sup></sub> | <sub><sup>43.0<sub>(0.2)</sub></sup></sub> |
| CLIP4Clip | Full | t2v | <sub><sup>43.0</sup></sub> | <sub><sup>70.5</sup></sub> | <sub><sup>80.0</sup></sub> | <sub><sup>2.0</sup></sub> | <sub><sup>62.4</sup></sub> |
| CLIP4Clip (+QB-Norm) | Full | t2v | <sub><sup>43.5</sup></sub> | <sub><sup>71.4</sup></sub> | <sub><sup>80.9</sup></sub> | <sub><sup>2.0</sup></sub> | <sub><sup>63.1</sup></sub> |

**QB-Norm Results on LSMDC Benchmark**

| Model | Split | Task | R@1 | R@5 | R@10 | MdR | Geom |
| ----- | ------| ---- | --- | --- | ---- | --- | --- |
| TT-CE+ | Full | t2v | <sub><sup>17.2<sub>(0.4)</sub></sup></sub> | <sub><sup>36.5<sub>(0.6)</sub></sup></sub> | <sub><sup>46.3<sub>(0.3)</sub></sup></sub> | <sub><sup>13.7<sub>(0.5)</sub></sup></sub> | <sub><sup>30.7<sub>(0.3)</sub></sup></sub> |
| TT-CE+ (+QB-Norm) | Full | t2v | <sub><sup>17.8<sub>(0.4)</sub></sup></sub> | <sub><sup>37.7<sub>(0.5)</sub></sup></sub> | <sub><sup>47.6<sub>(0.6)</sub></sup></sub> | <sub><sup>12.7<sub>(0.5)</sub></sup></sub> | <sub><sup>31.7<sub>(0.3)</sub></sup></sub> |
| CLIP4Clip | Full | t2v | <sub><sup>21.3</sup></sub> | <sub><sup>40.0</sup></sub> | <sub><sup>49.5</sup></sub> | <sub><sup>11.0</sup></sub> | <sub><sup>34.8</sup></sub> |
| CLIP4Clip (+QB-Norm) | Full | t2v | <sub><sup>22.4</sup></sub> | <sub><sup>40.1</sup></sub> | <sub><sup>49.5</sup></sub> | <sub><sup>11.0</sup></sub> | <sub><sup>35.4</sup></sub> |


### References

If you find this code useful or use the extracted similarity matrices, please consider citing:

```
TODO
```
