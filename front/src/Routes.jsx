import {
  BrowserRouter as Router,
  Routes,
  Route,
  useLocation,

} from "react-router-dom";

import React from "react";
import { Error404 } from "./container/error/Error404.jsx";
import About from "./container/pages/About.jsx";
import  Blog  from "@container/pages/Blog.jsx";
import  Post  from "@container/pages/Post.jsx";
import { Cases } from "./container/pages/Cases.jsx";
import  Contact  from "@container/pages/Contact.jsx";
import { Home } from "./container/pages/Home.jsx";
import { Services} from "./container/pages/Services.jsx";
import Category from "@container/pages/Category.jsx";
import Search from "@container/pages/Search.jsx";





export const AnimateRoutes = ({data,index}) => {
  const location = useLocation();

  return (
    <Routes location={location} key={location.pathname}>
      <Route path="*" element={<Error404 />} />
      <Route path="/" element={<Home />}></Route>
      <Route exact path="/about" element={<About />}></Route>
      <Route exact path= "/blog" element={<Blog />}>  </Route>
       <Route exact path= "/blog/detail/:slug" element={<Post />}>  </Route>
      <Route exact path="/cases" element={<Cases />}></Route>
      <Route exact path="/contact" element={<Contact />}></Route>
      <Route exact path="/services" element={<Services />}></Route>
       <Route exact path="/category/:slug" element={<Category/>}></Route>
      <Route  path="/search/:term" element={<Search />}></Route>

    </Routes>
  );
};
