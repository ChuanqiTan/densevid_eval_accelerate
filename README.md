# densevid_eval_accelerate
accelerate the speed of densevid_eval (https://github.com/ranjaykrishna/densevid_eval)

The origin code of densevid_eval runs too slow, we optimize these code.

## Run
our code:

> python2.7 new_process_data.py --test_type=new
  
origin code:

> python2.7 new_process_data.py --test_type=slow

## Results
For tiny_sample.json, run on my personal computer, "slow" method finish in 67s and our "new" method finish in 10s.
