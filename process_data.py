import json
from old_evaluate import old_ANETcaptions
from evaluate import ANETcaptions
import operator



	
   
name_id = 'small_sample.json'
evaluation_type = 'fast'

#generate score for the captioning
if (evaluation_type == 'slow'):
	evaluator = old_ANETcaptions(ground_truth_filenames=['./data/val_1.json', './data/val_2.json'],
	                 prediction_filename='./'+name_id,
	                 tious=[0.3, 0.5, 0.7, 0.9],
	                 max_proposals=1000,
	                 verbose=True)
elif(evaluation_type == 'fast'):
	evaluator = ANETcaptions(ground_truth_filenames=['./data/val_1.json', './data/val_2.json'],
	                 prediction_filename='./'+name_id,
	                 tious=[0.3, 0.5, 0.7, 0.9],
	                 max_proposals=1000,
	                 verbose=True)
# verbose=args.verbose -> verbose = True
evaluator.evaluate()


# Output the results
for i, tiou in enumerate([0.3, 0.5, 0.7, 0.9]):
	print '-' * 80
	print "tIoU: " , tiou
	print '-' * 80
	for metric in evaluator.scores:
	    score = evaluator.scores[metric][i]
	    print '| %s: %2.4f'%(metric, 100*score)


# Print the averages
print '-' * 80
print "Average across all tIoUs"
print '-' * 80
for metric in evaluator.scores:
	score = evaluator.scores[metric]
	print '| %s: %2.4f'%(metric, 100 * sum(score) / float(len(score)))
#print '-' * 80
#print(evaluator.scores)
