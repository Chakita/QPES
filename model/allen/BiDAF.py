import argparse

def Bidaf(context,question):
  from allennlp.predictors.predictor import Predictor
  import allennlp_models.rc
  predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-model-2020.03.19.tar.gz")
  answer=predictor.predict(passage=context,question=question)["best_span_str"]
  return answer
  
parser = argparse.ArgumentParser(description="BiDAF based QnA model")
parser.add_argument("question",metavar="question",type=str,nargs=1,help="Enter your question")
all_args=parser.parse_args()
question=all_args.question[0]
with open("../data/pes-corpus.txt") as infile:
    context = infile.read().strip()
bidaf_answer=Bidaf(context,question)
print(bidaf_answer,"\n")
