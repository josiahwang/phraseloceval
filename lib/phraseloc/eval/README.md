# Evaluation script for image-text region correspondence

## Classes

### Dataset (defined in dataset.py)

### DatasetLoader (defined in dataset.py)

### Evaluator (defined in evaluate.py)

#### compute_iou()

#### accuracy()

#### evaluate()

Convenience function: compute_iou() followed by accuracy(). Returns both accuracy and per-instance iou. 

#### evaluate_perclass()

Like evaluate, but also returns the accuracy per category. Useful especialy for Flickr30kEntities evaluation.
