//import { AnimateRoutes } from "Routes";
import { Home } from "./container/pages/Home";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import { AnimateRoutes } from "./Routes";
import { Provider } from "react-redux";
import store from "./store";

function App() {
  return (
    <Provider store={store}>
      <Router>
        <AnimateRoutes />
      </Router>
    </Provider>
  );
}

export default App;
