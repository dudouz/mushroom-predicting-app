import React from "react";
import { PredictResult } from "./Form";

interface ResultsProps {
  result: PredictResult;
  clearResults: () => void;
}
export const Results: React.FC<ResultsProps> = ({ clearResults, result }) => {
  console.log(result);
  return (
    <div className="evaluation-results">
      {result === "Edible" ? <Edible /> : <Poisonous />}

      <button onClick={clearResults}>Tentar de novo</button>
    </div>
  );
};

const Edible: React.FC = () => {
  return (
    <div>
      <p>Este cogumelo é:</p>

      <img
        src="/edible-mushroom.jpg"
        alt="Comestível! Bom apetite!"
        width="300"
      />

      <h1>Comestível!</h1>

      <p>Parece saboroso, bom apetite!</p>
    </div>
  );
};

const Poisonous: React.FC = () => {
  return (
    <div>
      <p>Este cogumelo é:</p>

      <img src="/poisonous-mushroom.jpg" alt="Venenoso! Não coma" width="300" />

      <h1>Venenoso!</h1>

      <p>Talvez você consiga comer ele uma vez só na vida!</p>
    </div>
  );
};
