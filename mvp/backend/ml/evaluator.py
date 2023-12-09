from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Evaluator:
    def evaluate_model_scores(self, model, X, y):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predictions = model.predict(X)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return (accuracy_score(y, predictions),
                recall_score(y, predictions, average='binary'),
                precision_score(y, predictions, average='binary'),
                f1_score(y, predictions, average='binary'))
