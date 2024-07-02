// eslint.config.js
// Configuration assistance provided by ChatGPT from OpenAI

import eslintPluginPrettier from "eslint-plugin-prettier";
import eslintPluginHtml from "eslint-plugin-html";
import eslintPluginCssModules from "eslint-plugin-css-modules";

export default [
  {
    files: ["**/*.html", "**/*.js"], // Lint HTML and JS files only
    ignores: [
      "myenv/**",
      "node_modules/**",
      "dist/**",
      "**/vendor/**",
      "**/admin/**",
      "myenv/lib/python3.8/site-packages/django/**", // Ignore all Django-related files in the environment
    ], // Exclude unnecessary directories
    languageOptions: {
      ecmaVersion: 2021, // Use ECMAScript 2021 features
      sourceType: "module", // Use ECMAScript modules
    },
    plugins: {
      prettier: eslintPluginPrettier, // Use the Prettier plugin
      html: eslintPluginHtml, // Use the HTML plugin
      "css-modules": eslintPluginCssModules, // Use CSS Modules plugin for linting CSS
    },
    rules: {
      "prettier/prettier": "error", // Show Prettier issues as errors
      "no-unused-vars": "warn", // Warn about unused variables
    },
    settings: {
      "html/html-extensions": [".html"], // Apply HTML plugin to .html files
    },
    linterOptions: {
      reportUnusedDisableDirectives: true, // Report unused eslint-disable directives
    },
  },
];
