# Phrase Localization Evaluation Library 

By [Josiah Wang](http://www.josiahwang.com)


### Introduction

This repository contains the libraries and scripts used for evaluating phrase localization in my ICCV 2019 paper (Phrase Localization Without Paired Training Examples).

I found existing evaluation scripts for the phrase localization task difficult to setup and use. I only really needed to evaluate my output, not to run other people's models so that I can evaluate my output! Thus, this library was born! 

I wrote it in standard Python, so the script does not need any other dependencies. You only need to provide the script a list of ground truth bounding boxes and a list of predicted bounding boxes, and it will return the accuracy. I hope having a simple and standard evaluation script for the task will make life easier for everyone!


### Using the library

The library is a Python module located in the ``lib/`` directory. Please refer to the doc comments in the code for explanations and usage.

Ground truth annotations for various datasets are provided in the ``data/`` directory.

An example script is available as ``demo.py``.
 

### Citation

If you use this evaluation script, please cite the following work:

Josiah Wang and Lucia Specia (2019). **Phrase Localization Without Paired Training Examples**. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*.

	@InProceedings{WangSpecia:2019,
	author    = {Wang, Josiah and Specia, Lucia},
	title     = {Phrase Localization Without Paired Training Examples},
	booktitle = {Proceedings of the IEEE/CVF Internaitonal Conference on Computer Vision (ICCV)},
	publisher = {{IEEE}},
	month     = oct,
	year      = {2019},
	pages     = {},  
	address   = {Seoul, South Korea}
	}


### License

GNU General Public License v3.0


