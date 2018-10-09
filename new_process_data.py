from __future__ import print_function
import argparse
import logging
import json
import time
from old_evaluate import old_ANETcaptions
from new_evaluate import new_ANETcaptions
from evaluate import ANETcaptions


parser = argparse.ArgumentParser(description='Eval of Dense Video Caption')
parser.add_argument('--test_file', type=str, default="tiny_sample.json", help='target file of predirect')
parser.add_argument('--test_type', type=str, default='new', help='test type (slow, fast, new)')
parser.add_argument('--log_level', type=int, default=30, help='log output level (DEFAULT:30, INFO:20, DEBUG:10)')
args = parser.parse_args()
print('=' * 80)
print(args)
print('=' * 80)


logging.basicConfig(level=args.log_level)


#generate score for the captioning
if (args.test_type == 'slow'):
	evaluator_func = old_ANETcaptions
elif(args.test_type == 'fast'):
	evaluator_func = ANETcaptions
elif (args.test_type == "new"):
	evaluator_func = new_ANETcaptions
else:
	raise RuntimeError("ERROR TEST TYPE")

start_t = time.time()
evaluator = evaluator_func(ground_truth_filenames=['./data/val_1.json', './data/val_2.json'],
					prediction_filename='./'+args.test_file,
					tious=[0.3, 0.5, 0.7, 0.9],
					max_proposals=1000,  # too much???
					verbose=True)
# verbose=args.verbose -> verbose = True
evaluator.evaluate()
end_t = time.time()
print(">>> time used: ", end_t-start_t, " seconds")


# Output the details
for i, tiou in enumerate([0.3, 0.5, 0.7, 0.9]):
	logging.info('-' * 80)
	logging.info("tIoU: {}".format(tiou))
	logging.info('-' * 80)
	for metric in evaluator.scores:
	    score = evaluator.scores[metric][i]
	    logging.info('| %s: %2.4f'%(metric, 100*score))


# Print the averages result
print('-' * 80)
print("Average across all tIoUs")
print('-' * 80)
for metric in evaluator.scores:
	score = evaluator.scores[metric]
	print('| %s: %2.4f'%(metric, 100 * sum(score) / float(len(score))))
print('-' * 80)
print(evaluator.scores)
