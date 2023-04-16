import {
  BrowserRouter as Router,
  Routes,
  Route,
  useLocation,
} from "react-router-dom";

import React from "react";
import { Error404 } from "./container/error/Error404.jsx";
import { Home } from "./container/pages/Home.jsx";

export const AnimateRoutes = () => {
  const location = useLocation();

  return (
    <Routes location={location} key={location.pathname}>
      <Route path="*" element={<Error404 />} />
      <Route path="/" element={<Home />}></Route>
    </Routes>
  );
};
