#import dataset
from pycaret.datasets import get_data
data = get_data('juice')

#init setup
from pycaret.classification import setup, compare_models, save_model, deploy_model
reg1 = setup(data, target = 'Purchase', logging=True, experiment_name = 'juice-script1', silent=True, html=False)

#compare models
c = compare_models(n_select=1)

#save model
save_model(c, model_name='tfdemo')

#deploy model on S3
deploy_model(c, model_name='tfdemo', platform='aws', authentication={'bucket' : 'pycaret-test'})