# TODO change
caffe_dir = '/home/ruthfong/sample_code/Caffe-ExcitationBP/'
alexnet_prototxt = '/home/ruthfong/packages/caffe/models/bvlc_reference_caffenet/deploy_force_backward.prototxt'
alexnet_model = '/home/ruthfong/packages/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
googlenet_prototxt = '/home/ruthfong/packages/caffe/models/bvlc_googlenet/deploy_force_backward.prototxt'
googlenet_model = '/home/ruthfong/packages/caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel'


# default hyperparameters for optimize_mask.py
num_iters = 300
lr = 1e-1
l1_lambda = 1e-4
l1_ideal = 1
l1_lambda_2 = 0
tv_lambda = 1e-2
tv_beta = 3
jitter = 4
num_top = 0
noise = 0
null_type = 'blur'
given_gradient = True
norm_score = False
end_layer = 'prob'
use_conv_norm = False
blur_mask = 5
mask_scale = 8
