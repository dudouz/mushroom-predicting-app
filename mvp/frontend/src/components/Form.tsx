import React, { ChangeEvent } from "react";
import {
  CapShape,
  CapSurface,
  CapColor,
  Bruises,
  Odor,
  GillAttachment,
  GillSpacing,
  GillSize,
  GillColor,
  StalkShape,
  StalkRoot,
  StalkSurfaceAboveRing,
  StalkSurfaceBelowRing,
  StalkColorAboveRing,
  StalkColorBelowRing,
  VeilType,
  VeilColor,
  RingNumber,
  RingType,
  SporePrintColor,
  Population,
  Habitat,
} from "../enums/mushroom";
type PredictResult = "Edible" | "Poisonous";

export const Form = () => {
  const [capShape, setCapShape] = React.useState<CapShape>(CapShape.BELL);
  const [capSurface, setCapSurface] = React.useState<CapSurface>(
    CapSurface.FIBROUS
  );
  const [capColor, setCapColor] = React.useState<CapColor>(CapColor.BROWN);
  const [bruises, setBruises] = React.useState<Bruises>(Bruises.BRUISES);
  const [odor, setOdor] = React.useState<Odor>(Odor.ALMOND);
  const [gillAttachment, setGillAttachment] = React.useState<GillAttachment>(
    GillAttachment.ATTACHED
  );
  const [gillSpacing, setGillSpacing] = React.useState<GillSpacing>(
    GillSpacing.CLOSE
  );
  const [gillSize, setGillSize] = React.useState<GillSize>(GillSize.BROAD);
  const [gillColor, setGillColor] = React.useState<GillColor>(GillColor.BLACK);
  const [stalkShape, setStalkShape] = React.useState<StalkShape>(
    StalkShape.ENLARGING
  );
  const [stalkRoot, setStalkRoot] = React.useState<StalkRoot>(
    StalkRoot.BULBOUS
  );
  const [stalkSurfaceAboveRing, setStalkSurfaceAboveRing] =
    React.useState<StalkSurfaceAboveRing>(StalkSurfaceAboveRing.FIBROUS);
  const [stalkSurfaceBelowRing, setStalkSurfaceBelowRing] =
    React.useState<StalkSurfaceBelowRing>(StalkSurfaceBelowRing.FIBROUS);
  const [stalkColorAboveRing, setStalkColorAboveRing] =
    React.useState<StalkColorAboveRing>(StalkColorAboveRing.BROWN);
  const [stalkColorBelowRing, setStalkColorBelowRing] =
    React.useState<StalkColorBelowRing>(StalkColorBelowRing.BROWN);
  const [veilType, setVeilType] = React.useState<VeilType>(VeilType.PARTIAL);
  const [veilColor, setVeilColor] = React.useState<VeilColor>(VeilColor.BROWN);
  const [ringNumber, setRingNumber] = React.useState<RingNumber>(
    RingNumber.NONE
  );
  const [ringType, setRingType] = React.useState<RingType>(RingType.EVANESCENT);
  const [sporePrintColor, setSporePrintColor] = React.useState<SporePrintColor>(
    SporePrintColor.BLACK
  );
  const [population, setPopulation] = React.useState<Population>(
    Population.ABUNDANT
  );
  const [habitat, setHabitat] = React.useState<Habitat>(Habitat.GRASSES);

  const [results, setResults] = React.useState<{
    result: PredictResult;
  } | null>(null);

  const onSelectHandler = React.useCallback(
    (e: ChangeEvent<HTMLSelectElement>) => {
      switch (e.target.id) {
        case "cap-shape":
          setCapShape(e.target.value as CapShape);
          break;
        case "cap-surface":
          setCapSurface(e.target.value as CapSurface);
          break;
        case "cap-color":
          setCapColor(e.target.value as CapColor);
          break;
        case "bruises":
          setBruises(e.target.value as Bruises);
          break;
        case "odor":
          setOdor(e.target.value as Odor);
          break;
        case "gill-attachment":
          setGillAttachment(e.target.value as GillAttachment);
          break;
        case "gill-spacing":
          setGillSpacing(e.target.value as GillSpacing);
          break;
        case "gill-size":
          setGillSize(e.target.value as GillSize);
          break;
        case "gill-color":
          setGillColor(e.target.value as GillColor);
          break;
        case "stalk-shape":
          setStalkShape(e.target.value as StalkShape);
          break;
        case "stalk-root":
          setStalkRoot(e.target.value as StalkRoot);
          break;
        case "stalk-surface-above-ring":
          setStalkSurfaceAboveRing(e.target.value as StalkSurfaceAboveRing);
          break;
        case "stalk-surface-below-ring":
          setStalkSurfaceBelowRing(e.target.value as StalkSurfaceBelowRing);
          break;
        case "stalk-color-above-ring":
          setStalkColorAboveRing(e.target.value as StalkColorAboveRing);
          break;
        case "stalk-color-below-ring":
          setStalkColorBelowRing(e.target.value as StalkColorBelowRing);
          break;
        case "veil-type":
          setVeilType(e.target.value as VeilType);
          break;
        case "veil-color":
          setVeilColor(e.target.value as VeilColor);
          break;
        case "ring-number":
          setRingNumber(e.target.value as RingNumber);
          break;
        case "ring-type":
          setRingType(e.target.value as RingType);
          break;
        case "spore-print-color":
          setSporePrintColor(e.target.value as SporePrintColor);
          break;
        case "population":
          setPopulation(e.target.value as Population);
          break;
        case "habitat":
          setHabitat(e.target.value as Habitat);
          break;
        default:
          break;
      }
    },
    []
  );
  const onSubmitHandler = React.useCallback(
    async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();

      const data = {
        capShape,
        capSurface,
        capColor,
        bruises,
        odor,
        gillAttachment,
        gillSpacing,
        gillSize,
        gillColor,
        stalkShape,
        stalkRoot,
        stalkSurfaceAboveRing,
        stalkSurfaceBelowRing,
        stalkColorAboveRing,
        stalkColorBelowRing,
        veilType,
        veilColor,
        ringNumber,
        ringType,
        sporePrintColor,
        population,
        habitat,
      };

      await fetch("http://localhost:5000/api/evaluate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then(async (res) => {
          if (res.ok) {
            const data = await res.json();

            setResults(data);
          } else {
            console.log("Error");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    [
      capShape,
      capSurface,
      capColor,
      bruises,
      odor,
      gillAttachment,
      gillSpacing,
      gillSize,
      gillColor,
      stalkShape,
      stalkRoot,
      stalkSurfaceAboveRing,
      stalkSurfaceBelowRing,
      stalkColorAboveRing,
      stalkColorBelowRing,
      veilType,
      veilColor,
      ringNumber,
      ringType,
      sporePrintColor,
      population,
      habitat,
    ]
  );

  const clearResults = React.useCallback(() => setResults(null), []);

  const renderResult = React.useCallback((result: PredictResult) => {
    if (result === "Edible") {
      return (
        <div>
          <p>Este cogumelo é:</p>

          <hr />
          <p>Comestível</p>

          <button onClick={clearResults}>Tentar de novo</button>
        </div>
      );
    } else {
      return (
        <div>
          <p>Este cogumelo é:</p>

          <hr />
          <p>Venenoso</p>

          <button onClick={clearResults}>Tentar de novo</button>
        </div>
      );
    }
  }, []);

  React.useEffect(() => {
    console.log({
      capShape,
      capSurface,
      capColor,
      bruises,
      odor,
      gillAttachment,
      gillSpacing,
      gillSize,
      gillColor,
      stalkShape,
      stalkRoot,
      stalkSurfaceAboveRing,
      stalkSurfaceBelowRing,
      stalkColorAboveRing,
      stalkColorBelowRing,
      veilType,
      veilColor,
      ringNumber,
      ringType,
      sporePrintColor,
      population,
      habitat,
    });
  }, [
    bruises,
    capColor,
    capShape,
    capSurface,
    gillAttachment,
    gillColor,
    gillSize,
    gillSpacing,
    habitat,
    odor,
    population,
    ringNumber,
    ringType,
    sporePrintColor,
    stalkColorAboveRing,
    stalkColorBelowRing,
    stalkRoot,
    stalkShape,
    stalkSurfaceAboveRing,
    stalkSurfaceBelowRing,
    veilColor,
    veilType,
  ]);
  if (results) {
    return (
      <div>
        <h1>{renderResult(results.result)}</h1>
      </div>
    );
  }

  return (
    <form onSubmit={onSubmitHandler}>
      <div>
        <div className="select_wrapper">
          <label htmlFor="cap-shape">Formato do Chapéu</label>
          <select onChange={onSelectHandler} id="cap-shape">
            <option value={CapShape.BELL}>Sino</option>
            <option value={CapShape.CONICAL}>Cônico</option>
            <option value={CapShape.CONVEX}>Convexo</option>
            <option value={CapShape.FLAT}>Plano</option>
            <option value={CapShape.KNOBBED}>Abobadado</option>
            <option value={CapShape.SUNKEN}>Afundado</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="cap-surface">Superfície do Chapéu</label>
          <select onChange={onSelectHandler} id="cap-surface">
            <option value={CapSurface.FIBROUS}>Fibrosa</option>
            <option value={CapSurface.GROOVES}>Estrias</option>
            <option value={CapSurface.SCALY}>Escamosa</option>
            <option value={CapSurface.SMOOTH}>Lisa</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="cap-color">Cor do Chapéu</label>
          <select onChange={onSelectHandler} id="cap-color">
            <option value={CapColor.BROWN}>Marrom</option>
            <option value={CapColor.BUFF}>Bege</option>
            <option value={CapColor.CINNAMON}>Canela</option>
            <option value={CapColor.GRAY}>Cinza</option>
            <option value={CapColor.GREEN}>Verde</option>
            <option value={CapColor.PINK}>Rosa</option>
            <option value={CapColor.PURPLE}>Roxo</option>
            <option value={CapColor.RED}>Vermelho</option>
            <option value={CapColor.WHITE}>Branco</option>
            <option value={CapColor.YELLOW}>Amarelo</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="bruises">Machucados</label>
          <select onChange={onSelectHandler} id="bruises">
            <option value={Bruises.BRUISES}>Com Machucados</option>
            <option value={Bruises.NO}>Sem Machucados</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="odor">Odor</label>
          <select onChange={onSelectHandler} id="odor">
            <option value={Odor.ALMOND}>Amêndoa</option>
            <option value={Odor.ANISE}>Anis</option>
            <option value={Odor.CREOSOTE}>Creosoto</option>
            <option value={Odor.FISHY}>De Peixe</option>
            <option value={Odor.FOUL}>Fétido</option>
            <option value={Odor.MUSTY}>Mofado</option>
            <option value={Odor.NONE}>Nenhum</option>
            <option value={Odor.PUNGENT}>Acre</option>
            <option value={Odor.SPICY}>Picante</option>
          </select>
        </div>
      </div>
      <div>
        <div className="select_wrapper">
          <label htmlFor="gill-attachment">Anexo das Lamelas</label>
          <select onChange={onSelectHandler} id="gill-attachment">
            <option value={GillAttachment.ATTACHED}>Anexadas</option>
            <option value={GillAttachment.DESCENDING}>Descendentes</option>
            <option value={GillAttachment.FREE}>Livres</option>
            <option value={GillAttachment.NOTCHED}>Entalhadas</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="gill-spacing">Espaçamento das Lamelas</label>
          <select onChange={onSelectHandler} id="gill-spacing">
            <option value={GillSpacing.CLOSE}>Próximas</option>
            <option value={GillSpacing.CROWDED}>Aglomeradas</option>
            <option value={GillSpacing.DISTANT}>Distantes</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="gill-size">Tamanho das Lamelas</label>
          <select onChange={onSelectHandler} id="gill-size">
            <option value={GillSize.BROAD}>Largas</option>
            <option value={GillSize.NARROW}>Estreitas</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="gill-color">Cor das Lamelas</label>
          <select onChange={onSelectHandler} id="gill-color">
            <option value={GillColor.BLACK}>Pretas</option>
            <option value={GillColor.BROWN}>Marrons</option>
            <option value={GillColor.BUFF}>Bege</option>
            <option value={GillColor.CHOCOLATE}>Chocolate</option>
            <option value={GillColor.GRAY}>Cinza</option>
            <option value={GillColor.GREEN}>Verdes</option>
            <option value={GillColor.ORANGE}>Laranjas</option>
            <option value={GillColor.PINK}>Rosas</option>
            <option value={GillColor.PURPLE}>Roxas</option>
            <option value={GillColor.RED}>Vermelhas</option>
            <option value={GillColor.WHITE}>Brancas</option>
            <option value={GillColor.YELLOW}>Amarelas</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="stalk-shape">Formato do Estipe</label>
          <select onChange={onSelectHandler} id="stalk-shape">
            <option value={StalkShape.ENLARGING}>Alargando</option>
            <option value={StalkShape.TAPERING}>Afunilando</option>
          </select>
        </div>
      </div>
      <div>
        <div className="select_wrapper">
          <label htmlFor="stalk-root">Raiz do Estipe</label>
          <select onChange={onSelectHandler} id="stalk-root">
            <option value={StalkRoot.BULBOUS}>Bolbosa</option>
            <option value={StalkRoot.CLUB}>Clubada</option>
            <option value={StalkRoot.CUP}>Em Forma de Copo</option>
            <option value={StalkRoot.EQUAL}>Igual</option>
            <option value={StalkRoot.RHIZOMORPHS}>Rizomorfos</option>
            <option value={StalkRoot.ROOTED}>Enraizada</option>
            <option value={StalkRoot.MISSING}>Ausente</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="stalk-surface-above-ring">
            Superfície do Estipe Acima do Anel
          </label>
          <select onChange={onSelectHandler} id="stalk-surface-above-ring">
            <option value={StalkSurfaceAboveRing.FIBROUS}>Fibrosa</option>
            <option value={StalkSurfaceAboveRing.SCALY}>Escamosa</option>
            <option value={StalkSurfaceAboveRing.SILKY}>Sedosa</option>
            <option value={StalkSurfaceAboveRing.SMOOTH}>Lisa</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="stalk-surface-below-ring">
            Superfície do Estipe Abaixo do Anel
          </label>
          <select onChange={onSelectHandler} id="stalk-surface-below-ring">
            <option value={StalkSurfaceBelowRing.FIBROUS}>Fibrosa</option>
            <option value={StalkSurfaceBelowRing.SCALY}>Escamosa</option>
            <option value={StalkSurfaceBelowRing.SILKY}>Sedosa</option>
            <option value={StalkSurfaceBelowRing.SMOOTH}>Lisa</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="stalk-color-above-ring">
            Cor do Estipe Acima do Anel
          </label>
          <select onChange={onSelectHandler} id="stalk-color-above-ring">
            <option value={StalkColorAboveRing.BROWN}>Marrom</option>
            <option value={StalkColorAboveRing.BUFF}>Bege</option>
            <option value={StalkColorAboveRing.CINNAMON}>Canela</option>
            <option value={StalkColorAboveRing.GRAY}>Cinza</option>
            <option value={StalkColorAboveRing.ORANGE}>Laranja</option>
            <option value={StalkColorAboveRing.PINK}>Rosa</option>
            <option value={StalkColorAboveRing.RED}>Vermelho</option>
            <option value={StalkColorAboveRing.WHITE}>Branco</option>
            <option value={StalkColorAboveRing.YELLOW}>Amarelo</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="stalk-color-below-ring">
            Cor do Estipe Abaixo do Anel
          </label>
          <select onChange={onSelectHandler} id="stalk-color-below-ring">
            <option value={StalkColorBelowRing.BROWN}>Marrom</option>
            <option value={StalkColorBelowRing.BUFF}>Bege</option>
            <option value={StalkColorBelowRing.CINNAMON}>Canela</option>
            <option value={StalkColorBelowRing.GRAY}>Cinza</option>
            <option value={StalkColorBelowRing.ORANGE}>Laranja</option>
            <option value={StalkColorBelowRing.PINK}>Rosa</option>
            <option value={StalkColorBelowRing.RED}>Vermelho</option>
            <option value={StalkColorBelowRing.WHITE}>Branco</option>
            <option value={StalkColorBelowRing.YELLOW}>Amarelo</option>
          </select>
        </div>
      </div>
      <div>
        <div className="select_wrapper">
          <label htmlFor="veil-type">Tipo de Véu</label>
          <select onChange={onSelectHandler} id="veil-type">
            <option value={VeilType.PARTIAL}>Parcial</option>
            <option value={VeilType.UNIVERSAL}>Universal</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="veil-color">Cor do Véu</label>
          <select onChange={onSelectHandler} id="veil-color">
            <option value={VeilColor.BROWN}>Marrom</option>
            <option value={VeilColor.ORANGE}>Laranja</option>
            <option value={VeilColor.WHITE}>Branco</option>
            <option value={VeilColor.YELLOW}>Amarelo</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="ring-number">Número do Anel</label>
          <select onChange={onSelectHandler} id="ring-number">
            <option value={RingNumber.NONE}>Nenhum</option>
            <option value={RingNumber.ONE}>Um</option>
            <option value={RingNumber.TWO}>Dois</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="ring-type">Tipo de Anel</label>
          <select onChange={onSelectHandler} id="ring-type">
            <option value={RingType.EVANESCENT}>Evanescente</option>
            <option value={RingType.FLARING}>Alargado</option>
            <option value={RingType.LARGE}>Grande</option>
            <option value={RingType.NONE}>Nenhum</option>
            <option value={RingType.PENDANT}>Pendente</option>
            <option value={RingType.SHEATHING}>Envoltório</option>
            <option value={RingType.ZONE}>Zona</option>
          </select>
        </div>
      </div>
      <div>
        <div className="select_wrapper">
          <label htmlFor="spore-print-color">Cor da Impressão de Esporos</label>
          <select onChange={onSelectHandler} id="spore-print-color">
            <option value={SporePrintColor.BLACK}>Preta</option>
            <option value={SporePrintColor.BROWN}>Marrom</option>
            <option value={SporePrintColor.BUFF}>Bege</option>
            <option value={SporePrintColor.CHOCOLATE}>Chocolate</option>
            <option value={SporePrintColor.GREEN}>Verde</option>
            <option value={SporePrintColor.ORANGE}>Laranja</option>
            <option value={SporePrintColor.PURPLE}>Roxa</option>
            <option value={SporePrintColor.WHITE}>Branca</option>
            <option value={SporePrintColor.YELLOW}>Amarela</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="population">População</label>
          <select onChange={onSelectHandler} id="population">
            <option value={Population.ABUNDANT}>Abundante</option>
            <option value={Population.CLUSTERED}>Agrupada</option>
            <option value={Population.NUMEROUS}>Numerosa</option>
            <option value={Population.SCATTERED}>Espalhada</option>
            <option value={Population.SEVERAL}>Várias</option>
            <option value={Population.SOLITARY}>Solitária</option>
          </select>
        </div>
        <div className="select_wrapper">
          <label htmlFor="habitat">Habitat</label>
          <select onChange={onSelectHandler} id="habitat">
            <option value={Habitat.GRASSES}>Grama</option>
            <option value={Habitat.LEAVES}>Folhas</option>
            <option value={Habitat.MEADOWS}>Prados</option>
            <option value={Habitat.PATHS}>Caminhos</option>
            <option value={Habitat.URBAN}>Urbano</option>
            <option value={Habitat.WASTE}>Lixo</option>
            <option value={Habitat.WOODS}>Florestas</option>
          </select>
        </div>
      </div>
      <button>Enviar Dados</button>
    </form>
  );
};
