from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger

from datasets import load_metric

metric = load_metric("rouge",trust_remote_code=True)

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()