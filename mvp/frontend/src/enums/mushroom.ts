enum CapShape {
  BELL = "b",
  CONICAL = "c",
  CONVEX = "x",
  FLAT = "f",
  KNOBBED = "k",
  SUNKEN = "s",
}

enum CapSurface {
  FIBROUS = "f",
  GROOVES = "g",
  SCALY = "y",
  SMOOTH = "s",
}

enum CapColor {
  BROWN = "n",
  BUFF = "b",
  CINNAMON = "c",
  GRAY = "g",
  GREEN = "r",
  PINK = "p",
  PURPLE = "u",
  RED = "e",
  WHITE = "w",
  YELLOW = "y",
}

enum Bruises {
  BRUISES = "t",
  NO = "f",
}

enum Odor {
  ALMOND = "a",
  ANISE = "l",
  CREOSOTE = "c",
  FISHY = "y",
  FOUL = "f",
  MUSTY = "m",
  NONE = "n",
  PUNGENT = "p",
  SPICY = "s",
}

enum GillAttachment {
  ATTACHED = "a",
  DESCENDING = "d",
  FREE = "f",
  NOTCHED = "n",
}

enum GillSpacing {
  CLOSE = "c",
  CROWDED = "w",
  DISTANT = "d",
}

enum GillSize {
  BROAD = "b",
  NARROW = "n",
}

enum GillColor {
  BLACK = "k",
  BROWN = "n",
  BUFF = "b",
  CHOCOLATE = "h",
  GRAY = "g",
  GREEN = "r",
  ORANGE = "o",
  PINK = "p",
  PURPLE = "u",
  RED = "e",
  WHITE = "w",
  YELLOW = "y",
}

enum StalkShape {
  ENLARGING = "e",
  TAPERING = "t",
}

enum StalkRoot {
  BULBOUS = "b",
  CLUB = "c",
  CUP = "u",
  EQUAL = "e",
  RHIZOMORPHS = "z",
  ROOTED = "r",
  MISSING = "?",
}

enum StalkSurfaceAboveRing {
  FIBROUS = "f",
  SCALY = "y",
  SILKY = "k",
  SMOOTH = "s",
}

enum StalkSurfaceBelowRing {
  FIBROUS = "f",
  SCALY = "y",
  SILKY = "k",
  SMOOTH = "s",
}

enum StalkColorAboveRing {
  BROWN = "n",
  BUFF = "b",
  CINNAMON = "c",
  GRAY = "g",
  ORANGE = "o",
  PINK = "p",
  RED = "e",
  WHITE = "w",
  YELLOW = "y",
}

enum StalkColorBelowRing {
  BROWN = "n",
  BUFF = "b",
  CINNAMON = "c",
  GRAY = "g",
  ORANGE = "o",
  PINK = "p",
  RED = "e",
  WHITE = "w",
  YELLOW = "y",
}

enum VeilType {
  PARTIAL = "p",
  UNIVERSAL = "u",
}

enum VeilColor {
  BROWN = "n",
  ORANGE = "o",
  WHITE = "w",
  YELLOW = "y",
}

enum RingNumber {
  NONE = "n",
  ONE = "o",
  TWO = "t",
}

enum RingType {
  // COBWEBBY = "c", // esse deu erro no treinamnento, nao é minha culpa.
  EVANESCENT = "e",
  FLARING = "f",
  LARGE = "l",
  NONE = "n",
  PENDANT = "p",
  SHEATHING = "s",
  ZONE = "z",
}

enum SporePrintColor {
  BLACK = "k",
  BROWN = "n",
  BUFF = "b",
  CHOCOLATE = "h",
  GREEN = "r",
  ORANGE = "o",
  PURPLE = "u",
  WHITE = "w",
  YELLOW = "y",
}

enum Population {
  ABUNDANT = "a",
  CLUSTERED = "c",
  NUMEROUS = "n",
  SCATTERED = "s",
  SEVERAL = "v",
  SOLITARY = "y",
}

enum Habitat {
  GRASSES = "g",
  LEAVES = "l",
  MEADOWS = "m",
  PATHS = "p",
  URBAN = "u",
  WASTE = "w",
  WOODS = "d",
}

export {
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
};
