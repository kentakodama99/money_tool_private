module.exports = {
    preset: '@vue/cli-plugin-unit-jest',
    transform: {
      "^.+\.csv$": "./jest-csv-transformer.js",
    }
  }