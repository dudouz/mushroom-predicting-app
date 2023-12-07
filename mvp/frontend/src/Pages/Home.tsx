import * as React from "react";
import { Form, PredictResult } from "../components/Form";
import { FormTitle } from "../components/FormTitle";
import { MainImage } from "../components/MainImage";
import { Results } from "../components/Results";

export const Home: React.FC = () => {
  const [result, setResult] = React.useState<PredictResult | null>(null);

  const clearResults = React.useCallback(() => setResult(null), []);

  const setResultCallback = React.useCallback((result: PredictResult) => {
    setResult(result);
  }, []);

  if (result) {
    return <Results result={result} clearResults={clearResults} />;
  }

  return (
    <main>
      <MainImage />

      <section>
        <FormTitle />

        <Form setResult={setResultCallback} />
      </section>
    </main>
  );
};
