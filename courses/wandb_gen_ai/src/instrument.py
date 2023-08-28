"""
Note: This is not a functioning code but a template for how to instrument a wandb experiement
"""

import wandb

config  = { "learning_rate": 0.001}

# start a wandb run
wandb.init(project='test', config=config)

# model training
# Train your model here

# Log the metrics
wandb.log({"loss": loss})

wandb.finish()
