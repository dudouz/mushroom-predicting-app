interface ExamplesProps {
  setPoisonousExample: () => void;
  setEdibleExample: () => void;
}

export const Examples: React.FC<ExamplesProps> = ({
  setEdibleExample,
  setPoisonousExample,
}) => {
  return (
    <div className="examples-wrapper">
      <h2>Exemplos</h2>

      <p>
        Sabemos que o formulário é longo então temos dois exemplos para validar
        o modelo mais rapidamente:
      </p>

      <div className="cards-wrapper">
        <div>
          <h3>Amanita Muscaria</h3>
          <p>Venenoso</p>

          <button onClick={setPoisonousExample}>Avaliar</button>
        </div>
        <div>
          <h3>Agaricus Campestris</h3>
          <p>Comestível</p>

          <button onClick={setEdibleExample}>Avaliar</button>
        </div>
      </div>
    </div>
  );
};
