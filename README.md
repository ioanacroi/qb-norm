**Usage example**
```
dynamic_inverted_softmax.py --sims_train_test_path msrvtt/tt-ce-train-captions-test-videos-seed0.pkl --sims_test_path msrvtt/tt-ce-test-captions-test-videos-seed0.pkl --test_query_masks_path msrvtt/tt-ce-test-query_masks.pkl
```

**Data**
The similarity matrices for CE+ and TT-CE+ were extracted using the weights and data provided in their [official repo](https://github.com/albanie/collaborative-experts).
You can download the extracted similarity matrices for training and testing here:
```
For MSRVTT
http:/www.robots.ox.ac.uk/~vgg/research/teachtext/QB-Norm/msrvtt-sims.tar.gz
```

**QB-Norm Results on MSRVTT Benchmark**

| Model | Split | Task | R@1 | R@5 | R@10 | MdR | Geom |
| ----- | ------| ---- | --- | --- | ---- | --- | --- |
| CE+   | Full | t2v | <sub><sup>14.4<sub>(0.1)</sub></sup></sub> | <sub><sup>37.4<sub>(0.1)</sub></sup></sub> | <sub><sup>50.2<sub>(0.1)</sub></sup></sub> | <sub><sup>10.0<sub>(0.0)</sub></sup></sub> | <sub><sup>30.0<sub>(0.1)</sub></sup></sub> |
| CE+ (+QB-Norm) | Full | t2v | <sub><sup>16.4<sub>(0.0)</sub></sup></sub> | <sub><sup>40.3<sub>(0.1)</sub></sup></sub> | <sub><sup>52.9<sub>(0.1)</sub></sup></sub> | <sub><sup>9.0<sub>(0.0)</sub></sup></sub> | <sub><sup>32.7<sub>(0.1)</sub></sup></sub> |
| TT-CE+    | Full  | t2v  | <sub><sup>14.9<sub>(0.1)</sub></sup></sub> | <sub><sup>38.3<sub>(0.1)</sub></sup></sub> | <sub><sup>51.5<sub>(0.1)</sub></sup></sub> | <sub><sup>10.0<sub>(0.0)</sub></sup></sub> | <sub><sup>30.9<sub>(0.1)</sub></sup></sub> |
| TT-CE+ (+QB-Norm) | Full | t2v | <sub><sup>17.3<sub>(0.0)</sub></sup></sub> | <sub><sup>42.1<sub>(0.2)</sub></sup></sub> | <sub><sup>54.9<sub>(0.1)</sub></sup></sub> | <sub><sup>8.0<sub>(0.0)</sub></sup></sub> | <sub><sup>34.2<sub>(0.1)</sub></sup></sub> |



