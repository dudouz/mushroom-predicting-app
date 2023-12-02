import "./App.scss";
import { Form } from "./components/Form";
import { FormTitle } from "./components/FormTitle";

function App() {
  return (
    <main>
      <h1>Será que posso comer esse cogumelo?</h1>

      <section>
        <FormTitle />

        <Form />
      </section>
    </main>
  );
}

export default App;
