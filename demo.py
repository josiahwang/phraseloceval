import sys
sys.path.append("lib/");

from phraseloc.eval.evaluator import Evaluator
from phraseloc.eval.dataset import Dataset, DatasetLoader

def test():
	print("Loading toy dataset from JSON...");
	loader = DatasetLoader();
	gtDataset = loader.read_json("data/toydata/gt.json");
	print(">> {}".format(gtDataset.phrases));
	gtBoxList = gtDataset.boxes; # or equivalently dataset.get_boxlist();
	
	print("Loading toy predictions from JSON...");
	predDataset = loader.read_json("data/toydata/pred.json");
	predictedBoxList = predDataset.boxes;

	iouThreshold = 0.5;
	
	assert predDataset.size == gtDataset.size;
	
	print("Evaluating toy dataset...");
	evaluator = Evaluator();
	(accuracy, iouList) = evaluator.evaluate(predictedBoxList, gtBoxList, iouThreshold);
	print(">> Accuracy: {}".format(accuracy));
	for (pred, gt, iou) in zip(predictedBoxList, gtBoxList, iouList):
		print(">>>> GT: {}, PRED: {}, IoU: {}".format(gt, pred, iou));

if __name__ == "__main__":
	test();
