export type CamelCaseObject = Record<string, string>;

export function convertCamelToKebab(obj: CamelCaseObject): CamelCaseObject {
  const kebabObject: CamelCaseObject = {};

  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj.prototype, key)) {
      const kebabKey = key.replace(/([a-z])([A-Z])/g, "$1-$2").toLowerCase();
      kebabObject[kebabKey] = obj[key];
    }
  }

  return kebabObject;
}
